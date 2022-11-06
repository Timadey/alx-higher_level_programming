#!/bin/bash
# send request to a url and display the size of the response body
curl "$1" -i -s -o /dev/null -w %{size_download};
