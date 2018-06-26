FROM ubuntu:18.04
MAINTAINER alejandrox1

ARG RELEASE=https://github.com/SD2E/sd2e-cli/raw/ci/sd2e-cloud-cli.tgz

RUN apt-get update -y && apt-get install -y curl && \
    apt-get install -y vim
    # Commenting these out in order to have the system updated - may need to
    # install something during an interactive run
    #rm -rf /var/lib/apt/lists/* && \
    #rm -rf /src/.*deb

RUN useradd -ms /bin/bash docker
USER docker

WORKDIR /home/docker
RUN curl -L ${RELEASE} -o sd2e-cloud-cli.tgz && \
    tar xzvf sd2e-cloud-cli.tgz && \
    rm sd2e-cloud-cli.tgz

ENV PATH /home/docker/sd2e-cloud-cli/bin:$PATH

CMD ["/bin/bash"]
