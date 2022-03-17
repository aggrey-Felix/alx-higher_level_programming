#!/bin/bash
#Script that takes in URL, sends a POST request to passed URL and displays the body of respone.
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
