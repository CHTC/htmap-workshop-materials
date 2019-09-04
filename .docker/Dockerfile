# Copyright 2019 HTCondor Team, Computer Sciences Department,
# University of Wisconsin-Madison, WI.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# this dockerfile builds a test environment for HTMap

FROM ubuntu:bionic

# switch to root to do root-level config
USER root

# build config
ARG PYTHON_VERSION=3.7
ARG HTCONDOR_VERSION=8.9
ARG MINICONDA_VERSION=latest

# environment setup
ENV DEBIAN_FRONTEND=noninteractive \
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8

# faster container builds
RUN apt-get update \
 && apt-get -y install --no-install-recommends software-properties-common \
 && add-apt-repository ppa:apt-fast/stable \
 && apt-get update \
 && apt-get -y install apt-fast \
 && apt-get -y clean \
 && rm -rf /var/lib/apt/lists/*

# install utils and dependencies
RUN apt-fast update \
 && apt-fast -y install --no-install-recommends sudo vim less build-essential git gnupg wget ca-certificates locales man \
 && apt-get -y clean \
 && rm -rf /var/lib/apt/lists/* \
 && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \
 && locale-gen

# install HTCondor version specified in config
RUN wget -qO - https://research.cs.wisc.edu/htcondor/ubuntu/HTCondor-Release.gpg.key | apt-key add - \
 && echo "deb http://research.cs.wisc.edu/htcondor/ubuntu/${HTCONDOR_VERSION}/bionic bionic contrib" >> /etc/apt/sources.list \
 && apt-fast -y update \
 && apt-fast -y install --no-install-recommends htcondor \
 && apt-get -y clean \
 && rm -rf /var/lib/apt/lists/*

ENV CONDA_DIR=/opt/conda
ENV PATH=${CONDA_DIR}/bin:${PATH}

RUN cd /tmp \
 && wget --quiet https://repo.continuum.io/miniconda/Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh \
 && bash Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh -f -b -p $CONDA_DIR \
 && rm Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh \
 && conda install python=${PYTHON_VERSION} ipython numpy \
 && pip install --no-cache-dir htmap \
 && conda clean -y -all

ENV SUBMIT_USER=me
RUN groupadd ${SUBMIT_USER} \
 && useradd -m -g ${SUBMIT_USER} ${SUBMIT_USER}
USER ${SUBMIT_USER}
RUN echo 'export PS1="\u:\w \\$ \[$(tput sgr0)\]"' >> /home/${SUBMIT_USER}/.bashrc

COPY .docker/condor_config.local /etc/condor/condor_config.local
COPY .docker/.htmaprc /home/${SUBMIT_USER}/.htmaprc

COPY --chown=me:me .docker/entrypoint.sh /home/${SUBMIT_USER}/.entrypoint.sh
RUN chmod +x /home/${SUBMIT_USER}/.entrypoint.sh
ENTRYPOINT ["/home/me/.entrypoint.sh"]

WORKDIR /home/${SUBMIT_USER}/workshop
