#!/bin/bash

cd $(dirname $0)/..

apps="learn my game organize gather_ldap gather_google"
exclude="TimeStampedModel"

./bin/manage.sh graph_models $apps -X $exclude -E -g > ava.dot
