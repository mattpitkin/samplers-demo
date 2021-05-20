FROM quay.io/jitesoft/debian:buster-slim

LABEL name="samplers-demo miniconda3" \
maintainer="Matthew Pitkin <matthew.pitkin@ligo.org>" \
date="20200205"

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH

# copy stuff from continuumio docker file https://github.com/ContinuumIO/docker-images/blob/master/anaconda3/debian/Dockerfile
RUN apt-get update --fix-missing && \
    apt-get install -y --no-install-recommends wget bzip2 ca-certificates libglib2.0-0 libxext6 libsm6 libxrender1 git mercurial subversion && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    wget --quiet https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc && \
    find /opt/conda/ -follow -type f -name '*.a' -delete && \
    find /opt/conda/ -follow -type f -name '*.js.map' -delete && \
    /opt/conda/bin/conda clean -afy

CMD [ "/bin/bash" ]

RUN conda update -n base -c defaults conda

ENV conda_env python37

RUN conda create -n ${conda_env} python=3.7
RUN echo "source activate ${conda_env}" > ~/.bashrc
ENV PATH /opt/conda/envs/${conda_env}/bin:$PATH
RUN /bin/bash -c "source activate ${conda_env}"
RUN conda info
RUN python --version

# bug fix - see https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=932168
RUN sed -i "s#deb http://security.debian.org/debian-security stretch/updates main#deb http://deb.debian.org/debian-security stretch/updates main#g" /etc/apt/sources.list

# Install some requirements
RUN apt-get update
RUN apt-get install -y build-essential git dvipng r-base

# install light(ish) weight LaTeX
RUN apt-get install -y --no-install-recommends texlive texlive-latex-extra

# Install JAGS
RUN apt-get install -y jags

# clean things up
RUN apt-get -y autoremove \
    && apt-get -y clean

# Install conda-installable programs
RUN conda install -n ${conda_env} -y matplotlib numpy scipy pandas ipython cython

# Install corner
RUN conda install -n ${conda_env} -c conda-forge corner

# Install some conda-installable samplers
# Install ultranest
RUN conda install -n ${conda_env} -c conda-forge ultranest

# Install CPNest
RUN conda install -n ${conda_env} -c conda-forge cpnest

# Install dynesty
RUN conda install -n ${conda_env} -c conda-forge dynesty

# Install Nestle
RUN conda install -n ${conda_env} -c conda-forge nestle

# Install PyMultiNest
RUN conda install -n ${conda_env} -c conda-forge pymultinest

# Install DNest4
RUN conda install -n ${conda_env} -c conda-forge dnest4

# Install ptemcee
RUN conda install -n ${conda_env} -c conda-forge ptemcee

# Install PySTAN
RUN conda install -n ${conda_env} -c conda-forge pystan

# Install emcee
RUN conda install -n ${conda_env} -c conda-forge emcee">=3.0"

# Install bilby
RUN conda install -n ${conda_env} -c conda-forge bilby

# Install zeus
RUN conda install -n ${conda_env} -c conda-forge zeus-mcmc

# Install pip-requirements
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

# intall kernel for Jupyter notebooks
RUN pip install ipykernel

# Install samplers using pip

# Install PyMC3 (conda version is older)
RUN pip install --trusted-host pypi.python.org pymc3

# Install YAPS
RUN pip install --trusted-host pypi.python.org yaps

# Install edward2 and TensorFlow Probability
RUN pip install tensorflow-probability edward2

# Install Sampyl
RUN pip install sampyl-mcmc

# Install Mici
RUN pip install mici

# Install PTMCMCSampler
RUN git clone https://github.com/jellis18/PTMCMCSampler.git \
&& (cd PTMCMCSampler && python setup.py install)

# Install rpy2 (get slightly older version, see https://stackoverflow.com/q/61491298/1862861) and MCMC package
RUN wget https://cran.r-project.org/src/contrib/mcmc_0.9-7.tar.gz \
&& R CMD INSTALL mcmc_0.9-7.tar.gz
RUN pip install rpy2==3.2.0

# Install Pyro
RUN pip install torch
RUN pip install pyro-ppl

# Install PyMC4
RUN pip install git+https://github.com/pymc-devs/pymc4.git#egg=pymc4

# Install MC3
RUN pip install mc3

# Add PolyChord
RUN git clone https://github.com/PolyChord/PolyChordLite.git \
&& (cd PolyChordLite && python setup.py --no-mpi install)

# Install PyJAGS
RUN pip install --trusted-host pypi.python.org pyjags

# Install Jupyter
RUN conda install -n ${conda_env} jupyter -y --quiet

# create IPython kernel
RUN python -m ipykernel install --user --name ${conda_env} --display-name "Samplers"

# Install CPU info package
RUN pip install py-cpuinfo
