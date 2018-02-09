title: Samplers demo
slug: index
Template: index

This site aims gives a demonstration of nine different [MCMC](https://en.wikipedia.org/wiki/Markov_chain_Monte_Carlo)
and [nested sampling](https://en.wikipedia.org/wiki/Nested_sampling_algorithm) algorithms that are
either written in Python, or have Python-wrapper implementations. The demostration is a simple toy
model of estimating the posteriors on the parameters of a straight line in Gaussian noise. The
samplers used are:

## MCMC:
   
1. [emcee](http://dfm.io/emcee/current/)
2. [PyMC3](http://docs.pymc.io/)
3. [PyStan](http://pystan.readthedocs.io/en/latest/)
4. [PyJAGS](https://pyjags.readthedocs.io/en/latest/)

## Nested Sampling:

1. [Nestle](http://kylebarbary.com/nestle/)
2. [CPNest](https://johnveitch.github.io/cpnest/)
3. [PyMultiNest](https://johannesbuchner.github.io/PyMultiNest/)
4. [DNest4](https://github.com/eggplantbren/DNest4)
5. [PyPolyChord](https://ccpforge.cse.rl.ac.uk/gf/project/polychord/)

A page showing a demonstration and comparison of all the samplers on a fixed dataset can be found
[here](http://mattpitkin.github.io/samplers-demo/pages/samplers-samplers-everywhere/).

Standalone example for each sampler will be coming soon, along with information on [Docker](https://docs.docker.com/)
images that can be used to run all the samplers mentioned above.

### The author

My name is Matthew Pitkin and I'm an astrophysicist working on gravitational wave data analysis in
the [Institute for Gravitational Research](http://www.physics.gla.ac.uk/igr/) at the [University of Glasgow](https://www.gla.ac.uk/).
