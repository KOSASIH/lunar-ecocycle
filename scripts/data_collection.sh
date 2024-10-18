#!/bin/bash

# This script collects data and logs it for the EcoCycle system.

# Define the log file
LOG_FILE="data_collection.log"

# Function to collect data
collect_data() {
    # Simulate data collection (replace with actual data collection logic)
    echo "$(date): Collected data point" >> "$LOG_FILE"
}

# Infinite loop to collect data at regular intervals
while true; do
    collect_data
    echo "Data collected at $(date)"
    sleep 60  # Collect data every 60 seconds
done
