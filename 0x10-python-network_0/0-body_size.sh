#!/bin/bash
# Curls request and display bytes received
curl -sI "$1" | grep 'Content-Length:' | cut -d' ' -f2
