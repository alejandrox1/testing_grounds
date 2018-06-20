#!/usr/bin/env bash

CONTAINER_IMAGE="index.docker.io/alejandrox1/fastqc:0.11.5"

fastqc_sample_input="/example/SP1.fq"
container_mount="-v ${PWD}/../example:/example:rw"


. _util/container_exec.sh

COMMAND="fastqc"
PARAMS="${fastqc_sample_input}"

DEBUG=1 container_exec ${container_mount} ${CONTAINER_IMAGE} ${COMMAND} ${PARAMS}

######################
#  FUNCTIONAL TESTS  #
#                    #
# Dont include in    #
# runner-template.sh #
######################


function cleanup() {

    rm -f .container_exec.*

}

function validate_output() {

    return 0

}

function run_tests() {

    validate_output
    return 0
}

run_tests && \
    echo "Success" && \
    cleanup

