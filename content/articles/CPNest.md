Title: An example using CPNest
date: 2018-02-09 12:40
comments: true
slug: cpnest
tags: CPNest,nested sampling

<!-- PELICAN_BEGIN_SUMMARY -->
Here we show a standalone example of using [CPNest](https://johnveitch.github.io/cpnest/) to
estimate the parameters of a straight line model in data with Gaussian noise. The
data and model used in this example are defined in `createdata.py`, which can be downloaded
from [here](http://mattpitkin.github.io/samplers-demo/downloads/code/createdata.py). The
script shown below can be downloaded from [here](http://mattpitkin.github.io/samplers-demo/downloads/code/test_CPNest.py).
<!-- PELICAN_END_SUMMARY -->

## Example code

{% include_code test_CPNest.py basedir:samplers-demo lang:python :hidefilename: %}

## Running the code

A description of installing CPNest is given [here](http://mattpitkin.github.io/samplers-demo/pages/samplers-samplers-everywhere/#CPNest). If you have downloaded the [`createdata.py`](http://mattpitkin.github.io/samplers-demo/downloads/code/createdata.py) and [`test_CPNest.py`](http://mattpitkin.github.io/samplers-demo/downloads/code/test_CPNest.py) scripts into the directory `${HOME}`, then you can run it using:

```bash
python test_CPNest.py
```

If you have [Matplotlib](https://matplotlib.org/) installed then the script will produce a plot of the posterior distributions
on the straight line parameters $m$ and $c$.

A Python 3 Docker image with CPNest installed is
[available](https://hub.docker.com/r/mattpitkin/samplers/tags/), which can be used with:

```bash
docker run -it -v ${HOME}:/work mattpitkin/samplers:python3
```

to enter an interactive container, and then within the container the test script can be run with:

```bash
python test_CPNest.py
```