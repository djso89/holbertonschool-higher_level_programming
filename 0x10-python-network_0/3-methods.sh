#!/bin/bash
# a Bash script that takes in a URL and displays
curl -sI -X OPTIONS "$1" | grep 'Allow: ' | cut -f 1 -d " " --complement
