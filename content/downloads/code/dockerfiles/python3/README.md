# Docker Image: Debian Buster, Python 3.7

This Dockerfile is based on
[`continuumio/miniconda3`](https://hub.docker.com/r/continuumio/miniconda3) and created a
`python3.7` conda environment.

Within this environment it installs the following packages:

 * [bilby](https://lscsoft.docs.ligo.org/bilby/index.html)
 * [CPNest](https://johnveitch.github.io/cpnest/)
 * [DNest4](https://github.com/eggplantbren/DNest4)
 * [dynesty](https://dynesty.readthedocs.io/en/latest/)
 * [edward2](https://github.com/google/edward2)
 * [emcee](https://emcee.readthedocs.io/en/stable/)
 * [Mici](https://matt-graham.github.io/mici/)
 * [Nestle](http://kylebarbary.com/nestle/)
 * [ptemcee](https://github.com/willvousden/ptemcee)
 * [PTMCMCSampler](http://jellis18.github.io/PTMCMCSampler/)
 * [PyJAGS](https://github.com/michaelnowotny/pyjags)
 * PyMC3
 * PyMC4
 * PyMultiNest
 * PyPolyChord
 * PySTAN
 * Pyro
 * Sampyl
 * TensorFlow Probability
 * UltraNest
 * YAPS
 * Zeus

## Docker image

The Dockerfile has been built, and [uploaded](https://hub.docker.com/r/mattpitkin/samplers/tags/) to
DockerHub with:

```bash
docker login
docker build -t samplers:python3 .
docker tag samplers:python3 mattpitkin/samplers:python3
docker push mattpitkin/samplers:python3
```

## Examples

Assuming that you have downloaded this repository to the location
`${HOME}/repositories/samplers-demo`, then the [examples](../../content/downloads/code) can be run
with, e.g.,:

```bash
docker run -it -v ${HOME}/repositories/samplers-demo/content/downloads/code:/samplers mattpitkin/samplers:python3
> cd samplers
> python test_emcee.py
```
