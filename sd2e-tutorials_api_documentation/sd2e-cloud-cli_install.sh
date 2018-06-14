#!/bin/bash

curl -L https://raw.githubusercontent.com/sd2e/sd2e-cli/master/sd2e-cloud-cli.tgz \
    -o sd2e-cloud-cli.tgz && \
       tar -xvzf sd2e-cloud-cli.tgz

echo "export PATH=$PWD/sd2e-cloud-cli/bin:$PATH" >> ~/.bashrc
