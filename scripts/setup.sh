#!/bin/bash
set -euo pipefail
echo "Setting up Ticket Routing Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
