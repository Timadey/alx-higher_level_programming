#!/bin/bash
# sends a json data to server
curl -s -d @"$2" "$1" -X POST -H "Content-Type: application/json"
