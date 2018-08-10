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

# create a log-likeihood function
def log_likelihood(x, cmin, cmax, mmu, msigma, sigma, size):
    c = ed.Uniform(cmin, cmax, sample_shape=[1], name="c")
    m = ed.Normal(mmu, msigma, sample_shape=[1], name="m")

    y = ed.Normal(tf.add(tf.multiply(m, x), c), sigma*tf.ones(size, dtype=tf.float32), name="y")

    return y

# make function
log_joint = ed.make_log_joint_fn(log_likelihood)

# set initial state (drawn from prior)
qc = tf.random_uniform([1], minval=cmin, maxval=cmax, dtype=tf.float32)
qm = tf.random_normal([1], mean=mmu, stddev=msigma, dtype=tf.float32)

# convert x values and data to tensors
size = len(x)
x = tf.convert_to_tensor(x, dtype=tf.float32)
data = tf.convert_to_tensor(data, dtype=tf.float32)

def target_log_prob_fn(c, m):
    """Target log-probability as a function of states."""
    return log_joint(x, cmin, cmax, mmu, msigma, sigma, size,
                     c=c, m=m, y=data)

Nsamples = 2000 # final number of samples
Nburn = 2000    # number of tuning samples

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

postsamples = np.hstack((ms, cs))
print(postsamples)

# plot posterior samples (if corner.py is installed)
try:
    import corner # import corner.py
except ImportError:
    sys.exit(1)

print('Number of posterior samples is {}'.format(postsamples.shape[0]))

fig = corner.corner(postsamples, labels=[r"$m$", r"$c$"], truths=[m, c])
fig.savefig('edward2.png')

