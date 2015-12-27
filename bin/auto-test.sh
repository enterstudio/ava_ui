#!/bin/bash

## The secret to test-driven development that actually works is
## to reduce the barriers of running the test-suite to zero.

## Running this script:
##
## - Sets up a docker container that listens for any file changes
##   in the ava/ directory.
## - Whenever a file changes, it runs the test suite.
## - Loop forever.
##
## Unfortunately, a quick google implies that this won't work
## effectively for boot2docker setups. We'll have to work out
## another solution to make that happen.

cd $(dirname $0)/..
docker-compose run web ./bin/in-container/auto-test.sh
