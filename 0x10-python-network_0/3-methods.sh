#!/bin/bash
# Takes in an URL and displays all HTTP methods server accepts
curl -sI "$1" | grep Allow | cut -d' ' -f2-
