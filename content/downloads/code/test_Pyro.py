#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Example of running pyro to fit the parameters of a straight line.
"""

from __future__ import print_function, division

import os
import sys
import numpy as np

import matplotlib as mpl
mpl.use("Agg") # force Matplotlib backend to Agg

# import torch and pyro
import torch
import pyro
import pyro.distributions as dist
import pyro.poutine as poutine
from pyro.infer import MCMC, NUTS

# import model and data
from createdata import *

def linear_model(sigma, x):
    """
    Args:
        sigma (float): the noise standard deviation of the data
        x (tensor): the abscissa variable
    """

    # set prior parameters
    cmin = -10. # lower range of uniform distribution on c
    cmax = 10.  # upper range of uniform distribution on c
    
    mmu = 0.     # mean of Gaussian distribution on m
    msigma = 10. # standard deviation of Gaussian distribution on m
    
    # set priors for unknown parameters
    cmodel = pyro.sample("c", dist.Uniform(cmin, cmax))
    mmodel = pyro.sample("m", dist.Normal(mmu, msigma))

    # the linear model
    mu = mmodel * x + cmodel

    # return sample from the model
    return pyro.sample("obs", dist.Normal(mu, sigma))


def conditioned_linear_model(model, sigma, data, x):
    """
    Args:
        model (func): the probabilistic model function
        sigma (float): the noise standard deviation of the data
        data (tensor): the observed data
        x (tensor): the abscissa variable
    """

    return poutine.condition(model, data={"obs": data})(sigma, x)


Nsamples = 1000 # final number of samples
Ntune = 1000    # number of "warm up"/burn-in samples
Nchains = 1     # number of chains

# set up to use the NUTS sampler
nuts_kernel = NUTS(conditioned_linear_model, jit_compile=False)

# set up the MCMC
mcmc = MCMC(nuts_kernel,
            num_samples=Nsamples,
            warmup_steps=Ntune,
            num_chains=Nchains)

# perform the sampling (convert the data and abscissa variable to
# pytorch tensors)
mcmc.run(
    linear_model,
    sigma,                                  # noise standard deviation
    torch.tensor(data).type(torch.Tensor),  # the data
    torch.tensor(x).type(torch.Tensor),     # the abscissa values
)

# extract the samples
samples = mcmc.get_samples()
postsamples = np.vstack((samples["m"].numpy(), samples["c"].numpy())).T

# plot posterior samples (if corner.py is installed)
try:
    import corner # import corner.py
except ImportError:
    sys.exit(1)

print('Number of posterior samples is {}'.format(postsamples.shape[0]))

fig = corner.corner(postsamples, labels=[r"$m$", r"$c$"], truths=[m, c])
fig.savefig('Pyro.png')
