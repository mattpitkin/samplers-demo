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

> Note: PyPolyChord currently only compiles with Python 2 and not with Python 3. The setting of
> `ulimit -s unlimited` for the stack size is required to prevent Segmentation Faults with PolyChord.

> Note: DNest4 is not currently cloned from the [original repository](https://github.com/eggplantbren/DNest4/),
> but instead from a [repository](https://github.com/mattpitkin/DNest4) with a fix that allows it to be built with Python 2.

## Docker image

The Dockerfile has been built, and uploaded, with (assuming MultiNest and PolyChord tarballs are in the directory):

```bash
docker login
docker build -t samplers:python2 .
docker tag samplers:python2 mattpitkin/samplers:python2
docker push mattpitkin/samplers:python2
```

## Examples

Assuming that you have downloaded this repository in a location at `${HOME}/repositories/samplers-demo`, then the [examples](../../examples) can be run with, e.g.:

```bash
docker run -it -v ${HOME}/repositories/samplers-demo:/samplers mattpitkin/samplers_python2:latest
cd examples
python test_PyPolyChord
```



