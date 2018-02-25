#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Example of running PyJAGS to fit the parameters of a straight line.
"""

from __future__ import print_function, division

import os
import sys
import numpy as np

import matplotlib as mpl
mpl.use("Agg") # force Matplotlib backend to Agg

# import PyJAGS
import pyjags

# import model and data
from createdata import *

# Create model code
line_code_jags = '''
model {{
    for (i in 1:N) {{
        y[i] ~ dnorm(c + m * x[i], {invvar}) # Gaussian likelihood
    }}
    m ~ dnorm({mmu}, {minvvar})     # Gaussian prior on m
    c ~ dunif({clower}, {cupper})   # Uniform prior on c
}}
'''

datadict = {'x': x,    # abscissa points (converted from numpy array to a list)
            'N': M,    # number of data points
            'y': data} # the observed data

Nsamples = 1000 # set the number of iterations of the sampler
chains = 4      # set the number of chains to run with

# dictionary for inputs into line_code
linedict = {}
linedict['mmu'] = 0.0           # mean of Gaussian prior distribution for m
linedict['minvvar'] = 1/10**2   # inverse variance of Gaussian prior distribution for m
linedict['clower'] = -10        # lower bound on uniform prior distribution for c
linedict['cupper'] = 10         # upper bound on uniform prior distribution for c
linedict['invvar'] = 1/sigma**2 # inverse variance of the data

# compile model
model = pyjags.Model(line_code_jags.format(**linedict), data=datadict, chains=chains)
samples = model.sample(Nsamples, vars=['m', 'c']) # perform sampling

mchainjags = samples['m'].flatten()
cchainjags = samples['c'].flatten()

# extract the samples
postsamples = np.vstack((mchainjags, cchainjags)).T

# plot posterior samples (if corner.py is installed)
try:
    import corner # import corner.py
except ImportError:
    sys.exit(1)

print('Number of posterior samples is {}'.format(postsamples.shape[0]))

fig = corner.corner(postsamples, labels=[r"$m$", r"$c$"], truths=[m, c])
fig.savefig('PyJAGS.png')

