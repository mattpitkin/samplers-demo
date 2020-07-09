Title: An example using TensorFlow Probability
date: 2018-09-03 12:47
comments: true
slug: tensorflow-probability
tags: TensorFlow,TensorFlow Probability,MCMC

<!-- PELICAN_BEGIN_SUMMARY -->
Here we show a standalone example of using [TensorFlow Probability](https://www.tensorflow.org/probability/) to
estimate the parameters of a straight line model in data with Gaussian noise. The
data and model used in this example are defined in `createdata.py`, which can be downloaded
from [here](http://mattpitkin.github.io/samplers-demo/downloads/code/createdata.py). The
script shown below can be downloaded from [here](http://mattpitkin.github.io/samplers-demo/downloads/code/test_TFP.py).
<!-- PELICAN_END_SUMMARY -->

## Example code

{% include_code test_TFP.py basedir:samplers-demo lang:python :hidefilename: %}

## Running the code

If you have downloaded the [`createdata.py`](http://mattpitkin.github.io/samplers-demo/downloads/code/createdata.py) and [`test_tensorflow_probability.py`](http://mattpitkin.github.io/samplers-demo/downloads/code/test_tensorflow_probability.py) scripts into the directory `${HOME}`, and [installed](https://github.com/tensorflow/probability#installation) TensorFlow Probability, then you can run it using:

```bash
python test_TFP.py
```

If you have [Matplotlib](https://matplotlib.org/) installed then the script will produce a plot of the posterior distributions
on the straight line parameters $m$ and $c$.

