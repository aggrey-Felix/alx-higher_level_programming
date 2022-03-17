#!/bin/bash
# Script sends request to URl passed as argument and displays only status code of response
curl -s -o /dev/null -w "%{http_code}" "$1"
