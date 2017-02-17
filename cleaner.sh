#!/bin/sh

a="$1"
cat $a | jq -n -f -r recover.jq | sort | cut -f 2 > $2
