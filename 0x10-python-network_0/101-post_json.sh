#!/bin/bash
# Sends a POST request with the contents of a file
curl -s -X POST -d @"$2" -H "Content-Type: application/json" "$1"
