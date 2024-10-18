import yaml
from predictive_model import PredictiveModel
from data_visualization import DataVisualizer

def load_config(config_file):
    """Load configuration from a YAML file."""
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config

def main():
    # Load configuration
    config = load_config("examples/sample_config.yaml")
    
    # Set up logging based on config
    import logging
    logging.basicConfig(level=config['eco_cycle']['logging']['level'],
                        filename=config['eco_cycle']['logging']['file'])
    
    # Initialize and train the predictive model
    predictive_model = PredictiveModel()
    predictive_model.train_model()
    logging.info("Predictive model trained.")

    # Visualize data if enabled in config
    if config['visualization']['enabled']:
        data_visualizer = DataVisualizer()
        data_visualizer.visualize_data()
        logging.info("Data visualized.")

if __name__ == "__main__":
    main()
