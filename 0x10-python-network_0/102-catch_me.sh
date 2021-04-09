#!/bin/bash
# Script to make a request to receive a custom message as response
curl -sL -X PUT -H "Origin:HolbertonSchool" -d "user_id=98" "0.0.0.0:5000/catch_me"
