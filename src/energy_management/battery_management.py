# battery_management.py

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

class Battery:
    def __init__(self, name, capacity, current_charge, cycle_life):
        self.name = name
        self.capacity = capacity  # in kWh
        self.current_charge = current_charge  # in kWh
        self.cycle_life = cycle_life  # number of charge/discharge cycles

    def display_info(self):
        """Display information about the battery."""
        print(f"Battery: {self.name}, Capacity: {self.capacity} kWh, Current Charge: {self.current_charge} kWh, Cycle Life: {self.cycle_life} cycles")

    def charge(self, amount):
        """Charge the battery by a specified amount."""
        if self.current_charge + amount <= self.capacity:
            self.current_charge += amount
            print(f"Charged {amount} kWh. Current Charge: {self.current_charge} kWh")
        else:
            print("Charge exceeds battery capacity!")

    def discharge(self, amount):
        """Discharge the battery by a specified amount."""
        if self.current_charge - amount >= 0:
            self.current_charge -= amount
            print(f"Discharged {amount} kWh. Current Charge: {self.current_charge} kWh")
        else:
            print("Not enough charge to discharge!")

class BatteryManager:
    def __init__(self):
        self.batteries = []

    def add_battery(self, battery):
        """Add a battery to the manager."""
        self.batteries.append(battery)

    def display_batteries(self):
        """Display all batteries."""
        for battery in self.batteries:
            battery.display_info()

    def analyze_battery_performance(self):
        """Analyze the performance of batteries."""
        total_capacity = sum(battery.capacity for battery in self.batteries)
        total_current_charge = sum(battery.current_charge for battery in self.batteries)
        avg_charge = total_current_charge / len(self.batteries) if self.batteries else 0
        print(f"Total Capacity: {total_capacity} kWh, Total Current Charge: {total_current_charge} kWh, Average Charge: {avg_charge:.2f} kWh")

    def predict_cycle_life(self, historical_data):
        """Predict battery cycle life based on historical data."""
        print("Predicting Battery Cycle Life...")
        X = historical_data[['Temperature', 'Charge_Discharge_Cycles']]
        y = historical_data['Cycle_Life']

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
        plt.scatter(X_test['Charge_Discharge_Cycles'], y_test, color='blue', label='Actual Cycle Life')
        plt.scatter(X_test['Charge_Discharge_Cycles'], predictions, color='red', label='Predicted Cycle Life')
        plt.xlabel('Charge/Discharge Cycles')
        plt.ylabel('Cycle Life')
        plt.title('Battery Cycle Life Prediction')
        plt.legend()
        plt.show()

    def optimize_battery_usage(self, usage_data):
        """Optimize battery usage based on historical usage data."""
        print("Optimizing Battery Usage...")
        # Define a neural network model
        model = keras.Sequential([
            layers.Dense(64, activation='relu', input_shape=(usage_data.shape[1],)),
            layers.Dense(32, activation='relu'),
            layers.Dense(1)
        ])

        # Compile the model
        model.compile(optimizer='adam', loss='mean_squared_error')

        # Train the model
        model.fit(usage_data, epochs =100, verbose=0)

        # Make predictions
        optimized_usage = model.predict(usage_data)

        # Visualize optimized battery usage
        plt.figure(figsize=(10, 5))
        plt.plot(usage_data, label='Actual Battery Usage')
        plt.plot(optimized_usage, label='Optimized Battery Usage')
        plt.xlabel('Time')
        plt.ylabel('Battery Usage (kWh)')
        plt.title('Optimized Battery Usage')
        plt.legend()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Create a BatteryManager instance
    battery_manager = BatteryManager()

    # Load battery data (name, capacity, current_charge, cycle_life)
    battery_data = [
        ("Battery 1", 100, 80, 500),
        ("Battery 2", 150, 120, 600),
        ("Battery 3", 200, 180, 700)
    ]

    for data in battery_data:
        battery = Battery(*data)
        battery_manager.add_battery(battery)

    # Display batteries
    battery_manager.display_batteries()

    # Analyze battery performance
    battery_manager.analyze_battery_performance()

    # Predict battery cycle life based on historical data
    historical_data = pd.DataFrame({
        'Temperature': [20, 25, 30, 35, 40],
        'Charge_Discharge_Cycles': [100, 150, 200, 250, 300],
        'Cycle_Life': [500, 550, 600, 650, 700]
    })
    battery_manager.predict_cycle_life(historical_data)

    # Optimize battery usage based on historical usage data
    usage_data = np.array([10, 20, 30, 40, 50])
    battery_manager.optimize_battery_usage(usage_data)
