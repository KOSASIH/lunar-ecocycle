# main.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

class Resource:
    def __init__(self, name, quantity, extraction_rate):
        self.name = name
        self.quantity = quantity  # in kg
        self.extraction_rate = extraction_rate  # in kg/hour

    def display_info(self):
        """Display information about the resource."""
        print(f"Resource: {self.name}, Quantity: {self.quantity} kg, Extraction Rate: {self.extraction_rate} kg/h")

class ISRUManager:
    def __init__(self):
        self.resources = []

    def add_resource(self, resource):
        """Add a resource to the ISRU manager."""
        self.resources.append(resource)

    def display_resources(self):
        """Display all resources."""
        for resource in self.resources:
            resource.display_info()

    def analyze_extraction_efficiency(self):
        """Analyze the efficiency of resource extraction."""
        total_quantity = sum(resource.quantity for resource in self.resources)
        total_extraction_rate = sum(resource.extraction_rate for resource in self.resources)
        avg_extraction_rate = total_extraction_rate / len(self.resources) if self.resources else 0
        print(f"Total Resource Quantity: {total_quantity} kg, Total Extraction Rate: {total_extraction_rate} kg/h, Average Extraction Rate: {avg_extraction_rate:.2f} kg/h")

    def predict_extraction(self, historical_data):
        """Predict resource extraction based on historical data."""
        print("Predicting Resource Extraction...")
        X = historical_data[['Time', 'Environmental_Conditions']]
        y = historical_data['Extraction_Amount']

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train a Random Forest Regressor
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Make predictions
        predictions = model.predict(X_test)

        # Evaluate the model
        mse = mean_squared_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)
        print(f"Mean Squared Error: {mse:.2f}")
        print(f"R^2 Score: {r2:.2f}")

        # Visualize predictions
        plt.figure(figsize=(10, 5))
        plt.scatter(X_test['Time'], y_test, color='blue', label='Actual Extraction')
        plt.scatter(X_test['Time'], predictions, color='red', label='Predicted Extraction')
        plt.xlabel('Time')
        plt.ylabel('Extraction Amount (kg)')
        plt.title('Resource Extraction Prediction')
        plt.legend()
        plt.show()

    def optimize_extraction_process(self, extraction_data):
        """Optimize the extraction process based on historical data."""
        print("Optimizing Extraction Process...")
        # Define a neural network model
        model = keras.Sequential([
            layers.Dense(64, activation='relu', input_shape=(extraction_data.shape[1],)),
            layers.Dense(32, activation='relu'),
            layers.Dense(1)
        ])

        # Compile the model
        model.compile(optimizer='adam', loss='mean_squared_error')

        # Train the model
        model.fit(extraction_data, epochs=100, verbose=0)

        # Make predictions
        optimized_extraction = model.predict(extraction_data)

        # Visualize optimized extraction
        plt.figure(figsize=(10, 5))
        plt.plot(extraction_data, label='Actual Extraction Amount')
        plt.plot(optimized_extraction, label='Optimized Extraction Amount')
        plt.xlabel('Time')
        plt.ylabel('Extraction Amount (kg)')
        plt.title('Optimized Resource Extraction')
        plt.legend()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Create an ISRUManager instance
    isru_manager = ISRUManager()

    # Load resource data (name, quantity, extraction_rate)
    resource_data = [
        ("Water", 1000, 50),
        ("Oxygen", 500, 25),
        ("Hydrogen", 300, 15)
    ]

    for data in resource_data:
        resource = Resource(*data)
        isru_manager.add_resource(resource)

    # Display resources
    isru_manager.display_resources()

    # Analyze extraction efficiency
    isru_manager.analyze_extraction_efficiency()

    # Predict resource extraction based on historical data
    historical_data = pd.DataFrame({
        'Time': [1, 2, 3, 4, 5],
        'Environmental_Conditions': [20, 25, 30, 35, 40],
        'Extraction_Amount': [50, 60, 70, 80, 90]
    })
    isru_manager.predict_extraction(historical_data)

    # Optimize the extraction process based on historical data
    extraction_data = np.array([50, 60, 70, 80, 90])
    isru_manager.optimize_extraction_process(extraction_data)
