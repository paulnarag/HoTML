#!/bin/bash

set -e

echo "Installing HoTML..."

sudo mkdir -p /usr/local/bin
sudo cp hotml /usr/local/bin/hotml
sudo chmod +x /usr/local/bin/hotml

echo ""
echo "HoTML installed successfully!"
echo ""
echo "Try:"
echo "  hotml help"
echo "  hotml create"