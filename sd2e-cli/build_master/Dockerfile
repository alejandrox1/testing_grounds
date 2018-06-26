FROM ubuntu:18.04
MAINTAINER alejandrox1

ARG RELEASE=https://raw.githubusercontent.com/sd2e/sd2e-cli/master/sd2e-cloud-cli.tgz
ARG INSTALL_SCRIPT=https://raw.githubusercontent.com/sd2e/sd2e-cli/master/install/install.sh

RUN apt-get update -y && apt-get install -y curl  && \
    apt-get install -y vim
    # Commenting these out in order to have the system updated - may need to
    # install something during an interactive run
    #rm -rf /var/lib/apt/lists/* && \
    #rm -rf /src/.*deb

RUN useradd -ms /bin/bash docker                                                
USER docker

WORKDIR /home/docker
RUN curl -L ${INSTALL_SCRIPT} | sh


CMD ["/bin/bash"]
