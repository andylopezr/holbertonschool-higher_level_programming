#!/bin/bash
# Displays only the status code of response
curl -so /dev/null --write-out "%{http_code}" "$1"
