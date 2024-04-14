#!/bin/bash

# Set script to exit on error
set -e

# Create a virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "Virtual environment created."
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Update pip to its latest version
echo "Updating pip..."
pip install --upgrade pip

# Install required Python packages
echo "Installing requirements from requirements.txt..."
pip install -r requirements.txt

echo "Dependencies installed successfully."
