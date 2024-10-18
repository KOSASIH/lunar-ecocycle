#!/bin/bash

# This script deploys the EcoCycle system.

# Navigate to the project directory
cd /path/to/your/project || exit

# Pull the latest code from the repository
echo "Pulling the latest code from the repository..."
git pull origin main

# Activate the virtual environment
echo "Activating the virtual environment..."
source eco_cycle_env/bin/activate

# Run migrations if applicable (uncomment if using a database)
# echo "Running database migrations..."
# python manage.py migrate

# Start the application (modify according to your application)
echo "Starting the EcoCycle application..."
python main.py &

echo "Deployment complete!"
