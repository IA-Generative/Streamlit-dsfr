#!/bin/sh

set -e

# Update the dependencies
python -m build

# Copy the dist folder to /tmp/dist
rm -rf /tmp/dist/*
cp -r ./dist/* /tmp/dist
