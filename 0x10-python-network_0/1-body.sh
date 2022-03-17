#!/bin/bash
# Script takes in url,sends GET request to the URL and display response body
curl -sfL "$1" -X GET
