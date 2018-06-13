#!/bin/bash

docker build --force-rm -t sd2e-cli . && \
    docker run -it sd2e-cli
