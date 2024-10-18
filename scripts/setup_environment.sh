#!/bin/bash

# This script sets up the development environment for the EcoCycle system.

# Update package list
echo "Updating package list..."
sudo apt-get update

# Install necessary packages
echo "Installing necessary packages..."
sudo apt-get install -y python3 python3-pip python3-venv git

# Create a virtual environment
echo "Creating a virtual environment..."
python3 -m venv eco_cycle_env

# Activate the virtual environment
echo "Activating the virtual environment..."
source eco_cycle_env/bin/activate

# Install required Python packages
echo "Installing required Python packages..."
pip install -r requirements.txt

echo "Development environment setup complete!"
