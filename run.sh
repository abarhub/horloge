#!/usr/bin/env bash

# to run in background :
# nohup ./run.sh >>custom-output.log 2>&1 &

set -e
source "./environnement/bin/activate"
flask --app server  run --host=0.0.0.0