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

class EnergyManagementSystem:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def display_info(self):
        """Display information about the energy management system."""
        print(f"Energy Management System: {self.name}, Capacity: {self.capacity} kW")

class EnergyManager:
    def __init__(self):
        self.systems = []

    def add_system(self, energy_system):
        """Add an energy management system to the manager."""
        self.systems.append(energy_system)

    def display_systems(self):
        """Display all energy management systems."""
        for system in self.systems:
            system.display_info()

    def analyze_efficiency(self):
        """Analyze the efficiency of energy management systems."""
        efficiencies = [system.capacity for system in self.systems]
        avg_efficiency = np.mean(efficiencies)
        print(f"Average Energy Management System Efficiency: {avg_efficiency:.2f} kW")

    def predict_efficiency(self, historical_data):
        """Predict energy management system efficiency based on historical data."""
        print("Predicting Energy Management System Efficiency...")
        X = historical_data[['Year']]
        y = historical_data['Efficiency']

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
        plt.scatter(X_test, y_test, color='blue', label='Actual Efficiency')
        plt.scatter(X_test, predictions, color='red', label='Predicted Efficiency')
        plt.xlabel('Year')
        plt.ylabel('Efficiency (%)')
        plt.title('Energy Management System Efficiency Prediction')
        plt.legend()
        plt.show()

    def optimize_energy_consumption(self, energy_demand):
        """Optimize energy consumption based on energy demand."""
        print("Optimizing Energy Consumption...")
        # Define a neural network model
        model = keras.Sequential([
            layers.Dense(64, activation='relu', input_shape=(1,)),
            layers.Dense(32, activation='relu'),
            layers.Dense(1)
        ])

        # Compile the model
        model.compile(optimizer='adam', loss='mean_squared_error')

        # Train the model
        model.fit(energy_demand, epochs=100, verbose=0)

        # Make predictions
        optimized_energy_consumption = model.predict(energy_demand)

        # Visualize optimized energy consumption
        plt.figure(figsize=(10, 5))
        plt.plot(energy_demand, label='Actual Energy Demand')
        plt.plot(optimized_energy_consumption, label='Optimized Energy Consumption')
        plt.xlabel('Time')
        plt.ylabel('Energy Consumption (kW)')
        plt.title('Optimized Energy Consumption')
        plt.legend()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Create an EnergyManager instance
    energy_manager = EnergyManager()

    # Load energy management systems data (name, capacity)
    energy_systems_data = [
        ("Solar Panel", 100),
        ("Wind Turbine", 50),
        ("Battery", 200)
    ]

    for data in energy_systems_data:
        energy_system = EnergyManagementSystem(*data)
        energy_manager.add_system(energy_system)

    # Display energy management systems
    energy_manager.display_systems()

    # Analyze average efficiency
    energy_manager.analyze_efficiency()

    # Predict energy management system efficiency based on historical data
    historical_data = pd.DataFrame({
        'Year': [2018, 2019, 2020, 2021, 2022],
        'Efficiency': [85, 87, 88, 90, 92]
    })
    energy_manager.predict_efficiency(historical_data)

    # Optimize energy consumption based on energy demand
    energy_demand = np.array([10, 20, 30, 40,  50])
    energy_manager.optimize_energy_consumption(energy_demand)
