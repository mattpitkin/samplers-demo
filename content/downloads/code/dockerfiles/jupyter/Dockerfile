FROM jupyter/minimal-notebook
# Jupyter minimal notebook installs Ubuntu 16.04 with a jupyter notebook with a python3 kernel

WORKDIR /samplers

USER root

### Distribution package installs
RUN apt-get update

# install git and gfortran, pkg-config, BLAS, cmake, libmpich-dev
RUN apt-get install -y git gfortran pkg-config libblas-dev liblapack-dev libmpich-dev cmake libopenmpi-dev scons dvipng

# Install JAGS
RUN apt-get install -y jags

# clean things up
RUN apt-get -y autoremove \
    && apt-get -y clean

### Python modules installed via conda and pip

# Install numpy, scipy
USER $NB_USER
RUN conda install -y numpy
RUN conda install -y scipy
RUN conda install -y mkl-service
USER root

# Install matplotlib, corner and cpuinfo
RUN pip install --trusted-host pypi.python.org matplotlib corner py-cpuinfo

# Install samplers
# Install PyJAGS from PyPI
RUN pip install --trusted-host pypi.python.org pyjags

# Install emcee
RUN pip install --upgrade --trusted-host pypi.python.org emcee --pre

# Install PyStan
RUN pip install --trusted-host pypi.python.org pystan

# Install PyMC3
RUN pip install --trusted-host pypi.python.org pymc3

# Install Nestle
RUN pip install --trusted-host pypi.python.org nestle

# Install CPNest
RUN pip install --trusted-host pypi.python.org cpnest

# Install dynesty
RUN pip install --trusted-host pypi.python.org dynesty

# Install edward and TensorFlow (v1.5 as later version break Edward v1.3.5)
RUN pip install --trusted-host pypi.python.org tensorflow==1.5 edward

# Install MultiNest
RUN cd ${HOME} && git clone https://github.com/farhanferoz/MultiNest.git
RUN cd ${HOME}/MultiNest/MultiNest_v3.11_CMake/multinest && mkdir build && cd build \
&& cmake .. && make && cd

# Install PyMultiNest
RUN pip install --trusted-host pypi.python.org pymultinest

ENV LD_LIBRARY_PATH /usr/local/lib

# Install DNest4 (and clean up so that Python2 install can also proceed)
RUN cd ${HOME} && git clone https://github.com/eggplantbren/DNest4.git
RUN chown -R $NB_USER ${HOME}/DNest4
RUN cd ${HOME}/DNest4/python && python setup.py install --prefix=/opt/conda \
    && rm -rf build && rm -rf dist && rm -rf dnest4.egg-info && rm dnest4/_dnest4.cpp

# set working directory as "/home/jovyan/work"
WORKDIR ${HOME}/work

# Add PolyChord
RUN cd ${HOME} && git clone https://github.com/PolyChord/PolyChordLite.git

# Install PyPolyChord (don't use the make file, use setup.py)
RUN cd ${HOME}/PolyChordLite && make pypolychord MPI= && python setup.py install && chmod -R a+rw ${HOME}/PolyChordLite

# Install getdist for PolyChord post-processing
RUN pip install --trusted-host pypi.python.org getdist

# Install UltraNest
# first install metric-learn and progressbar-latest, which are required by UltraNest
RUN pip install --trusted-host pypi.python.org metric-learn progressbar-latest

RUN cd ${HOME} && git clone https://github.com/JohannesBuchner/UltraNest.git
RUN chown -R $NB_USER ${HOME}/UltraNest
RUN cd ${HOME}/UltraNest && python setup.py install --prefix=/opt/conda
RUN cd ${HOME}/UltraNest/nested_sampling/clustering && make && cp *.so /opt/conda/lib/python3.6/site-packages/nested_sampling-*.egg/nested_sampling/clustering

# add global environment variables
RUN echo "LD_LIBRARY_PATH=/usr/local/lib:${HOME}/PolyChordLite/lib:${HOME}/MultiNest/MultiNest_v3.11_CMake/multinest/lib" >> /etc/environment

# switch back to non-root user
USER $NB_USER
