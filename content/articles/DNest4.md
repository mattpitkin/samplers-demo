Title: An example using DNest4
date: 2018-02-09 12:40
comments: true
slug: dnest4
tags: DNest4,nested sampling

<!-- PELICAN_BEGIN_SUMMARY -->
Here we show a standalone example of using [DNest4](https://github.com/eggplantbren/DNest4) to
estimate the parameters of a straight line model in data with Gaussian noise. The
data and model used in this example are defined in `createdata.py`, which can be downloaded
from [here](http://mattpitkin.github.io/samplers-demo/downloads/code/createdata.py). The
script shown below can be downloaded from [here](http://mattpitkin.github.io/samplers-demo/downloads/code/test_DNest4.py).
<!-- PELICAN_END_SUMMARY -->

## Example code

{% include_code test_DNest4.py basedir:samplers-demo lang:python :hidefilename: %}

## Running the code

A description of installing DNest4 is given [here](http://mattpitkin.github.io/samplers-demo/pages/samplers-samplers-everywhere/#DNest4). If you have downloaded the [`createdata.py`](http://mattpitkin.github.io/samplers-demo/downloads/code/createdata.py) and [`test_DNest4.py`](http://mattpitkin.github.io/samplers-demo/downloads/code/test_DNest4.py) scripts into the directory `${HOME}`, then you can run it using:

```bash
python test_DNest4.py
```

If you have [Matplotlib](https://matplotlib.org/) installed then the script will produce a plot of the posterior distributions
on the straight line parameters $m$ and $c$.

A Python 3 Docker image with DNest4 installed is
[available](https://hub.docker.com/r/mattpitkin/samplers/tags/), which can be used with:

```bash
docker run -it -v ${HOME}:/work mattpitkin/samplers:python3
```

to enter an interactive container, and then within the container the test script can be run with:

```bash
python test_DNest4.py
```