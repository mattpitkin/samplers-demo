#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Example of running PyPolyChord to fit the parameters of a straight line.
"""

from __future__ import print_function, division

import os
import sys
from scipy.special import ndtri
import numpy as np
import resource

# import PolyChord
import PyPolyChord
from PyPolyChord.settings import PolyChordSettings
from PyPolyChord.priors import UniformPrior

# import model and data
from createdata import *

LN2PI = np.log(2.*np.pi)
LNSIGMA = np.log(sigma)


def prior_transform_polychord(cube):
    """
    A function defining the tranform between the parameterisation in the unit hypercube
    to the true parameters.
    
    Args:
        cube (array, list): a list containing the parameters as drawn from a unit hypercube.
        
    Returns:
        list: the transformed parameters.
    """
    
    #mprime, cprime = cube # unpack the parameters (in their unit hypercube form)
    mprime = cube[0]
    cprime = cube[1]

    cmin = -10.  # lower bound on uniform prior on c
    cmax = 10.   # upper bound on uniform prior on c

    mmu = 0.     # mean of Gaussian prior on m
    msigma = 10. # standard deviation of Gaussian prior on m

    m = mmu + msigma*ndtri(mprime) # convert back to m
    c = UniformPrior(cmin, cmax)(cprime) # convert back to c using UniformPrior class

    theta = [m, c]
    
    return theta


def loglikelihood_polychord(theta):
    """
    The log-likelihood function.
    
    Args:
        theta (array, list): the set of parameter values.
        
    Returns:
        float: the log-likelihood value.
        list: A list of any derived parameters (an empty list if there are none)
    """

    # unpack the parameters
    m = theta[0]
    c = theta[1]

    # normalisation
    norm = -0.5*M*LN2PI - M*LNSIGMA

    # chi-squared (data, sigma and x are global variables defined early on in this notebook)
    chisq = np.sum(((data-straight_line(x, m, c))/sigma)**2)

    return norm - 0.5*chisq, []


nlive = 1024   # number of live points
ndims = 2      # number of parameters
nderived = 0   # number of derived parameters (this is zero)
tol = 0.5      # stopping criterion
basedir = os.path.join(os.getcwd(), 'polychord')   # output base directory
if not os.path.isdir(basedir):
    os.makedirs(basedir)                           # create base directory
    os.makedirs(os.path.join(basedir, 'clusters')) # 'clusters' directory

fileroot = 'straightline'                          # output file name
broot = os.path.join(basedir, fileroot)

# set an unlimited stack-size of PolyChord
curlimit = resource.getrlimit(resource.RLIMIT_STACK) # get current stack resource size
resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY,resource.RLIM_INFINITY)) # set to unlimited

# setup run settings using the PolyChordSetting class
pargs = {'nlive': nlive,
         'precision_criterion': tol,
         'base_dir': basedir,
         'file_root': fileroot,
         'write_resume': False, # don't output a resume file
         'read_resume': False}  # don't read a resume file
settings = PolyChordSettings(ndims, nderived, **pargs)

# run nested sampling
output = PyPolyChord.run_polychord(loglikelihood_polychord, ndims, nderived, settings, prior_transform_polychord)

# reset stack resource size
resource.setrlimit(resource.RLIMIT_STACK, curlimit)

# output marginal likelihood
print('Marginalised evidence is {} ± {}'.format(output.logZ, output.logZerr))

# plot posterior samples (if corner.py is installed)
try:
    import matplotlib as mpl
    mpl.use("Agg") # force Matplotlib backend to Agg
    import corner # import corner.py
except ImportError:
    sys.exit(1)

samplefile = broot+'_equal_weights.txt'
samples = np.loadtxt(samplefile)
postsamples = samples[:,2:]

print('Number of posterior samples is {}'.format(postsamples.shape[0]))

fig = corner.corner(postsamples, labels=[r"$m$", r"$c$"], truths=[m, c])
fig.savefig('PyPolyChord.png')
