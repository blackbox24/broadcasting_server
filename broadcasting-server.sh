#!/bin/bash

set -e

command=$1

if [[ $command == "start" ]]; then
    echo $(python ./server.py);
elif [[ $command == "connect" ]]; then 
    echo $(python ./main.py);
else 
    echo "$command not found";
fi