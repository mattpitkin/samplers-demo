# Docker Image: Debian Buster, Python 3.7

This Dockerfile is based on [`continuumio/miniconda3`](https://hub.docker.com/r/continuumio/miniconda3) and created a `python3.7` conda environment.

Within this environment it installs the following samplers:
 * emcee
 * PyMC3
 * PySTAN
 * PyJAGS
 * Nestle
 * CPNest
 * PyMultiNest
 * DNest4
 * PyPolyChord
 * UltraNest
 * TensorFlow Probability
 * dynesty
 * Pyro
 * PyMC4

## Docker image

The Dockerfile has been built, and [uploaded](https://hub.docker.com/r/mattpitkin/samplers/tags/) to DockerHub, with (assuming MultiNest and PolyChord tarballs are in the directory):

```bash
docker login
docker build -t samplers:python3 .
docker tag samplers:python3 mattpitkin/samplers:python3
docker push mattpitkin/samplers:python3
```

## Examples

Assuming that you have downloaded this repository to the location `${HOME}/repositories/samplers-demo`, then the [examples](../../content/downloads/code) can be run with, e.g.,:

```bash
docker run -it -v ${HOME}/repositories/samplers-demo/content/downloads/code:/samplers mattpitkin/samplers:python3
> cd samplers
> python test_emcee.py
```
