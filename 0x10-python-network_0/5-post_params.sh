#!/bin/bash
# Sends a POST request with email and subjetct variable
curl -s -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
