# water_recovery.py

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

class WaterRecovery:
    def __init__(self, total_capacity, recovery_rate):
        self.total_capacity = total_capacity  # in liters
        self.recovery_rate = recovery_rate  # in liters/hour
        self.recovered_amount = 0  # in liters

    def recover_water(self, hours):
        """Recover water over a specified number of hours."""
        recovered = min(self.recovery_rate * hours, self.total_capacity - self.recovered_amount)
        self.recovered_amount += recovered
        print(f"Recovered {recovered:.2f} liters of water. Total Recovered: {self.recovered_amount:.2f} liters")

    def display_info(self):
        """Display information about the water recovery system."""
        print(f"Total Capacity: {self.total_capacity} liters, Recovery Rate: {self.recovery_rate} liters/h, "
              f"Recovered Amount: {self.recovered_amount:.2f} liters")

class WaterRecoveryManager:
    def __init__(self):
        self.water_recovery_systems = []

    def add_water_recovery_system(self, water_recovery):
        """Add a water recovery system to the manager."""
        self.water_recovery_systems.append(water_recovery)

    def display_systems(self):
        """Display all water recovery systems."""
        for system in self.water_recovery_systems:
            system.display_info()

    def analyze_recovery_efficiency(self):
        """Analyze the efficiency of water recovery systems."""
        total_recovered = sum(system.recovered_amount for system in self.water_recovery_systems)
        total_recovery_rate = sum(system.recovery_rate for system in self.water_recovery_systems)
        avg_recovery_rate = total_recovery_rate / len(self.water_recovery_systems) if self.water_recovery_systems else 0
        print(f"Total Recovered Water: {total_recovered:.2f} liters, Total Recovery Rate: {total_recovery_rate:.2f} liters/h, "
              f"Average Recovery Rate: {avg_recovery_rate:.2f} liters/h")

    def predict_recovery(self, historical_data):
        """Predict water recovery based on historical data."""
        print("Predicting Water Recovery...")
        X = historical_data[['Time', 'Environmental_Conditions']]
        y = historical_data['Recovered_Amount']

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
        plt.scatter(X_test['Time'], y_test, color='blue', label='Actual Recovery')
        plt.scatter(X_test['Time'], predictions, color='red', label='Predicted Recovery')
        plt.xlabel('Time')
        plt.ylabel('Recovered Amount (liters)')
        plt.title('Water Recovery Prediction')
        plt.legend()
        plt.show()

    def optimize_recovery_process(self, recovery_data):
        """Optimize the water recovery process based on historical data."""
        print("Optimizing Water Recovery Process...")
        # Define a neural network model
        model = keras.Sequential([
            layers.Dense(64, activation='relu', input_shape=(recovery_data.shape[1],)),
            layers.Dense(32, activation='relu'),
            layers.Dense(1)
        ])

        # Compile the model
        model.compile(optimizer='adam', loss='mean_squared_error')

        # Train the model
        model.fit(recovery_data, epochs=100, verbose=0)

        # Make predictions
        optimized_recovery = model.predict(recovery_data)

        # Visualize optimized recovery
        plt .figure(figsize=(10, 5))
        plt.plot(recovery_data, label='Actual Recovery Amount')
        plt.plot(optimized_recovery, label='Optimized Recovery Amount')
        plt.xlabel('Time')
        plt.ylabel('Recovered Amount (liters)')
        plt.title('Optimized Water Recovery')
        plt.legend()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Create a WaterRecoveryManager instance
    manager = WaterRecoveryManager()

    # Load water recovery system data (total_capacity, recovery_rate)
    recovery_data = [
        (1000, 50),
        (500, 25),
        (300, 15)
    ]

    for data in recovery_data:
        water_recovery = WaterRecovery(*data)
        manager.add_water_recovery_system(water_recovery)

    # Display water recovery systems
    manager.display_systems()

    # Analyze recovery efficiency
    manager.analyze_recovery_efficiency()

    # Predict water recovery based on historical data
    historical_data = pd.DataFrame({
        'Time': [1, 2, 3, 4, 5],
        'Environmental_Conditions': [20, 25, 30, 35, 40],
        'Recovered_Amount': [50, 60, 70, 80, 90]
    })
    manager.predict_recovery(historical_data)

    # Optimize the water recovery process based on historical data
    recovery_data = np.array([50, 60, 70, 80, 90])
    manager.optimize_recovery_process(recovery_data)
