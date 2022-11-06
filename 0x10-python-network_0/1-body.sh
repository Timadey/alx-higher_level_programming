#!/bin/bash
# senda a GET request and display the response

status=$(curl "$1" -s -o /dev/null -w %{http_code});
if [ "$status" -eq "200" ]
then curl -Ls "$1";
fi


