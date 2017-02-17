#!/bin/sh
cat $1 | jq -n -f -r recover.jq | sort | cut -f 2 > $2
