#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Example of running TensorFlow probability + edward2 to fit the parameters of a straight line.
"""

from __future__ import print_function, division

import os
import sys
import numpy as np

import matplotlib as mpl
mpl.use("Agg") # force Matplotlib backend to Agg

# import edward2 and TensorFlow probability
import tensorflow_probability as tfp
from tensorflow_probability import edward2 as ed
import tensorflow as tf

# import model and data
from createdata import *

cmin = -10. # lower range of uniform distribution on c
cmax = 10.  # upper range of uniform distribution on c

mmu = 0.     # mean of Gaussian distribution on m
msigma = 10. # standard deviation of Gaussian distribution on m

# create a log-likelihood function
def log_likelihood(data, x, cmin, cmax, mmu, msigma, sigma, testc, testm):
    c = tfp.distributions.Uniform(low=cmin, high=cmax, name="c")
    m = tfp.distributions.Normal(loc=mmu, scale=msigma, name="m")

    y = tfp.distributions.Normal(loc=(testm*x + testc), scale=sigma, name="y")

    return c.log_prob(testc) + m.log_prob(testm) + tf.reduce_sum(y.log_prob(data))

# set initial state (drawn from prior)
qc = tf.random_uniform([], minval=cmin, maxval=cmax, dtype=tf.float32)
qm = tf.random_normal([], mean=mmu, stddev=msigma, dtype=tf.float32)

# convert x values and data to tensors
x = tf.convert_to_tensor(x, dtype=tf.float32)
data = tf.convert_to_tensor(data, dtype=tf.float32)

def target_log_prob_fn(c, m):
    """Target log-probability as a function of states."""
    return log_likelihood(data, x, cmin, cmax, mmu, msigma, sigma, c, m)

Nsamples = 2000  # final number of samples
Nburn = 2000     # number of tuning samples

# set up Hamiltonian MC
hmc_kernel = tfp.mcmc.HamiltonianMonteCarlo(
    target_log_prob_fn=target_log_prob_fn,
    step_size=0.015,
    num_leapfrog_steps=5)

states, kernels_results = tfp.mcmc.sample_chain(
    num_results=Nsamples,
    current_state=[qc, qm],
    kernel=hmc_kernel,
    num_burnin_steps=Nburn)

# extract the samples
with tf.Session():
    cs = states[0].eval()
    ms = states[1].eval()

postsamples = np.vstack((ms, cs)).T
print(postsamples)

# plot posterior samples (if corner.py is installed)
try:
    import corner # import corner.py
except ImportError:
    sys.exit(1)

print('Number of posterior samples is {}'.format(postsamples.shape[0]))

fig = corner.corner(postsamples, labels=[r"$m$", r"$c$"], truths=[m, c])
fig.savefig('edward2.png')
