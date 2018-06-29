#!/usr/bin/env bash

CONTAINER="sd2e-cli-ci"

docker build --no-cache --force-rm -t $CONTAINER . && \
    docker run --rm -it $CONTAINER
