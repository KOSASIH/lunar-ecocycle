# main.py

import pandas as pd
import numpy as np
from bioregenerative_system import BioregenerativeSystem, Plant, NutrientCycle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

class LunarBioregenerativeSystem:
    def __init__(self):
        self.bioregenerative_system = BioregenerativeSystem()

    def load_plants(self, plants_data):
        for data in plants_data:
            plant = Plant(*data)
            self.bioregenerative_system.add_plant(plant)

    def load_nutrient_cycles(self, nutrient_data):
        for data in nutrient_data:
            nutrient_cycle = NutrientCycle(*data)
            self.bioregenerative_system.add_nutrient_cycle(nutrient_cycle)

    def analyze_system(self):
        print("Analyzing Bioregenerative System...")
        self.bioregenerative_system.display_plants()
        self.bioregenerative_system.display_nutrient_cycles()

    def predict_yield(self, historical_data):
        print("Predicting Plant Yield...")
        X = historical_data[['Year']]
        y = historical_data['Yield']

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train a Random Forest Regressor
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Make predictions
        predictions = model.predict(X_test)

        # Visualize predictions
        plt.figure(figsize=(10, 5))
        plt.scatter(X_test, y_test, color='blue', label='Actual Yield')
        plt.scatter(X_test, predictions, color='red', label='Predicted Yield')
        plt.xlabel('Year')
        plt.ylabel('Yield (kg)')
        plt.title('Plant Yield Prediction with Random Forest')
        plt.legend()
        plt.show()

# Example usage
if __name__ == "__main__":
    lunar_bioregenerative_system = LunarBioregenerativeSystem()

    # Load plants data (name, growth_rate, nutrient_requirements, water_needs, yield_per_year)
    plants_data = [
        ("Wheat", 1.2, ["N", "P", "K"], 500, 2000),
        ("Corn", 1.5, ["N", "P", "K"], 600, 3000),
        ("Soybean", 1.0, ["N", "P"], 400, 1500),
        ("Rice", 1.3, ["N", "P", "K"], 550, 2500)
    ]
    lunar_bioregenerative_system.load_plants(plants_data)

    # Load nutrient cycles data (name, cycle_type, efficiency)
    nutrient_data = [
        ("Nitrogen Cycle", "Biological", 90),
        ("Phosphorus Cycle", "Geological", 80),
        ("Potassium Cycle", "Chemical", 85)
    ]
    lunar_bioregenerative_system.load_nutrient_cycles(nutrient_data)

    # Analyze the bioregenerative system
    lunar_bioregenerative_system.analyze_system()

    # Predict plant yield
    historical_data = pd.DataFrame({
        'Year': [2018, 2019, 2020, 2021, 2022],
        'Yield': [1800, 1900, 2100, 2200, 2300]
    })
    lunar_bioregenerative_system.predict_yield(historical_data)
