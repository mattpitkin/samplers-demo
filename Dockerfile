FROM jupyter/minimal-notebook
# Jupyter minimal notebook installs Ubuntu 16.04 with a jupyter notebook with a python3 kernel

WORKDIR /samplers

USER root

### Distribution package installs
RUN apt-get update

# install git and gfortran, pkg-config, BLAS, cmake, libmpich-dev
RUN apt-get install -y git gfortran pkg-config libblas-dev liblapack-dev libmpich-dev cmake libopenmpi-dev

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

# Install PyMC3
RUN pip install --trusted-host pypi.python.org pymc3

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
ENV LD_LIBRARY_PATH /usr/local/lib:/samplers/PolyChord/lib
ENV LD_PRELOAD /usr/lib/openmpi/lib/libmpi.so
ENV PYTHONPATH /samplers/PolyChord/PyPolyChord

# Install corner.py
RUN pip install --trusted-host pypi.python.org corner

# switch back to non-root user
USER $NB_USER

# add Python 2 kernel for Jupyter notebook (PyPolyChord needs Python 2 at the moment)
RUN conda create -y -n py27 python=2.7 && /bin/bash -c "source activate py27; conda install -y notebook ipykernel; pip install numpy; pip install scipy; pip install matplotlib; pip install corner; pip install emcee pymc3 pystan pyjags pymultinest nestle cpnest; ipython kernel install --user"

WORKDIR /notebooks
