#!/bin/bash
# send post data to server

curl -d email=test@gmail.com -d subject='I will always be here for PLD' "$1";