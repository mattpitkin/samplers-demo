# Docker Image: `minimal-notebook`

This Dockerfile creates an image using the [`minimal-notebook` image](https://github.com/jupyter/docker-stacks/tree/master/minimal-notebook),
which runs Ubuntu 16.04 and provides a Jupyter notebook that can access the various samplers.

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

The container can create notebooks using either a Python 2 or Python 3 kernel.

> Note: DNest4 is not currently
> cloned from the [original repository](https://github.com/eggplantbren/DNest4/),
> but instead from a [repository](https://github.com/mattpitkin/DNest4) with a fix that allows it to be built with Python 2.

## Docker image

The Dockerfile has been built, and [uploaded](https://hub.docker.com/r/mattpitkin/samplers/tags/) to DockerHub, with (assuming MultiNest and PolyChord tarballs are in the directory):

```bash
docker login
docker build -t samplers:jupyter .
docker tag samplers:jupyter mattpitkin/samplers:jupyter
docker push mattpitkin/samplers:jupyter
```

## Examples

Assuming that you have downloaded this repository to the location `${HOME}/repositories/samplers-demo`, then [Samplers.ipynb](../../Samplers.ipynb) can be run with:

```bash
docker run -it -v ${HOME}/repositories/samplers-demo:/home/jovyan/work -e NB_UID=1001 --user root --rm -p 8888:8888 mattpitkin/samplers:jupyter
```

then pasting the supplied link into your browser, and selecting the `Samplers.ipynb` file.

