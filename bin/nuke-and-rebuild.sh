#!/bin/bash

cd $(dirname $0)/..

docker-compose rm -f
docker-compose build

echo
echo "Running 'docker-compose up' should now fire up your AVA core dev instance"

