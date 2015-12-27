#!/bin/bash

## Run the 'flake8' code quality/style-guide checking tool
## over the AVA codebase.

## This script can be run on its own (although you will have to
## 'pip install flake8' first) or it is run as part of the unit
## test suite.

## When run in the context of the unit test suite it's done
## inside the docker container, where flake8 is already installed.

## PEP8 Violations we globally allow:
##
## E501: Line length, 79 is too short.
## E265: Tom's habit of using ## for block comments is very
##       hard to break.

FLAKE8_ARGUMENTS="--ignore=E501,E265"

cd $(dirname $0)/../

find core -type f -name '*.py' -not -path '*/migrations/*' | xargs flake8 ${FLAKE8_ARGUMENTS}
