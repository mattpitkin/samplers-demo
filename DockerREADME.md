# Setting up a Docker container for running the notebook

A Docker image [exists](https://hub.docker.com/r/mattpitkin/samplers/) for running this notebook. This is created from
[this](Dockerfile) Dockerfile, which using the [jupyter/minimal-notebook](https://github.com/jupyter/docker-stacks/tree/master/minimal-notebook) image, and contains:

```
FROM jupyter/minimal-notebook
# Jupyter minimal notebook installs Ubuntu 16.04 with a jupyter notebook with a python3 kernel

WORKDIR /samplers

USER root

### Distribution package installs
RUN apt-get update

# install git and gfortran, pkg-config, BLAS, cmake, libmpich-dev
RUN apt-get install -y git gfortran pkg-config libblas-dev liblapack-dev libmpich-dev cmake

# Install JAGS
RUN apt-get install -y jags

# clean things up
RUN apt-get -y autoremove \
    && apt-get -y clean

### Python modules installed via pip

# Install numpy, scipy, matplotlib
RUN pip install --trusted-host pypi.python.org numpy scipy matplotlib

# Install samplers
# Install PyJAGS from PyPI
RUN pip install --trusted-host pypi.python.org pyjags

# Install emcee
RUN pip install --trusted-host pypi.python.org emcee

# Install PyStan
RUN pip install --trusted-host pypi.python.org pystan

# Install Nestle
RUN pip install --trusted-host pypi.python.org nestle

# Install CPNest
RUN pip install --trusted-host pypi.python.org cpnest

# Install MultiNest 
ADD MultiNest_v3.10_CMake.tar.gz /samplers
RUN cd MultiNest_v3.10_CMake/multinest/build \
    && cmake .. && make && make install && cd

# Install PyMultiNest
RUN pip install --trusted-host pypi.python.org pymultinest

# Install PolyChord
ADD PolyChord_v1.9.tar.gz /samplers
RUN cd PolyChord && make PyPolyChord
RUN export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/samplers/PolyChord/lib \
    && export LD_PRELOAD=/usr/lib/openmpi/lib/libmpi.so:$LD_PRELOAD \
    && export PYTHONPATH=${PYTHONPATH}:/samplers/PolyChord/PyPolyChord

# Install corner.py
RUN pip install --trusted-host pypi.python.org corner

# switch back to non-root user
USER $NB_USER

# set working directory
WORKDIR /notebooks
```

This was built with:

```bash
docker build -t samplers .
```

and pushed to Docker Hub with:

```bash
docker login
docker tag samplers mattpitkin/samplers
docker push mattpitkin/samplers
```

## Run Jupyter notebook

To run a Jupyter notebook from this image first create a local directory that will contain notebooks that can be
read/written from the Docker container, e.g.:

```bash
mkdir ${HOME}/notebooks
```

Set the [ownership of the directory](https://github.com/jupyter/docker-stacks/tree/master/minimal-notebook#docker-options)
so that the notebook can write to that directory, e.g.:

```
sudo chown ${HOME}/notebooks
```

Now run the Docker image:

```bash
docker run -it -v ${HOME}/notebooks:/notebooks -e NB_UID=1000 --rm -p 8888:8888 mattpitkin/samplers:latest
```
