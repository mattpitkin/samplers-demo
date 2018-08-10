#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Example of running dynesty to fit the parameters of a straight line.
"""

from __future__ import print_function, division

import os
import sys
from scipy.special import ndtri
import numpy as np

# import dynesty (we'll give an example with both the static and
# dynamic nested samplers)
from dynesty.utils import resample_equal
from dynesty import NestedSampler, DynamicNestedSampler

# import model and data
from createdata import *

LN2PI = np.log(2.*np.pi)
LNSIGMA = np.log(sigma)

def prior_transform(theta):
    """
    A function defining the tranform between the parameterisation in the unit hypercube
    to the true parameters.

    Args:
        theta (tuple): a tuple containing the parameters.
        
    Returns:
        tuple: a new tuple or array with the transformed parameters.
    """

    mprime, cprime = theta # unpack the parameters (in their unit hypercube form)

    cmin = -10.  # lower bound on uniform prior on c
    cmax = 10.   # upper bound on uniform prior on c

    mmu = 0.     # mean of Gaussian prior on m
    msigma = 10. # standard deviation of Gaussian prior on m

    m = mmu + msigma*ndtri(mprime) # convert back to m
    c = cprime*(cmax-cmin) + cmin  # convert back to c

    return (m, c)

def loglikelihood_dynesty(theta):
    """
    The log-likelihood function.
    """

    m, c = theta # unpack the parameters

    # normalisation
    norm = -0.5*M*LN2PI - M*LNSIGMA

    # chi-squared (data, sigma and x are global variables defined early on in this notebook)
    chisq = np.sum(((data-straight_line(x, m, c))/sigma)**2)

    return norm - 0.5*chisq

nlive = 1024      # number of (initial) live points
bound = 'multi'   # use MutliNest algorithm
sample = 'rwalk'  # use the random walk to draw new samples
ndims = 2         # two parameters

dsampler = DynamicNestedSampler(loglikelihood_dynesty, prior_transform, ndims,
                                bound=bound, sample=sample)
dsampler.run_nested(nlive_init=nlive)
dres = dsampler.results

dlogZdynesty = dres.logz[-1]        # value of logZ
dlogZerrdynesty = dres.logzerr[-1]  # estimate of the statistcal uncertainty on logZ

# output marginal likelihood
print('Marginalised evidence (using dynamic sampler) is {} ± {}'.format(dlogZdynesty, dlogZerrdynesty))

# get the posterior samples
dweights = np.exp(dres['logwt'] - dres['logz'][-1])
dpostsamples = resample_equal(dres.samples, dweights)

print('Number of posterior samples (using dynamic sampler) is {}'.format(dpostsamples.shape[0]))

# Now run with the static sampler
sampler = NestedSampler(loglikelihood_dynesty, prior_transform, ndims,
                        bound=bound, sample=sample, nlive=nlive)
sampler.run_nested(dlogz=0.1)

res = sampler.results

logZdynesty = res.logz[-1]        # value of logZ
logZerrdynesty = res.logzerr[-1]  # estimate of the statistcal uncertainty on logZ

# output marginal likelihood
print('Marginalised evidence (using static sampler) is {} ± {}'.format(logZdynesty, logZerrdynesty))

# get the posterior samples
weights = np.exp(res['logwt'] - res['logz'][-1])
postsamples = resample_equal(res.samples, weights)

print('Number of posterior samples (using static sampler) is {}'.format(postsamples.shape[0]))

# plot posterior samples (if corner.py is installed)
try:
    import matplotlib as mpl
    mpl.use("Agg") # force Matplotlib backend to Agg
    import corner # import corner.py
except ImportError:
    sys.exit(1)

fig = corner.corner(dpostsamples, labels=[r"$m$", r"$c$"], truths=[m, c], hist_kwargs={'density': True})
fig = corner.corner(postsamples, fig=fig, color='r', hist_kwargs={'density': True})

fig.savefig('dynesty.png')
