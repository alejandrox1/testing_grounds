#    SD2E-CLI
#
# Install sd2e-cli from source. This image specification file allows you to
# specify what branch to build off of.
#
FROM ubuntu:18.04
MAINTAINER alejandrox1

ARG UID=1000
ARG USER=docker

RUN apt-get update -y && apt-get install -y git build-essential  && \
    apt-get install -y vim
    # Commenting these out in order to have the system updated - may need to
    # install something during an interactive run
    #rm -rf /var/lib/apt/lists/* && \
    #rm -rf /src/.*deb

RUN useradd -u $UID -ms /bin/bash $USER
USER $USER

WORKDIR /home/$USER
RUN git clone --recurse-submodules https://github.com/alejandrox1/sd2e-cli

ENV PATH /home/$USER/sd2e-cli/bin:$PATH

WORKDIR /home/$USER/sd2e-cli

CMD ["/bin/bash"]
