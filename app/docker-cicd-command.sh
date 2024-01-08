#!/bin/sh

set -e

# Assert the dist folder is not empty
if [ ! "$(ls -A ./dist 2> /dev/null)" ]; then
  echo "Error: The dist folder is empty. Try to rebuild the image." >&2
  exit 1
fi

# Copy the dist folder to /tmp/dist
rm -rf /tmp/dist/*
cp -r ./dist/* /tmp/dist
