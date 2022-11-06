#!/bin/bash
# show list of methods allowed on the server

curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-