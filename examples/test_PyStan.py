#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Example of running emcee to fit the parameters of a straight line.
"""

from __future__ import print_function, division

import os
import sys
import numpy as np

import matplotlib as mpl
mpl.use("Agg") # force Matplotlib backend to Agg

# import PyStan
import pystan

# import model and data
from createdata import *

# Create model code
line_code = """
data {{
    int<lower=0> N;      // number of data points
    real y[N];           // observed data points
    real x[N];           // abscissa points
    real<lower=0> sigma; // standard deviation
}}
parameters {{
    // parameters for the fit
    real m;
    real c;
}}
transformed parameters {{
    real theta[N];
    for (j in 1:N)
    theta[j] = m * x[j] + c; // straight line model
}}
model {{
    m ~ normal({mmu}, {msigma});     // prior on m (gradient)
    c ~ uniform({clower}, {cupper}); // prior on c (y-intercept)
    y ~ normal(theta, sigma);        // likelihood of the data given the model
}}
"""

# set the data and the abscissa
linear_data = {'N': M,          # number of data points
               'y': data,       # observed data (converted from numpy array to a list)
               'x': x,          # abscissa points (converted from numpy array to a list)
               'sigma': sigma}  # standard deviation

Nsamples = 1000 # set the number of iterations of the sampler
chains = 4      # set the number of chains to run with

# dictionary for inputs into line_code
linedict = {}
linedict['mmu'] = 0.0    # mean of Gaussian prior distribution for m
linedict['msigma'] = 10  # standard deviation of Gaussian prior distribution for m
linedict['clower'] = -10 # lower bound on uniform prior distribution for c
linedict['cupper'] = 10  # upper bound on uniform prior distribution for c

sm = pystan.StanModel(model_code=line_code.format(**linedict)); # compile model
fit = sm.sampling(data=linear_data, iter=Nsamples, chains=chains); # perform sampling

la = fit.extract(permuted=True)  # return a dictionary of arrays

# extract the samples
postsamples = np.vstack((la['m'], la['c'])).T

# plot posterior samples (if corner.py is installed)
try:
    import corner # import corner.py
except ImportError:
    sys.exit(1)

print('Number of posterior samples is {}'.format(postsamples.shape[0]))

fig = corner.corner(postsamples, labels=[r"$m$", r"$c$"], truths=[m, c])
fig.savefig('PyStan.png')

