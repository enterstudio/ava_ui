#!/bin/bash

set -e

## Use docker-compose to run the AVA test suite.

# cd $(dirname $0)/..

./bin/manage.sh test -v2
