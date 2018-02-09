#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Example of running CPNest to fit the parameters of a straight line.
"""

from __future__ import print_function, division

import os
import sys
import six
import numpy as np

# import CPNest
from cpnest.model import Model
import cpnest

# import model and data
from createdata import *

LN2PI = np.log(2.*np.pi)
LNSIGMA = np.log(sigma)

# set the model, likelihood and prior
class StraightLineModel(Model):
    """
    A simple straight line model, with a Gaussian likelihood.
    
    Args:
        data (:class:`numpy.ndarray`): an array containing the observed data
        abscissa (:class:`numpy.ndarray`): an array containing the points at which the data were taken
        modelfunc (function): a function defining the model
        sigma (float): the standard deviation of the noise in the data
        
    """
    names = ['m','c'] # parameter names (this is a required variables for the class)

    # define the boundaries using for initial sampling of the live points
    cmin = -10.  # lower range on c (the same as the uniform c prior lower bound)
    cmax = 10.   # upper range on c (the same as the uniform c prior upper bound)

    mmu = 0.     # mean of the Gaussian prior on m
    msigma = 10. # standard deviation of the Gaussian prior on m

    cbounds = [cmin, cmax]
    # set the m bounds to be +/- 10sigma about the mean
    mbounds = [mmu-10.*msigma, mmu+10.*msigma]

    # NOTE: the bounds could instead be set through arguments passed to the __init__
    # function for the class if wanted
    bounds=[mbounds, cbounds] # upper and lower bounds on each parameter (required for the class)

    def __init__(self, data, abscissa, modelfunc, sigma):
        # set the data
        self._data = data         # oberserved data
        self._abscissa = abscissa # points at which the observed data are taken
        self._sigma = sigma       # standard deviation(s) of the data
        self._logsigma = np.log(sigma) # log sigma here to save computations in the likelihood
        self._ndata = len(data)   # number of data points
        self._model = modelfunc   # model function

    def log_likelihood(self, params):
        """
        The natural logarithm of the likelihood function.

        Args:
            params (dict): a dictionary keyed to the parameter names.

        Returns:
            float: the log likelihood value.
        """
        # extract the parameters
        m = params['m']
        c = params['c']

        # calculate the model
        model = self._model(x, m, c)

        # normalisation
        norm = -0.5*self._ndata*LN2PI - self._ndata*self._logsigma

        # chi-squared
        chisq = np.sum(((self._data - model)/(self._sigma))**2)

        return norm - 0.5*chisq

    def log_prior(self,p):
        """
        The natural logarithm of the prior function.

        Args:
            p (dict): a dictionary keyed to parameter names.

        Returns:
            float: The log prior value.
        """
        # the uniform priors are dealt with by just checking that we're within the bounds
        if not self.in_bounds(p): return -np.inf # check parameters are all in bounds

        # Gaussian prior on m
        lp = 0.
        m = p['m']
        lp -= 0.5*((m-self.mmu)/self.msigma)**2 # no need for normalisation constant on the prior

        return lp

nlive = 1024      # number of live point
maxmcmc = 1024    # maximum MCMC chain length
nthreads = 1      # use one CPU core

# set up the algorithm
work = cpnest.CPNest(StraightLineModel(data, x, straight_line, sigma), verbose=0,
                     Nthreads=nthreads, Nlive=nlive, maxmcmc=maxmcmc);

# run the algorithm
work.run();

logZcpnest = work.NS.logZ                     # value of log Z
infogaincpnest = work.NS.state.info           # value of the information gain
logZerrcpnest = np.sqrt(infogaincpnest/nlive) # estimate of the statistcal uncertainty on logZ

# get the null log likelihood (evidence that the data is Gaussian noise with zero mean, and given standard devaition)
logZnull = work.user.log_likelihood({'m': 0., 'c': 0.})

print(six.u('Marginalised evidence is {} \u00B1 {}'.format(logZcpnest, logZerrcpnest)))

# output the log Bayes factor
print('log Bayes factor is {}'.format(logZcpnest - logZnull))

mchain_cpnest = work.posterior_samples['m'] # extract chain of m values
cchain_cpnest = work.posterior_samples['c'] # extract chain if c values
postsamples = np.vstack((mchain_cpnest, cchain_cpnest)).T

# plot posterior samples (if corner.py is installed)
try:
    import matplotlib as mpl
    mpl.use("Agg") # force Matplotlib backend to Agg
    import corner # import corner.py
except ImportError:
    sys.exit(1)

fig = corner.corner(postsamples, labels=[r"$m$", r"$c$"], truths=[m, c])
fig.savefig('CPNest.png')

