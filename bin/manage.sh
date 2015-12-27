#!/bin/bash

## A wrapper to call 'manage.py' within the docker container.

cd $(dirname $0)/..

docker-compose run --rm ui ./manage.py "$@"
