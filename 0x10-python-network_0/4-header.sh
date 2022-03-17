#!/bin/bash
#Script takes in URL as an argument, sends A GET request to the URL and Displays body of response
curl -sX GET -H "X-School-User-Id: 98" "$1"
