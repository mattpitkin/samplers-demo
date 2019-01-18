FROM ubuntu:xenial
# installs Ubuntu 16.04

WORKDIR /samplers

### Distribution package installs
RUN apt-get update

# install git and gfortran, pkg-config, BLAS, cmake, libmpich-dev
RUN apt-get install -y git gfortran pkg-config libblas-dev liblapack-dev libmpich-dev cmake libopenmpi-dev dvipng python-tk

# install light(ish) weight LaTeX
RUN apt-get install -y --no-install-recommends texlive texlive-latex-extra

# install pip
RUN apt-get install -y python-pip

# Install JAGS
RUN apt-get install -y jags

# clean things up
RUN apt-get -y autoremove \
    && apt-get -y clean

### Python modules installed via conda and pip
RUN pip install --upgrade pip

# Install numpy, scipy, matplotlib and corner
RUN pip install --trusted-host pypi.python.org numpy scipy matplotlib corner

# Install IPython kernel
RUN pip install --trusted-host pypi.python.org ipykernel

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

# Install dynesty
RUN pip install --trusted-host pypi.python.org dynesty

# Install edward and TensorFlow
RUN pip install --trusted-host pypi.python.org tensorflow==1.5 edward

# Install MultiNest 
RUN cd /samplers && git clone https://github.com/farhanferoz/MultiNest.git
RUN cd /samplers/MultiNest/MultiNest_v3.11_CMake/multinest && mkdir build && cd build \
&& cmake .. && make && cd

# Install PyMultiNest
RUN pip install --trusted-host pypi.python.org pymultinest

# Install DNest4 (and clean up so that Python2 install can also proceed)
RUN cd /samplers && git clone https://github.com/eggplantbren/DNest4.git
RUN cd /samplers/DNest4/python && python setup.py install --prefix=/usr/local

# Add PolyChord
RUN cd /samplers && git clone https://github.com/PolyChord/PolyChordLite.git

# Install PyPolyChord (don't use the make file, use setup.py)
RUN cd /samplers/PolyChordLite && make pypolychord MPI= && python setup.py install

# Add getdist package for reading in PolyChord output
RUN pip install --trusted-host pypi.python.org getdist

# Install UltraNest
# first install metric-learn and progressbar-latest, which are required by UltraNest
RUN pip install --trusted-host pypi.python.org metric-learn progressbar-latest

RUN cd /samplers && git clone https://github.com/JohannesBuchner/UltraNest.git
RUN cd /samplers/UltraNest && python setup.py install --prefix=/usr/local
RUN cd /samplers/UltraNest/nested_sampling/clustering && make && cp *.so /usr/local/lib/python2.7/dist-packages/nested_sampling-*.egg/nested_sampling/clustering

# add global environment variables
ENV LD_LIBRARY_PATH /usr/local/lib:/samplers/PolyChordLite/lib:/samplers/UltraNest/nested_sampling/clustering:/samplers/MultiNest/MultiNest_v3.11_CMake/multinest/lib
ENV PYTHONPATH /usr/local/lib/python2.7/dist-packages/nested_sampling

# change to new working directory
WORKDIR /work

