#!/bin/bash

cd $(dirname $0)/..

find . -name "000*" -exec rm {} \;
