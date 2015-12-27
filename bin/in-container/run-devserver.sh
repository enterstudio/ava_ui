#!/bin/bash

## This script is used as the 'entry point' for the application
## server docker container. It runs 'migrate' on every start to
## ensure the database is built, and then executes the internal
## Django devserver.

## This is convenient for development, but it is *not* appropriate
## to run the Django devserver on a deployed or production systems.
## A TODO is to either configure this script to run in a non-debug
## "production" mode, or a separate script.

DIRECTORY=$(dirname $0)/../..
PYTHON=python
MANAGE=${DIRECTORY}/manage.py

## This one-off try-again is there because the postgres docker image
## takes a few extra seconds to initialize the database cluster on
## its first boot.
##
## It's not a loop because if it fails the second time there's probably
## something else going wrong.

${MANAGE} migrate --noinput
RESULT=$?
if [ ${RESULT} != 0 ]
then
    echo "Migrate failed, trying again in five seconds."
    sleep 5
    ${MANAGE} migrate --noinput
fi

${MANAGE} runserver 0.0.0.0:8888
