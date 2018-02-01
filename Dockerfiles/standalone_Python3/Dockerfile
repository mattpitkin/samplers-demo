FROM ubuntu:xenial
# installs Ubuntu 16.04

WORKDIR /samplers

### Distribution package installs
RUN apt-get update

# install git and gfortran, pkg-config, BLAS, cmake, libmpich-dev
RUN apt-get install -y git gfortran pkg-config libblas-dev liblapack-dev libmpich-dev cmake libopenmpi-dev dvipng

# install light(ish) weight LaTeX
RUN apt-get install -y --no-install-recommends texlive texlive-latex-extra

# install pip
RUN apt-get install -y python3 python3-dev python3-pip python3-tk

# Install JAGS
RUN apt-get install -y jags

# clean things up
RUN apt-get -y autoremove \
    && apt-get -y clean

### Python modules installed via conda and pip
RUN pip3 install --upgrade pip

# Install numpy, scipy, matplotlib and corner
RUN pip3 install --trusted-host pypi.python.org numpy scipy matplotlib corner

# Install samplers
# Install PyJAGS from PyPI
RUN pip3 install --trusted-host pypi.python.org pyjags

# Install emcee
RUN pip3 install --trusted-host pypi.python.org emcee

# Install PyStan
RUN pip3 install --trusted-host pypi.python.org pystan

# Install PyMC3
RUN pip3 install --trusted-host pypi.python.org pymc3

# Install Nestle
RUN pip3 install --trusted-host pypi.python.org nestle

# Install CPNest
RUN pip3 install --trusted-host pypi.python.org cpnest

# Install MultiNest 
ADD MultiNest_v3.10_CMake.tar.gz /samplers
RUN cd MultiNest_v3.10_CMake/multinest/build \
    && cmake .. && make && make install && cd

# Install PyMultiNest
RUN pip3 install --trusted-host pypi.python.org pymultinest

# Install DNest4 (and clean up so that Python2 install can also proceed)
RUN cd /samplers && git clone https://github.com/mattpitkin/DNest4.git
RUN cd /samplers/DNest4/python && python3 setup.py install --prefix=/usr/local

# Add PolyChord
ADD PolyChord_v1.12.tar.gz /samplers

# Install PyPolyChord (don't use the make file, use setup.py)
RUN cd /samplers/PolyChord && make MPI= && python3 setup.py install

# add global environment variables
ENV LD_LIBRARY_PATH /usr/local/lib

# update alternatives to python3 (generally not what you should do, but it shouldn't be a problem in this container)
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 10
RUN update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 10

