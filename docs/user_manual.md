# User Manual for the Lunar EcoCycle System

## Introduction
This manual provides instructions for operating the Lunar EcoCycle system. It is intended for users who will interact with the system components.

## Getting Started
1. **System Requirements**: Ensure that the following prerequisites are met:
   - Power supply: 220V AC
   - Network connectivity for remote monitoring

2. **Installation**:
   - Clone the repository:
     ```bash
     git clone https://github.com/your-repo/lunar-ecocycle.git
     ```
   - Navigate to the project directory and run the setup script:
     ```bash
     cd lunar-ecocycle
     ./setup_environment.sh
     ```

## Operating the System
### Starting the EcoCycle
- To start the EcoCycle system, run the following command:
  ```bash
  ./deploy.sh
  ```

### Monitoring System Status

Access the monitoring dashboard at http://localhost:5000/status.

### Troubleshooting

Common Issues:

- If the Waste Sorting Module fails, check the logs in ./logs/deployment.log.
- For network issues, ensure that the system is connected to the lunar network.

# Contact Information

For further assistance, please contact the support team at support@lunarecocycle.org.
