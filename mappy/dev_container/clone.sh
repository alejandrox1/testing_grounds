#!/usr/bin/env bash
set -x

git clone https://gitlab.com/alejandrox1/mappy || true

cd mappy && git remote add upstream https://gitlab.com/sd2e/mappy
