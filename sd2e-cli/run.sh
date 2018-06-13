#!/bin/bash
#-
#-                          :-) Testing sd2e-cli (-:
#-
#- Testing nvironment for the development of github.com/sd2e/sd2e-cli fork on
#- github.com/alejandrox1/sd2e-cli.
#-
##
## Usage:
##
##      ./run.sh [-v|-h] [-i|--input INPUT_FILE]
##
##      -v|--version print to stdout any information related to this script.
##
##      -h|--help print to stdout any help information included in the header
##                of the script.
##
##      -b|--branch clone the development branch. CUrrently, the development 
##                  branch in the github.com/alejandrox1/sd2e-cli is the 
##                  v1.0.7_alejandrox1 branch.
##
set -e
set -o pipefail
export blue="\e[1;34m"                                                         
export green="\e[32m"                                                           
export red="\e[1;31m"

# Input parameters
SD2E_BRANCH="master"
#SD2E_BRANCH="v1.0.7_alejandrox1"

# Parse command line arguments.
while [[ "$#" > 0 ]]; do
    arg="$1"

    case "${arg}" in
        -v|--version)
            echo "$(grep "^#-" ${BASH_SOURCE[0]} | cut -c 4-)"
            exit 0
            ;;
        -h|--help)
            echo "$(grep "^##" ${BASH_SOURCE[0]} | cut -c 4-)"
            exit 0
            ;;
        -b|--branch)
            SD2E_BRANCH="v1.0.7_alejandrox1"
        *)
            >&2 echo "Unknown command-line option: '${arg}'."
            exit 1
            ;;
    esac
    shift
done

echo -e "${red}Building with the ${SD2E_BRANCH} branch...${reset}"

docker build --no-cache --force-rm --build-arg BRANCH=${SD2E_BRANCH} -t sd2e-cli . && \
    docker run -it sd2e-cli
