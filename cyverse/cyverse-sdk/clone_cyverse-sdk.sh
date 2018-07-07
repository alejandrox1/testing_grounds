#!/usr/bin/env bash

rm -rf cyverse-sdk

git clone https://github.com/alejandrox1/cyverse-sdk

( cd cyverse-sdk && git remote add upsream https://github.com/cyverse/cyverse-sdk )
