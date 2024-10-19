# main.py

import numpy as np
import cv2
import joblib
from sklearn.preprocessing import StandardScaler
from waste_sorting import WasteSorter, SensorManager

class Main:
    def __init__(self):
        self.waste_sorter = WasteSorter()
        self.sensor_manager = SensorManager()
        self.scaler = StandardScaler()

    def load_model(self, model_path):
        """Load the pre-trained machine learning model for waste classification."""
        self.model = joblib.load(model_path)
        print("Model loaded successfully.")

    def preprocess_data(self, data):
        """Preprocess the input data for classification."""
        data_scaled = self.scaler.transform(data)
        return data_scaled

    def classify_waste(self, image):
        """Classify waste using the loaded model."""
        features = self.extract_features(image)
        features_scaled = self.preprocess_data(features)
        prediction = self.model.predict(features_scaled)
        return prediction

    def extract_features(self, image):
        """Extract features from the image for classification."""
        # Example feature extraction (color histogram, shape, etc.)
        histogram = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
        histogram = cv2.normalize(histogram, histogram).flatten()
        return histogram.reshape(1, -1)

    def run(self):
        """Main loop for waste sorting."""
        while True:
            # Read data from sensors
            sensor_data = self.sensor_manager.read_sensors()
            print(f"Sensor Data: {sensor_data}")

            # Capture image from camera
            image = self.sensor_manager.capture_image()

            # Classify waste
            waste_type = self.classify_waste(image)
            print(f"Classified Waste Type: {waste_type}")

            # Sort waste based on classification
            self.waste_sorter.sort_waste(waste_type)

            # Check for exit condition
            if self.check_exit_condition():
                break

    def check_exit_condition(self):
        """Check if the main loop should exit."""
        # Implement exit condition logic (e.g., user input, sensor signal)
        return False

if __name__ == "__main__":
    main = Main()
    main.load_model("path/to/your/model.pkl")  # Update with the actual model path
    main.run()
