Title: An example using PyMC4
date: 2018-09-03 12:52
comments: true
slug: pymc4
tags: PyMC4,MCMC,TensorFlow Probability,Edward 2

<!-- PELICAN_BEGIN_SUMMARY -->
Here we show a standalone example of using [PyMC4](https://github.com/pymc-devs/pymc4) to
estimate the parameters of a straight line model in data with Gaussian noise. The
data and model used in this example are defined in `createdata.py`, which can be downloaded
from [here](http://mattpitkin.github.io/samplers-demo/downloads/code/createdata.py). The
script shown below can be downloaded from [here](http://mattpitkin.github.io/samplers-demo/downloads/code/test_pymc4.py).
<!-- PELICAN_END_SUMMARY -->

## Example code

{% include_code test_pymc4.py basedir:samplers-demo lang:python :hidefilename: %}

## Running the code

A description of installing PyMC4 is given [here](http://mattpitkin.github.io/samplers-demo/pages/samplers-samplers-everywhere/#PyMC4). If you have downloaded the [`createdata.py`](http://mattpitkin.github.io/samplers-demo/downloads/code/createdata.py) and [`test_pymc4.py`](http://mattpitkin.github.io/samplers-demo/downloads/code/test_pymc4.py) scripts into the directory `${HOME}`, then you can run it using:

```bash
python test_PyMC4.py
```

If you have [Matplotlib](https://matplotlib.org/) installed then the script will produce a plot of the posterior distributions
on the straight line parameters $m$ and $c$.

