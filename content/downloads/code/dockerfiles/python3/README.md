# Docker Image: Debian Buster, Python 3.7

This Dockerfile is based on
[`continuumio/miniconda3`](https://hub.docker.com/r/continuumio/miniconda3) and creates a
`python3.7` conda environment.

Within this environment it installs the following packages:

 * [bilby](https://lscsoft.docs.ligo.org/bilby/index.html)
 * [CPNest](https://johnveitch.github.io/cpnest/)
 * [DNest4](https://github.com/eggplantbren/DNest4)
 * [dynesty](https://dynesty.readthedocs.io/en/latest/)
 * [edward2](https://github.com/google/edward2)
 * [emcee](https://emcee.readthedocs.io/en/stable/)
 * [MC3](https://mc3.readthedocs.io/en/latest/index.html)
 * [Mici](https://matt-graham.github.io/mici/)
 * [Nestle](http://kylebarbary.com/nestle/)
 * [ptemcee](https://github.com/willvousden/ptemcee)
 * [PTMCMCSampler](http://jellis18.github.io/PTMCMCSampler/)
 * [PyJAGS](https://github.com/michaelnowotny/pyjags)
 * [PyMC3](https://docs.pymc.io/)
 * [PyMC4](https://github.com/pymc-devs/pymc4)
 * [PyMultiNest](https://johannesbuchner.github.io/PyMultiNest/)
 * [PyPolyChord](https://github.com/PolyChord/PolyChordLite)
 * [PySTAN](https://pystan.readthedocs.io/en/latest/)
 * [Pyro](http://docs.pyro.ai/en/stable/index.html)
 * [Sampyl](http://mcleonard.github.io/sampyl/)
 * [TensorFlow Probability](https://www.tensorflow.org/probability)
 * [UltraNest](https://johannesbuchner.github.io/UltraNest/index.html)
 * [YAPS](https://github.com/IBM/yaps)
 * [Zeus](https://github.com/minaskar/zeus)

## Docker image

The Dockerfile image is available at [Quay.io](https://quay.io/repository/mattpitkin/samplers-demo).

## Examples

Assuming that you have downloaded this repository to the location
`${HOME}/repositories/samplers-demo`, then the [examples](../../content/downloads/code) can be run
with, e.g.,:

```bash
docker run -it -v ${HOME}/repositories/samplers-demo/content/downloads/code:/samplers quay.io/mattpitkin/samplers-demo:latest
> cd samplers
> python test_emcee.py
```

You can run the sampler notebook by using:

```bash
sudo docker run -i -t -p 8888:8888 -v ${HOME}/repositories/samplers-demo/content/downloads/notebooks:/samplers quay.io/mattpitkin/samplers-demo:latest /bin/bash -c "jupyter notebook --notebook-dir=/samplers --ip='*' --port=8888 --no-browser --allow-root --MultiKernelManager.default_kernel_name=Samplers"
```

This will allow access to all the files within the `samplers-demo/content/downloads/notebooks` within a directory
within the container called `samplers`. To open the notebook, copy and paste the supplied URL into your web browser
and click on "`Samplers.ipynb`". You may then need to change the "Kernel" to "Samplers" by click the "Kernel" drop
down menu and selecting the "Samplers" option within "Change kernel".
