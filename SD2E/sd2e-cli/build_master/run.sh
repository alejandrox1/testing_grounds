#!/usr/bin/env bash

CONTAINER="sd2e-cli-master"

docker build --no-cache --force-rm -t $CONTAINER . && \
    docker run --rm -it $CONTAINER
