#!/usr/bin/env bash

CONTAINER_TAG="alejandrox1/fastqc:0.11.5"

docker build -t ${CONTAINER_TAG} . && docker push ${CONTAINER_TAG}
