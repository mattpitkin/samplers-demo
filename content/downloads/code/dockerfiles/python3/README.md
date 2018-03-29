# Docker Image: Ubuntu 16.04, Python 3.5.2

This Dockerfile creates an image using Ubuntu 16.04 with Python 3.5.2.

It installs the following samplers:
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
 * edward

## Docker image

The Dockerfile has been built, and [uploaded](https://hub.docker.com/r/mattpitkin/samplers/tags/) to DockerHub, with (assuming MultiNest and PolyChord tarballs are in the directory):

```bash
docker login
docker build -t samplers:python3 .
docker tag samplers:python3 mattpitkin/samplers:python3
docker push mattpitkin/samplers:python3
```

## Examples

Assuming that you have downloaded this repository to the location `${HOME}/repositories/samplers-demo`, then the [examples](../../content/downloads/code) can be run with, e.g.:

```bash
docker run -it -v ${HOME}/repositories/samplers-demo/content/downloads/code:/work mattpitkin/samplers:python3
python test_emcee
```
