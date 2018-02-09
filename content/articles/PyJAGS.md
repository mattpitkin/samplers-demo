Title: An example using PyJAGS
date: 2018-02-09 12:40
comments: true
slug: pyjags
tags: PyJAGS,MCMC

<!-- PELICAN_BEGIN_SUMMARY -->
Here we show a standalone example of using [PyJAGS](https://pyjags.readthedocs.io/) to
estimate the parameters of a straight line model in data with Gaussian noise. The
data and model used in this example are defined in `createdata.py`, which can be downloaded
from [here](http://mattpitkin.github.io/samplers-demo/downloads/code/createdata.py). The
script shown below can be downloaded from [here](http://mattpitkin.github.io/samplers-demo/downloads/code/test_PyJAGS.py).
<!-- PELICAN_END_SUMMARY -->

## Example code

{% include_code test_PyJAGS.py basedir:samplers-demo lang:python :hidefilename: %}

## Running the code

A description of installing PyJAGS is given [here](http://mattpitkin.github.io/samplers-demo/pages/samplers-samplers-everywhere/#PyJAGS). If you have downloaded the [`createdata.py`](http://mattpitkin.github.io/samplers-demo/downloads/code/createdata.py) and [`test_PyJAGS.py`](http://mattpitkin.github.io/samplers-demo/downloads/code/test_PyJAGS.py) scripts into the directory `${HOME}`, then you can run it using:

```bash
python test_PyJAGS.py
```

If you have [Matplotlib](https://matplotlib.org/) installed then the script will produce a plot of the posterior distributions
on the straight line parameters $m$ and $c$.

Python 2 and 3 Docker images with emcee installed are [available](https://hub.docker.com/r/mattpitkin/samplers/tags/), and to run with, e.g., the Python 2 container, you can do:

```bash
docker run -it -v ${HOME}:/work mattpitkin/samplers:python2
```

to enter an interactive container, and then within the contain run:

```bash
python test_PyJAGS.py
```

