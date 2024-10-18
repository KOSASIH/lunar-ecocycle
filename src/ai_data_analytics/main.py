import logging
from predictive_model import PredictiveModel
from data_visualization import DataVisualizer

def main():
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    
    # Initialize predictive model
    predictive_model = PredictiveModel()
    
    # Train the predictive model
    predictive_model.train_model()
    logging.info("Predictive model trained.")
    
    # Initialize data visualizer
    data_visualizer = DataVisualizer()
    
    # Visualize data
    data_visualizer.visualize_data()
    logging.info("Data visualized.")

if __name__ == "__main__":
    main()
