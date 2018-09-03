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
import tensorflow as tf # For Random Variable operation
from tensorflow_probability import edward2 as ed # For defining random variables

# import model and data
from createdata import *

cmin = -10.  # lower range of uniform distribution on c
cmax = 10.   # upper range of uniform distribution on c

mmu = 0.      # mean of Gaussian distribution on m
msigma = 10.  # standard deviation of Gaussian distribution on m

# convert x values and data to tensors
x = tf.convert_to_tensor(x, dtype=tf.float32)
data = tf.convert_to_tensor(data, dtype=tf.float32)

# PyMC4 specific model initialisation
pymc4_linear_regression = pm4.Model(y=data, x=x, sigma=sigma, cmin=cmin, cmax=cmax,
                                    mmu=0., msigma=10.)

# create model
@pymc4_linear_regression.define
def process(cfg):
    c = ed.Uniform(low=cfg.cmin, high=cfg.cmax, name="c")
    m = ed.Normal(loc=cfg.mmu, scale=cfg.msigma, name="m")

    y = ed.Normal(loc=(m*cfg.x+c), scale=np.float32(cfg.sigma), name="y")
    return y

# add observed data
pymc4_linear_regression.observe(y=data)

Nsamples = 2000  # final number of samples
Nburn = 2000     # number of tuning samples

pymc4_trace = pm4.sample(pymc4_linear_regression, num_results=Nsamples,
                         num_burnin_steps=Nburn, step_size=0.01,
                         num_leapfrog_steps=5)

postsamples = np.vstack((pymc4_trace['m'], pymc4_trace['c'])).T
print(postsamples)

# plot posterior samples (if corner.py is installed)
try:
    import corner # import corner.py
except ImportError:
    sys.exit(1)

print('Number of posterior samples is {}'.format(postsamples.shape[0]))

fig = corner.corner(postsamples, labels=[r"$m$", r"$c$"], truths=[m, c])
fig.savefig('pymc4.png')
