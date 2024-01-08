#!/bin/sh

set -e

# Copy the dist folder to /tmp/dist
rm -rf /tmp/dist/*
cp -r ./dist/* /tmp/dist
