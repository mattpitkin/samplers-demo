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
import PyPolyChord as PolyChord

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
    c = cprime*(cmax-cmin) + cmin  # convert back to c

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

# run nested sampling
PolyChord.run_nested_sampling(loglikelihood_polychord, ndims, nderived, prior=prior_transform_polychord, precision_criterion=tol, nlive=nlive, file_root=fileroot, base_dir=basedir, write_resume=False, read_resume=False)

# reset stack resource size
resource.setrlimit(resource.RLIMIT_STACK, curlimit)

# output marginal likelihood
statsfile = broot+'.stats'
fp = open(statsfile, 'r')
statslines = fp.readlines()
fp.close()
for line in statslines:
    sp = [sv.strip() for sv in line.split()]
    if len(sp):
        if sp[0] == 'log(Z)':
            logZ = float(sp[2])    # marginal likelihood value
            logZerr = float(sp[4]) # marginal likelihood uncertainty
            break

print(u'Marginalised evidence is {} \u00B1 {}'.format(logZ, logZerr).encode('utf-8'))

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

