#!/bin/bash

# Set variables
LOG_FILE="./logs/setup_environment.log"
REQUIREMENTS_FILE="./requirements.txt"  # Python dependencies
ENV_DIR="./venv"  # Virtual environment directory
DOCKER_IMAGE="your_docker_image"  # Replace with your Docker image name

# Create necessary directories
mkdir -p $(dirname $LOG_FILE)

# Function to log messages
log_message() {
    local MESSAGE=$1
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $MESSAGE" >> $LOG_FILE
}

# Function to create a virtual environment
create_virtual_environment() {
    log_message "Creating virtual environment..."
    if python3 -m venv $ENV_DIR; then
        log_message "Virtual environment created successfully."
    else
        log_message "Error: Failed to create virtual environment."
        exit 1
    fi
}

# Function to activate the virtual environment and install dependencies
install_dependencies() {
    log_message "Installing dependencies from $REQUIREMENTS_FILE..."
    source $ENV_DIR/bin/activate
    if pip install -r $REQUIREMENTS_FILE; then
        log_message "Dependencies installed successfully."
    else
        log_message "Error: Failed to install dependencies."
        exit 1
    fi
}

# Function to build Docker image (optional)
build_docker_image() {
    log_message "Building Docker image..."
    if docker build -t $DOCKER_IMAGE .; then
        log_message "Docker image built successfully."
    else
        log_message "Error: Failed to build Docker image."
        exit 1
    fi
}

# Main script execution
log_message "Environment setup script started."

# Create virtual environment
create_virtual_environment

# Install dependencies
install_dependencies

# Optionally build Docker image
# Uncomment the following line if you want to build the Docker image as part of the setup
# build_docker_image

log_message "Environment setup script completed."
