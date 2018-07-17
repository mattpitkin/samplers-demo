#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Example of running UltraNest to fit the parameters of a straight line.
"""

from __future__ import print_function, division

import os
import sys
import six
from scipy.special import ndtri
import numpy as np

# plot posterior samples (if corner.py is installed)
try:
    # set backend now as nested_samplers module tries changing backend
    import matplotlib as mpl
    mpl.use("Agg") # force Matplotlib backend to Agg
    import corner # import corner.py
    doplot = True
except ImportError:
    doplot = False

# import UltraNest modules
from nested_sampling.samplers.hiermetriclearn import MetricLearningFriendsConstrainer
from nested_sampling.nested_integrator import nested_integrator
from nested_sampling.nested_sampler import NestedSampler
from nested_sampling.termination_criteria import TerminationCriterion
from nested_sampling.postprocess import equal_weighted_posterior

# import model and data
from createdata import *

LN2PI = np.log(2.*np.pi)
LNSIGMA = np.log(sigma)

def prior_transform(theta):
    """
    A function defining the tranform between the parameterisation in the unit hypercube
    to the true parameters.

    Args:
        theta (list): a list/array containing the parameters.
        
    Returns:
        list: a new list/array with the transformed parameters.
    """

    # unpack the parameters (in their unit hypercube form)
    mprime = theta[0]
    cprime = theta[1]

    cmin = -10.  # lower bound on uniform prior on c
    cmax = 10.   # upper bound on uniform prior on c

    mmu = 0.     # mean of Gaussian prior on m
    msigma = 10. # standard deviation of Gaussian prior on m

    m = mmu + msigma*ndtri(mprime) # convert back to m
    c = cprime*(cmax-cmin) + cmin  # convert back to c

    return np.array([m, c])

def loglikelihood_ultranest(theta):
    """
    The log-likelihood function.
    """

    # unpack the parameters
    m = theta[0]
    c = theta[1]

    # normalisation
    norm = -0.5*M*LN2PI - M*LNSIGMA

    # chi-squared (data, sigma and x are global variables defined early on in this notebook)
    chisq = np.sum(((data-straight_line(x, m, c))/sigma)**2)

    return norm - 0.5*chisq

nlive = 1024      # number of live points
ndims = 2         # two parameters
tol = 0.5         # the stopping criterion

# set "constrainer" for sampling the constrained prior
constrainer = MetricLearningFriendsConstrainer(metriclearner='truncatedscaling', force_shrink=True, rebuild_every=50, verbose=False)

# set termination condition
termination = TerminationCriterion(tolerance=tol, maxRemainderFraction=0.001)

# set the sampler
sampler = NestedSampler(nlive_points=nlive, priortransform=prior_transform, loglikelihood=loglikelihood_ultranest, draw_constrained=constrainer.draw_constrained, ndim=ndims, constrainer_get_Lmax=constrainer.get_Lmax)

constrainer.sampler = sampler

# run the nested sampling algorithm
result = nested_integrator(sampler, termination)

logZultranest = result['logZ']        # value of logZ
logZerrultranest = result['logZerr']  # estimate of the statistcal uncertainty on logZ

# output marginal likelihood
print(six.u('Marginalised evidence is {} \u00B1 {}'.format(logZultranest, logZerrultranest)))

# get the posterior samples (first output is samples in the unit hypercube, so ignore that)
nsamples = np.array([xi for ui, xi, Li, logwidth in result['weights']])
probs = np.array([Li + logwidth for ui, xi, Li, logwidth in result['weights']])
probs = np.exp(probs - probs.max())

keepidx = np.where(np.random.rand(len(probs)) < probs)[0]

postsamples = nsamples[keepidx,:]

print('Number of posterior samples is {}'.format(postsamples.shape[0]))

if doplot:
    fig = corner.corner(postsamples, labels=[r"$m$", r"$c$"], truths=[m, c])
    fig.savefig('UltraNest.png')

