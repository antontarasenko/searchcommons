#!/usr/bin/env bash

set -e

curl 'https://s3.amazonaws.com/alexa-static/top-1m.csv.zip' > 'top-1m.csv.zip'
unzip 'top-1m.csv.zip'
awk 'BEGIN { FS=","; } ; { printf "*.%s/*\n", $2; }' top-1m.csv | head -n 1000 > 'exclude.txt'
