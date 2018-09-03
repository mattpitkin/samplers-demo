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

cmin = -10.  # lower range of uniform distribution on c
cmax = 10.   # upper range of uniform distribution on c

mmu = 0.      # mean of Gaussian distribution on m
msigma = 10.  # standard deviation of Gaussian distribution on m

# create a log-likelihood function
def log_likelihood(x, cmin, cmax, mmu, msigma, sigma):
    m = ed.Normal(loc=mmu, scale=msigma, name="m")
    c = ed.Uniform(low=cmin, high=cmax, name="c")

    y = ed.Normal(loc=(m*x + c), scale=sigma, name="y")
    return y

# set initial state (drawn from prior)
qm = tf.random_normal([], mean=mmu, stddev=msigma, dtype=tf.float32)
qc = tf.random_uniform([], minval=cmin, maxval=cmax, dtype=tf.float32)

# convert x values and data to tensors
x = tf.convert_to_tensor(x, dtype=tf.float32)
data = tf.convert_to_tensor(data, dtype=tf.float32)

# make function
log_joint = ed.make_log_joint_fn(log_likelihood)

def target_log_prob_fn(m, c):
    """Target log-probability as a function of states."""
    return log_joint(x, cmin, cmax, mmu, msigma, sigma, m=m, c=c,
                     y=data)

Nsamples = 2000  # final number of samples
Nburn = 2000     # number of tuning samples

# set up Hamiltonian MC
hmc_kernel = tfp.mcmc.HamiltonianMonteCarlo(
    target_log_prob_fn=target_log_prob_fn,
    step_size=0.01,
    num_leapfrog_steps=5)

states, kernel_results = tfp.mcmc.sample_chain(
    num_results=Nsamples,
    current_state=[qm, qc],
    kernel=hmc_kernel,
    num_burnin_steps=Nburn)

# run the session to extract the samples
with tf.Session() as sess:
    states, is_accepted_ = sess.run([states, kernel_results.is_accepted])
    accepted = np.sum(is_accepted_)
    print("Acceptance rate: {}".format(accepted / Nsamples))

results = dict(zip(['m', 'c'], states))

postsamples = np.vstack((results['m'], results['c'])).T
print(postsamples)

# plot posterior samples (if corner.py is installed)
try:
    import corner # import corner.py
except ImportError:
    sys.exit(1)

print('Number of posterior samples is {}'.format(postsamples.shape[0]))

fig = corner.corner(postsamples, labels=[r"$m$", r"$c$"], truths=[m, c])
fig.savefig('tensorflow_probability.png')
