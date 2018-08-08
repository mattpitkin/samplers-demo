#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Example of running edward to fit the parameters of a straight line.
"""

from __future__ import print_function, division

import os
import sys
import numpy as np

import matplotlib as mpl
mpl.use("Agg") # force Matplotlib backend to Agg

# import edward and TensorFlow
import edward as ed
import tensorflow as tf
from edward.models import Normal, Uniform, Empirical

# import model and data
from createdata import *

# set the priors
cmin = -10. # lower range of uniform distribution on c
cmax = 10.  # upper range of uniform distribution on c
cp = Uniform(low=cmin, high=cmax)

mmu = 0.     # mean of Gaussian distribution on m
msigma = 10. # standard deviation of Gaussian distribution on m
mp = Normal(loc=mmu, scale=msigma)

# set the likelihood containing the model
y = Normal(loc=mp*x + cp, scale=sigma*tf.ones(len(data)))

# set number of samples
Nsamples = 2000 # final number of samples
Ntune = 2000    # number of tuning samples

# set parameters to infer
qm = Empirical(params=tf.Variable(tf.zeros(Nsamples+Ntune)))
qc = Empirical(params=tf.Variable(tf.zeros(Nsamples+Ntune)))

# use Hamiltonian Monte Carlo
inference = ed.HMC({mp: qm, cp: qc}, data={y: data})
inference.run(step_size=1.5e-2) # higher steps sizes can lead to zero acceptance rates

# extract the samples
msamples = qm.params.eval()[Ntune:]
csamples = qc.params.eval()[Ntune:]
postsamples = np.vstack((msamples, csamples)).T

# plot posterior samples (if corner.py is installed)
try:
    import corner # import corner.py
except ImportError:
    sys.exit(1)

print('Number of posterior samples is {}'.format(postsamples.shape[0]))

fig = corner.corner(postsamples, labels=[r"$m$", r"$c$"], truths=[m, c])
fig.savefig('edward.png')

