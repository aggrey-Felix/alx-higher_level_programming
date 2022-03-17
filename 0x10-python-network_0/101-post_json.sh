#!/bin/bash
#Script sends a JSON POST request to URL passed as argument and displays the body of the response
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
