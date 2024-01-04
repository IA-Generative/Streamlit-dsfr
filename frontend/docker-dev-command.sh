#!/bin/sh

set -e

# Update the dependencies
npm clean-install
npm cache clean --force

# Create symlink to streamlit component library
# Workaround for "Unexpected token 'export'" error
ln -s /app/node_modules/streamlit-component-lib/dist ./src/stcomponentlib

exec npm run dev -- --host --port ${PORT:-80}
