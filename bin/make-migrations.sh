#!/bin/bash

## Run 'manage.py makemigrations' on all AVA apps to auto-detect
## database changes.
##
## Uses list-ava-apps.sh to find the apps names.


## I don't like having to hardwire this list.
## AVA_APPS="core_auth core_group core_identity core core_project import_ldap import_google test_email test test_twitter"


cd $(dirname $0)/..

./bin/manage.sh makemigrations
./bin/manage.sh migrate
