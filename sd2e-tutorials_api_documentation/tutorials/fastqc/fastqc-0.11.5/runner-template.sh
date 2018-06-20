CONTAINER_IMAGE="index.docker.io/alejandrox1/fastqc:0.11.5"

. _util/container_exec.sh


COMMAND="fastqc"
PARAMS="${fastqc}" # $fastqc will be defined later by agave

container_exec ${CONTAINER_IMAGE} ${COMMAND} ${PARAMS}
