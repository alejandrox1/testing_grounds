FROM ubuntu:18.04
MAINTAINER alejandrox1

ARG BRANCH=master

RUN apt-get update -y && apt-get install -y git build-essential  && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /src/.*deb

WORKDIR /work
RUN git clone -b ${BRANCH} https://github.com/alejandrox1/sd2e-cli
WORKDIR sd2e-cli

CMD ["/bin/bash"]
