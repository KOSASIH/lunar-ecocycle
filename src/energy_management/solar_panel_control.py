# solar_panel_control.py

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

class SolarPanel:
    def __init__(self, name, capacity, current_output, angle):
        self.name = name
        self.capacity = capacity  # in kW
        self.current_output = current_output  # in kW
        self.angle = angle  # in degrees

    def display_info(self):
        """Display information about the solar panel."""
        print(f"Solar Panel: {self.name}, Capacity: {self.capacity} kW, Current Output: {self.current_output} kW, Angle: {self.angle}°")

    def adjust_angle(self, new_angle):
        """Adjust the angle of the solar panel."""
        self.angle = new_angle
        print(f"Adjusted angle to {self.angle}°")

class SolarPanelManager:
    def __init__(self):
        self.panels = []

    def add_panel(self, solar_panel):
        """Add a solar panel to the manager."""
        self.panels.append(solar_panel)

    def display_panels(self):
        """Display all solar panels."""
        for panel in self.panels:
            panel.display_info()

    def analyze_performance(self):
        """Analyze the performance of solar panels."""
        total_capacity = sum(panel.capacity for panel in self.panels)
        total_output = sum(panel.current_output for panel in self.panels)
        avg_output = total_output / len(self.panels) if self.panels else 0
        print(f"Total Capacity: {total_capacity} kW, Total Output: {total_output} kW, Average Output: {avg_output:.2f} kW")

    def predict_output(self, historical_data):
        """Predict solar panel output based on historical data."""
        print("Predicting Solar Panel Output...")
        X = historical_data[['Sunlight_Hours', 'Temperature']]
        y = historical_data['Output']

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
        plt.scatter(X_test['Sunlight_Hours'], y_test, color='blue', label='Actual Output')
        plt.scatter(X_test['Sunlight_Hours'], predictions, color='red', label='Predicted Output')
        plt.xlabel('Sunlight Hours')
        plt.ylabel('Output (kW)')
        plt.title('Solar Panel Output Prediction')
        plt.legend()
        plt.show()

    def optimize_output(self, sunlight_data):
        """Optimize solar panel output based on sunlight data."""
        print("Optimizing Solar Panel Output...")
        # Define a neural network model
        model = keras.Sequential([
            layers.Dense(64, activation='relu', input_shape=(sunlight_data.shape[1],)),
            layers.Dense(32, activation='relu'),
            layers.Dense(1)
        ])

        # Compile the model
        model.compile(optimizer='adam', loss='mean_squared_error')

        # Train the model
        model.fit(sunlight_data, epochs=100, verbose=0)

        # Make predictions
        optimized_output = model.predict(sunlight_data)

        # Visualize optimized output
        plt.figure(figsize=(10, 5))
        plt.plot(sunlight_data, label='Actual Solar Output')
        plt.plot(optimized_output, label='Optimized Solar Output')
        plt.xlabel('Time')
        plt.ylabel('Solar Output (kW)')
        plt.title('Optimized Solar Panel Output')
        plt.legend()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Create a SolarPanelManager instance
    solar _panel_manager = SolarPanelManager()

    # Load solar panel data (name, capacity, current_output, angle)
    solar_panel_data = [
        ("Panel 1", 100, 80, 30),
        ("Panel 2", 150, 120, 45),
        ("Panel 3", 200, 180, 60)
    ]

    for data in solar_panel_data:
        solar_panel = SolarPanel(*data)
        solar_panel_manager.add_panel(solar_panel)

    # Display solar panels
    solar_panel_manager.display_panels()

    # Analyze solar panel performance
    solar_panel_manager.analyze_performance()

    # Predict solar panel output based on historical data
    historical_data = pd.DataFrame({
        'Sunlight_Hours': [4, 5, 6, 7, 8],
        'Temperature': [20, 25, 30, 35, 40],
        'Output': [80, 90, 100, 110, 120]
    })
    solar_panel_manager.predict_output(historical_data)

    # Optimize solar panel output based on sunlight data
    sunlight_data = np.array([4, 5, 6, 7, 8])
    solar_panel_manager.optimize_output(sunlight_data)
