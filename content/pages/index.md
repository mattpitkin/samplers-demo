title: Samplers demo
slug: index
Template: index

This site aims gives a demonstration of [nine different](#Samplers) [MCMC](https://en.wikipedia.org/wiki/Markov_chain_Monte_Carlo)
and [nested sampling](https://en.wikipedia.org/wiki/Nested_sampling_algorithm) algorithms that are
either written in Python, or have Python-wrapper implementations. The demostration is a simple toy
model of estimating the posteriors on the parameters of a straight line in Gaussian noise of known variance.

## Samplers

The MCMC samplers used are:
   
1. [emcee](http://dfm.io/emcee/current/)
2. [PyMC3](http://docs.pymc.io/)
3. [PyStan](http://pystan.readthedocs.io/en/latest/)
4. [PyJAGS](https://pyjags.readthedocs.io/en/latest/)

The nested sampling algorithms implementations uses are:

1. [Nestle](http://kylebarbary.com/nestle/)
2. [CPNest](https://johnveitch.github.io/cpnest/)
3. [PyMultiNest](https://johannesbuchner.github.io/PyMultiNest/)
4. [DNest4](https://github.com/eggplantbren/DNest4)
5. [PyPolyChord](https://ccpforge.cse.rl.ac.uk/gf/project/polychord/)

A page showing a demonstration and comparison of all the samplers on a fixed dataset can be found
[here](http://mattpitkin.github.io/samplers-demo/pages/samplers-samplers-everywhere/).

## Examples

Standalone examples for each sampler can be found at the links below:

* [emcee example](http://mattpitkin.github.io/samplers-demo/pages/emcee/)
* [PyMC3 example](http://mattpitkin.github.io/samplers-demo/pages/pymc3/)
* [PyStan example](http://mattpitkin.github.io/samplers-demo/pages/pystan/)
* [PyJAGS example](http://mattpitkin.github.io/samplers-demo/pages/pyjags/)
* [Nestle example](http://mattpitkin.github.io/samplers-demo/pages/nestle/)
* [CPNest example](http://mattpitkin.github.io/samplers-demo/pages/cpnest/)
* [PyMultiNest example](http://mattpitkin.github.io/samplers-demo/pages/pymultinest/)
* [DNest4 example](http://mattpitkin.github.io/samplers-demo/pages/dnest4/)
* [PyPolyChord example](http://mattpitkin.github.io/samplers-demo/pages/pypolychord/)

Information on [Docker](https://docs.docker.com/) images that can be used to run all
the samplers mentioned above can be found [here](http://mattpitkin.github.io/samplers-demo/pages/docker/).

## Acknowlegdments

The samplers mentioned above are obviously the work of a lot of people and I am very much indebted to
them for producing the software. Hopefully, this site will make it slightly easier for some more people to
get started using them. References for each of the packages can be found in the appropriate section of
the [demonstration page](http://mattpitkin.github.io/samplers-demo/pages/samplers-samplers-everywhere/).

This site is heavily based on the [_Pythonic Perambulations_](http://jakevdp.github.io/) blog by [Jake
VanderPlas](http://vanderplas.com/), and was created using [Pelican](http://docs.getpelican.com/en/stable/).
The source code for the site can be found on GitHub [here](https://github.com/mattpitkin/samplers-demo/),
and any problems/suggestions can be submitted as
[issues](https://github.com/mattpitkin/samplers-demo/issues) there, or left as comments on the various pages
here.

Also deserving thanks are: [Chris Pankow](https://github.com/cpankow) for spotting and fixing many typos and adding useful information to the
emcee section of the sampler demonstration page; and, [João Faria](https://github.com/j-faria) for spotting a problem with the DNest4 example
and suggesting a fix.

### The author

My name is [Matthew Pitkin](http://www.astro.gla.ac.uk/~matthew) and I'm an astrophysicist working on gravitational wave data analysis in
the [Institute for Gravitational Research](http://www.physics.gla.ac.uk/igr/) at the
[University of Glasgow](https://www.gla.ac.uk/).

