# Docker Image: Ubuntu 16.04, Python 2.7.12

This Dockerfile creates an image using Ubuntu 16.04 with Python 2.7.12.

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
 * Edward
 * dynesty

## Docker image

The Dockerfile has been built, and [uploaded](https://hub.docker.com/r/mattpitkin/samplers/tags/) to DockerHub, with (assuming MultiNest and PolyChord tarballs are in the directory):

```bash
docker login
docker build -t samplers:python2 .
docker tag samplers:python2 mattpitkin/samplers:python2
docker push mattpitkin/samplers:python2
```

## Examples

Assuming that you have downloaded this repository to the location `${HOME}/repositories/samplers-demo`, then the [examples](../../content/downloads/code) can be run with, e.g.:

```bash
docker run -it -v ${HOME}/repositories/samplers-demo/content/downloads/code:/work mattpitkin/samplers:python2
python test_PyPolyChord
```
