#!/bin/bash
set -e

cd /workspaces/github-copilot-demo/octofit-tracker/backend

# Create virtual environment
echo "Creating Python virtual environment..."
python3 -m venv venv

# Activate venv and install requirements
echo "Installing required packages..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "Virtual environment setup complete!"
echo "To activate the virtual environment, run: source octofit-tracker/backend/venv/bin/activate"
