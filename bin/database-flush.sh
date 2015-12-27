#!/bin/bash

## Flush all database tables.

## This doesn't drop and recreate tables, it just empties them and reloads
## any initial_data. It's fast for a data reset, but not useful for a structural
## change.

cd $(dirname $0)/..
./bin/manage.sh flush --noinput "$@"
