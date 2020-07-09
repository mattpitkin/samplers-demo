#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Example of running TensorFlow probability to fit the parameters of a straight line.
"""

import os
import sys
import numpy as np

import matplotlib as mpl
mpl.use("Agg") # force Matplotlib backend to Agg

# import TensorFlow probability
import tensorflow_probability as tfp
from tensorflow_probability import distributions as tfd
import tensorflow as tf

# import model and data
from createdata import *

cmin = -10. # lower range of uniform distribution on c
cmax = 10.  # upper range of uniform distribution on c

mmu = 0.     # mean of Gaussian distribution on m
msigma = 10. # standard deviation of Gaussian distribution on m

# convert x values and data to 32 bit float
x = x.astype(np.float32)  # x is being use globally here
data = data.astype(np.float32)

# set model - contains priors and the expected linear model
model = tfd.JointDistributionSequential([
  tfd.Normal(loc=mmu, scale=msigma, name="m"),  # m prior
  tfd.Uniform(cmin, cmax, name="c"),  # c prior
  lambda c, m: (tfd.Independent(
        tfd.Normal(loc=(m[..., tf.newaxis] * x + c[..., tf.newaxis]), scale=sigma),
        name="data",
        reinterpreted_batch_ndims=1,
    ))
])

def target_log_prob_fn(mvalue, cvalue):
    """Unnormalized target density as a function of states."""
    return model.log_prob(
        (mvalue, cvalue, data)
    )

Nsamples = 2000 # final number of samples
Nburn = 2000    # number of tuning samples

# set up Hamiltonian MC (within TensorFlow function to speed up computation)
@tf.function(autograph=False)
def do_sampling():
    # set initial state (random draw from prior)
    qc = tf.random.uniform([], minval=cmin, maxval=cmax, name="init_c")
    qm = tf.random.normal([], stddev=msigma, mean=mmu, name="init_m")

    hmc_kernel = tfp.mcmc.NoUTurnSampler(
        target_log_prob_fn=target_log_prob_fn,
        step_size=0.01,
    )

    return tfp.mcmc.sample_chain(
        num_results=Nsamples,
        current_state=[qm, qc],
        kernel=hmc_kernel,
        num_burnin_steps=Nburn,
    )

states, kernel_results = do_sampling()

# extract the samples
cs, ms = states

# convert output states to numpy arrays
postsamples = np.vstack((ms.numpy(), cs.numpy())).T

# plot posterior samples (if corner.py is installed)
try:
    import corner # import corner.py
except ImportError:
    sys.exit(1)

print('Number of posterior samples is {}'.format(postsamples.shape[0]))

fig = corner.corner(postsamples, labels=[r"$m$", r"$c$"], truths=[m, c])
fig.savefig('tfp.png')
