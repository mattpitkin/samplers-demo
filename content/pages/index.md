title: Samplers demo
slug: index
Template: index

This site aims gives a demonstration of [thirteen different](#Samplers) [MCMC](https://en.wikipedia.org/wiki/Markov_chain_Monte_Carlo)
and [nested sampling](https://en.wikipedia.org/wiki/Nested_sampling_algorithm) algorithms that are
either written in Python, or have Python-wrapper implementations. The demonstration is a simple toy
model of estimating the posteriors on the parameters of a straight line in Gaussian noise of known variance.

## Samplers

The MCMC samplers used are:
   
1. [emcee](http://dfm.io/emcee/current/)
2. [TensorFlow Probability](https://www.tensorflow.org/probability/)
3. [PyMC4](https://github.com/pymc-devs/pymc4/)
4. [Zeus](https://zeus-mcmc.readthedocs.io/en/latest/index.html)
5. [PyStan](http://pystan.readthedocs.io/en/latest/)
6. [PyJAGS](https://pyjags.readthedocs.io/en/latest/)

The nested sampling algorithms implementations uses are:

1. [Nestle](http://kylebarbary.com/nestle/)
2. [CPNest](https://johnveitch.github.io/cpnest/)
3. [dynesty](https://dynesty.readthedocs.io)
4. [UltraNest](https://github.com/JohannesBuchner/UltraNest)
5. [PyMultiNest](https://johannesbuchner.github.io/PyMultiNest/)
6. [DNest4](https://github.com/eggplantbren/DNest4)
7. [PyPolyChord](https://ccpforge.cse.rl.ac.uk/gf/project/polychord/)

A page showing a demonstration and comparison of all the samplers on a fixed data set can be found
[here](http://mattpitkin.github.io/samplers-demo/pages/samplers-samplers-everywhere/).

## Examples

Standalone examples for each sampler can be found at the links below:

* [emcee example](http://mattpitkin.github.io/samplers-demo/pages/emcee/)
* [PyMC3 example](http://mattpitkin.github.io/samplers-demo/pages/pymc3/)
* [Zeus example](http://mattpitkin.github.io/samplers-demo/pages/zeus/)
* [PyStan example](http://mattpitkin.github.io/samplers-demo/pages/pystan/)
* [PyJAGS example](http://mattpitkin.github.io/samplers-demo/pages/pyjags/)
* [TensorFlow Probability example](http://mattpitkin.github.io/samplers-demo/pages/tensorflow-probability/)
* [Nestle example](http://mattpitkin.github.io/samplers-demo/pages/nestle/)
* [CPNest example](http://mattpitkin.github.io/samplers-demo/pages/cpnest/)
* [dynesty example](http://mattpitkin.github.io/samplers-demo/pages/dynesty/)
* [UltraNest example](http://mattpitkin.github.io/samplers-demo/pages/ultranest/)
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
[emcee section](http://mattpitkin.github.io/samplers-demo/pages/samplers-samplers-everywhere/#emcee) of the sampler demonstration page; [João Faria](https://github.com/j-faria) for spotting a problem with the DNest4 example
and suggesting a fix; and, [Johannes Buchner](https://github.com/JohannesBuchner) for useful information about effective sample sizes.

### The author

My name is [Matthew Pitkin](https://ma.ttpitk.in) and I'm an astrophysicist working on gravitational-wave data analysis in
the [Department of Physics](https://www.lancaster.ac.uk/physics/) at the
[Lancaster University](https://www.lancaster.ac.uk).
