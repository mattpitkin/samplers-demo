#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Example of running DNest4 to fit the parameters of a straight line.
"""

from __future__ import print_function, division

import os
import sys
import six
import numpy as np

# import DNest4
from dnest4 import randh
import dnest4

# import model and data
from createdata import *

LN2PI = np.log(2.*np.pi)
LNSIGMA = np.log(sigma)

# Create model class
class DNest4Model(object):
    """
    Specify the model in Python.
    """
    def __init__(self):
        """
        Parameter values *are not* stored inside the class
        """
        pass

    def from_prior(self):
        """
        Draw points from the prior distribution.

        Returns:
            :class:`np.ndarray`: a numpy array containing the parameter values.
        
        """

        cmin = -10.  # lower range on c (the same as the uniform c prior lower bound)
        cmax = 10.   # upper range on c (the same as the uniform c prior upper bound)

        mmu = 0.     # mean of the Gaussian prior on m
        msigma = 10. # standard deviation of the Gaussian prior on m

        m = np.random.normal(mmu, msigma)
        c = np.random.uniform(cmin,  cmax)

        return np.array([m, c])

    def perturb(self, params):
        """
        Perturb the current parameters by proposing a new position. This takes a numpy array of
        parameters as input, and modifies it in-place. In just perturbs one parameter at a time.

        Args:
            params (:class:`np.ndarray`): the current parameters (this is modified by the function)

        Returns:
            float: the natural logarithm of the Metropolis-Hastings proposal ratio.
        """
        logH = 0.0 # log of the Metropolis-Hastings prior x proposal ratio
        
        # randomly choose which parameter to perturb 
        which = np.random.randint(len(params))
        mmu = 0.
        msigma = 10.
        if which == 0:
            # update H for Gaussian prior
            logH -= -0.5*((params[which]-mmu)/msigma)**2
        params[which] += 10.*randh() # scale factor of 10, which is ~the prior width
        if which == 0:
            # update H for Gaussian prior
            logH += -0.5*((params[which]-mmu)/msigma)**2

        return logH

    def log_likelihood(self, params):
        """
        Gaussian sampling distribution.
        """
        m, c = params # unpack parameters
        
        norm = -0.5*M*LN2PI - M*LNSIGMA
        chisq = np.sum(((data - straight_line(x, m, c))/sigma)**2)
        return norm - 0.5*chisq

# Create a model object and a sampler
model = DNest4Model()
sampler = dnest4.DNest4Sampler(model, backend=dnest4.backends.CSVBackend(".", sep=" "))

# Set up the sampler. The first argument is max_num_levels
gen = sampler.sample(max_num_levels=30, num_steps=1000, new_level_interval=10000,
                     num_per_step=10000, thread_steps=100, num_particles=5, lam=10, beta=100)

# Do the sampling (one iteration here = one particle save)
t0 = time()
for sample in enumerate(gen):
    pass

# run the algorithm
solution = StraightLineModelPyMultiNest(data, x, straight_line, sigma, n_dims=ndim,
                                        n_live_points=nlive, evidence_tolerance=tol);

# Run the postprocessing to get marginal likelihood and generate posterior samples
logZdnest4, infogaindnest4, _ = dnest4.postprocess(plot=False);

postsamples = np.loadtxt('posterior_sample.txt')

print(six.u('Marginalised evidence is {}'.format(logZdnest4)))

print('Number of posterior samples is {}'.format(postsamples.shape[0]))

# plot posterior samples (if corner.py is installed)
try:
    import matplotlib as mpl
    mpl.use("Agg") # force Matplotlib backend to Agg
    import corner # import corner.py
except ImportError:
    sys.exit(1)

fig = corner.corner(postsamples, labels=[r"$m$", r"$c$"], truths=[m, c])
fig.savefig('DNest4.png')

