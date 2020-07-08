#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Example of running UltraNest to fit the parameters of a straight line.
"""

from __future__ import print_function, division

import os
import sys
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

# import UltraNest
import ultranest

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

tol = 0.5         # the stopping criterion

# set the ReactiveNestedSampler method
sampler = ultranest.ReactiveNestedSampler(
    ["m", "c"], loglikelihood_ultranest, prior_transform_ultranest
)

tol = 0.5         # the stopping criterion

# run the nested sampling algorithm
result = sampler.run(dlogz=tol)

logZultranest = result['logz']        # value of logZ
logZerrultranest = result['logzerr']  # estimate of the statistcal uncertainty on logZ

# output marginal likelihood
print('Marginalised evidence is {} ± {}'.format(logZultranest, logZerrultranest))

# get the posterior samples
data = np.array(result["weighted_samples"]["points"])
weights = np.array(result["weighted_samples"]["weights"])
scaledweights = weights / weights.max()
mask = np.random.rand(len(scaledweights)) < scaledweights

samples_ultranest = data[mask, :]

print('Number of posterior samples is {}'.format(postsamples.shape[0]))

if doplot:
    fig = corner.corner(postsamples, labels=[r"$m$", r"$c$"], truths=[m, c])
    fig.savefig('UltraNest.png')
