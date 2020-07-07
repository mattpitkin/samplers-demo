Title: An example using dynesty
date: 2018-08-10 10:03
comments: true
slug: dynesty
tags: dynesty,nested sampling

<!-- PELICAN_BEGIN_SUMMARY -->
Here we show a standalone example of using [dynesty](https://dynesty.readthedocs.io) to
estimate the parameters of a straight line model in data with Gaussian noise. The
data and model used in this example are defined in `createdata.py`, which can be downloaded
from [here](http://mattpitkin.github.io/samplers-demo/downloads/code/createdata.py). The
script shown below can be downloaded from [here](http://mattpitkin.github.io/samplers-demo/downloads/code/test_Nestle.py).
<!-- PELICAN_END_SUMMARY -->

The example code below shows how to run dynesty with both the
[**dynamic**](https://dynesty.readthedocs.io/en/latest/dynamic.html#dynamic-nested-sampling)
and [**static**](https://dynesty.readthedocs.io/en/latest/dynamic.html#static-nested-sampling) samplers.

## Example code

{% include_code test_dynesty.py basedir:samplers-demo lang:python :hidefilename: %}

## Running the code

A description of installing dynesty is given [here](http://mattpitkin.github.io/samplers-demo/pages/samplers-samplers-everywhere/#dynesty). If you have downloaded the [`createdata.py`](http://mattpitkin.github.io/samplers-demo/downloads/code/createdata.py) and [`test_dynesty.py`](http://mattpitkin.github.io/samplers-demo/downloads/code/test_dynesty.py) scripts into the directory `${HOME}`, then you can run it using:

```bash
python test_dynesty.py
```

If you have [Matplotlib](https://matplotlib.org/) installed then the script will produce a plot of the posterior distributions
on the straight line parameters $m$ and $c$.

A Python 3 Docker image with dynesty installed is
[available](https://hub.docker.com/r/mattpitkin/samplers/tags/), which can be used with:

```bash
docker run -it -v ${HOME}:/work mattpitkin/samplers:python3
```

to enter an interactive container, and then within the container the test script can be run with:

```bash
python test_dynesty.py
```