#!/bin/bash

# Set variables
APP_DIR="/path/to/your/app"  # Update with the actual application directory
LOG_FILE="./logs/deployment.log"
ENV_FILE="./.env"  # Environment variables file
DOCKER_IMAGE="your_docker_image"  # Replace with your Docker image name
MAX_RETRIES=3

# Create necessary directories
mkdir -p $(dirname $LOG_FILE)

# Function to log messages
log_message() {
    local MESSAGE=$1
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $MESSAGE" >> $LOG_FILE
}

# Function to load environment variables
load_env() {
    if [ -f $ENV_FILE ]; then
        export $(grep -v '^#' $ENV_FILE | xargs)
        log_message "Environment variables loaded from $ENV_FILE."
    else
        log_message "Warning: Environment file $ENV_FILE not found."
    fi
}

# Function to build Docker image
build_docker_image() {
    log_message "Building Docker image..."
    if docker build -t $DOCKER_IMAGE $APP_DIR; then
        log_message "Docker image built successfully."
    else
        log_message "Error: Failed to build Docker image."
        exit 1
    fi
}

# Function to deploy the application
deploy_application() {
    log_message "Deploying application..."
    local attempt=1
    while [ $attempt -le $MAX_RETRIES ]; do
        log_message "Attempting to deploy (Attempt $attempt of $MAX_RETRIES)"
        
        if docker run -d --rm --env-file $ENV_FILE $DOCKER_IMAGE; then
            log_message "Application deployed successfully."
            return 0
        else
            log_message "Error: Deployment failed. Retrying..."
            ((attempt++))
            sleep 5  # Wait before retrying
        fi
    done
    log_message "Error: Failed to deploy application after $MAX_RETRIES attempts."
    exit 1
}

# Main script execution
log_message "Deployment script started."

# Load environment variables
load_env

# Build Docker image
build_docker_image

# Deploy the application
deploy_application

log_message "Deployment script completed."
