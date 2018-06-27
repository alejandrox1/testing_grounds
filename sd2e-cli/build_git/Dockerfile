#    SD2E-CLI
#
# Install sd2e-cli from source. This image specification file allows you to
# specify what branch to build off of.
#
FROM ubuntu:18.04
MAINTAINER alejandrox1

RUN apt-get update -y && apt-get install -y git build-essential  && \
    apt-get install -y vim
    # Commenting these out in order to have the system updated - may need to
    # install something during an interactive run
    #rm -rf /var/lib/apt/lists/* && \
    #rm -rf /src/.*deb

RUN useradd -ms /bin/bash docker
USER docker

WORKDIR /home/docker
RUN git clone --recurse-submodules https://github.com/alejandrox1/sd2e-cli

ENV PATH /home/docker/sd2e-cli/bin:$PATH

CMD ["/bin/bash"]
