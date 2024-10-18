# nutrient_cycle.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

class NutrientCycle:
    def __init__(self, name, cycle_type, efficiency):
        self.name = name
        self.cycle_type = cycle_type
        self.efficiency = efficiency

    def display_info(self):
        """Display information about the nutrient cycle."""
        print(f"Nutrient Cycle: {self.name}, Type: {self.cycle_type}, Efficiency: {self.efficiency}%")

class NutrientCycleManager:
    def __init__(self):
        self.cycles = []

    def add_cycle(self, nutrient_cycle):
        """Add a nutrient cycle to the manager."""
        self.cycles.append(nutrient_cycle)

    def display_cycles(self):
        """Display all nutrient cycles."""
        for cycle in self.cycles:
            cycle.display_info()

    def analyze_efficiency(self):
        """Analyze the efficiency of nutrient cycles."""
        efficiencies = [cycle.efficiency for cycle in self.cycles]
        avg_efficiency = np.mean(efficiencies)
        print(f"Average Nutrient Cycle Efficiency: {avg_efficiency:.2f}%")

    def predict_efficiency(self, historical_data):
        """Predict nutrient cycle efficiency based on historical data."""
        print("Predicting Nutrient Cycle Efficiency...")
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
        plt.title('Nutrient Cycle Efficiency Prediction')
        plt.legend()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Create a NutrientCycleManager instance
    nutrient_cycle_manager = NutrientCycleManager()

    # Load nutrient cycles data (name, cycle_type, efficiency)
    nutrient_cycles_data = [
        ("Nitrogen Cycle", "Biological", 90),
        ("Phosphorus Cycle", "Geological", 80),
        ("Potassium Cycle", "Chemical", 85)
    ]

    for data in nutrient_cycles_data:
        nutrient_cycle = NutrientCycle(*data)
        nutrient_cycle_manager.add_cycle(nutrient_cycle)

    # Display nutrient cycles
    nutrient_cycle_manager.display_cycles()

    # Analyze average efficiency
    nutrient_cycle_manager.analyze_efficiency()

    # Predict nutrient cycle efficiency based on historical data
    historical_data = pd.DataFrame({
        'Year': [2018, 2019, 2020, 2021, 2022],
        'Efficiency': [85, 87, 88, 90, 92]
    })
    nutrient_cycle_manager.predict_efficiency(historical_data)
