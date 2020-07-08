#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Example of running PyMC4 to fit the parameters of a straight line.
"""

from __future__ import print_function, division

import os
import sys
import numpy as np

import matplotlib as mpl
mpl.use("Agg") # force Matplotlib backend to Agg

# import PyMC4
import pymc4 as pm4
import tensorflow as tf

# import model and data
from createdata import *

cmin = -10.  # lower range of uniform distribution on c
cmax = 10.   # upper range of uniform distribution on c

mmu = 0.      # mean of Gaussian distribution on m
msigma = 10.  # standard deviation of Gaussian distribution on m

# convert x values and data to tensors
xtensor = tf.convert_to_tensor(x, dtype=tf.float32)
datatensor = tf.convert_to_tensor(data, dtype=tf.float32)

# model must be wrapped with the model decorator
@pm4.model
def model(x, data, sigma=sigma):
    cvalue = yield pm4.Uniform(name='c', low=cmin, high=cmax)  # prior on c
    mvalue = yield pm4.Normal(name='m', loc=mmu, scale=msigma) # prior on m
    
    # the straight line model
    mu = cvalue + mvalue * x
    
    # the likelihood
    yield pm4.Normal(name='t_obs', loc=mu, scale=sigma, observed=data)

Nsamples = 2000  # final number of samples
Nburn = 2000     # number of tuning samples

# perform the sampling
pymc4_trace = pm4.sample(
    model(xtensor, datatensor),
    num_chains=1,
    burn_in=Nburn,
    num_samples=Nsamples,
)

postsamples = np.vstack((
    pymc4_trace.posterior["model/m"].data.flatten(),
    pymc4_trace.posterior["model/c"].data.flatten()
)).T

# plot posterior samples (if corner.py is installed)
try:
    import corner # import corner.py
except ImportError:
    sys.exit(1)

print('Number of posterior samples is {}'.format(postsamples.shape[0]))

fig = corner.corner(postsamples, labels=[r"$m$", r"$c$"], truths=[m, c])
fig.savefig('pymc4.png')
