FROM continuumio/miniconda3
LABEL name="samplers-demo miniconda3" \
maintainer="Matthew Pitkin <matthew.pitkin@ligo.org>" \
date="20200205"

RUN conda update -n base -c defaults conda

ENV conda_env python37

RUN conda create -n ${conda_env} python=3.7
RUN echo "source activate ${conda_env}" > ~/.bashrc
ENV PATH /opt/conda/envs/${conda_env}/bin:$PATH
RUN /bin/bash -c "source activate ${conda_env}"
RUN conda info
RUN python --version

# Install some requirements
RUN apt-get update
RUN apt-get install -y libblas3 libblas-dev liblapack3 liblapack-dev \
libatlas3-base libatlas-base-dev cmake build-essential gfortran git \
 git pkg-config libmpich-dev libopenmpi-dev dvipng r-base

# install light(ish) weight LaTeX
RUN apt-get install -y --no-install-recommends texlive texlive-latex-extra

# Install JAGS
RUN apt-get install -y jags

# clean things up
RUN apt-get -y autoremove \
    && apt-get -y clean

# Install conda-installable programs
RUN conda install -n ${conda_env} -y matplotlib numpy scipy pandas ipython

# Install pip-requirements
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools coverage-badge

# intall kernel for Jupyter notebooks
RUN pip install ipykernel

# Install some sampler dependencies
RUN pip install corner theano cython

# Install samplers
# Install PyJAGS from PyPI
RUN pip install --trusted-host pypi.python.org pyjags

# Install emcee
RUN pip install --trusted-host pypi.python.org emcee

# Install PyStan
RUN pip install --trusted-host pypi.python.org pystan

# Install YAPS
RUN pip install --trusted-host pypi.python.org yaps

# Install PyMC3
RUN pip install --trusted-host pypi.python.org pymc3

# Install Nestle
RUN pip install --trusted-host pypi.python.org nestle

# Install CPNest
RUN pip install --trusted-host pypi.python.org cpnest

# Install dynesty
RUN pip install --trusted-host pypi.python.org dynesty

# Install edward2 and TensorFlow Probability
RUN pip install tensorflow-probability edward2

# Install MultiNest
RUN git clone https://github.com/farhanferoz/MultiNest.git \
&& (cd MultiNest/MultiNest_v3.12_CMake/multinest && mkdir build && cd build && cmake .. && make)

ENV LD_LIBRARY_PATH $HOME/MultiNest/MultiNest_v3.12_CMake/multinest/lib:

# Install PyMultiNest
RUN pip install --trusted-host pypi.python.org pymultinest

# Install DNest4
RUN git clone https://github.com/eggplantbren/DNest4.git \
&& (cd DNest4 && python setup.py install)

# Add PolyChord
RUN git clone https://github.com/PolyChord/PolyChordLite.git \
&& (cd PolyChordLite && make pypolychord  MPI= && python setup.py install)

# Install Zeus
RUN pip install zeus-mcmc

# Install Sampyl
RUN pip install sampyl-mcmc

# Install PTMCMCSampler
RUN git clone https://github.com/jellis18/PTMCMCSampler.git \
&& (cd PTMCMCSampler && python setup.py install)

# Install ptemcee
RUN pip install ptemcee

# Install rpy2 (get slightly older version, see https://stackoverflow.com/q/61491298/1862861) and MCMC package
RUN wget https://cran.r-project.org/src/contrib/mcmc_0.9-7.tar.gz \
&& R CMD INSTALL mcmc_0.9-7.tar.gz
RUN pip install rpy2==3.2.0

# Install Pyro
RUN pip install torch
RUN pip install pyro-ppl

# Install PyMC4
RUN pip install git+https://github.com/pymc-devs/pymc4.git#egg=pymc4
