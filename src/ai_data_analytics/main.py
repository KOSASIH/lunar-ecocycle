# main.py

import pandas as pd
import numpy as np
from print_materials import MaterialManager, PrintMaterial
from recycling_process import RecyclingProcess, RecyclingMaterial
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

class LunarEcoCycle:
    def __init__(self):
        self.material_manager = MaterialManager()
        self.recycling_process = RecyclingProcess()

    def load_materials(self, materials_data):
        for data in materials_data:
            material = PrintMaterial(*data)
            self.material_manager.add_material(material)

    def load_recycling_materials(self, recycling_data):
        for data in recycling_data:
            recycling_material = RecyclingMaterial(*data)
            self.recycling_process.add_material(recycling_material)

    def analyze_materials(self):
        print("Analyzing Materials...")
        self.material_manager.display_materials()

    def predict_recycling(self, historical_data):
        print("Predicting Recycling Trends...")
        X = historical_data[['Year']]
        y = historical_data['Recycled Quantity']

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train a Random Forest Regressor
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Make predictions
        predictions = model.predict(X_test)

        # Visualize predictions
        plt.figure(figsize=(10, 5))
        plt.scatter(X_test, y_test, color='blue', label='Actual Data')
        plt.scatter(X_test, predictions, color='red', label='Predicted Data')
        plt.xlabel('Year')
        plt.ylabel('Recycled Quantity (kg)')
        plt.title('Recycling Quantity Prediction with Random Forest')
        plt.legend()
        plt.show()

# Example usage
if __name__ == "__main__":
    lunar_ecocycle = LunarEcoCycle()

    # Load materials data (name, density, melting_point, tensile_strength, cost, compatibility, environmental_impact, availability)
    materials_data = [
        ("PLA", 1.24, 180, 50, 20, ["FDM"], 3, 8),
        ("ABS", 1.04, 220, 40, 25, ["FDM"], 5, 7),
        ("PETG", 1.27, 230, 50, 30, ["FDM", "SLS"], 4, 9),
        ("Nylon", 1.15, 260, 70, 35, ["FDM", "SLS"], 6, 6)
    ]
    lunar_ecocycle.load_materials(materials_data)

    # Load recycling materials data (name, type, quantity, recycling_rate)
    recycling_data = [
        ("PET Bottles", "Plastic", 1000, 80),
        ("Aluminum Cans", "Metal", 500, 90),
        ("Glass Bottles", "Glass", 300, 70)
    ]
    lunar_ecocycle.load_recycling_materials(recycling_data)

    # Analyze materials
    lunar_ecocycle.analyze_materials()

    # Predict recycling trends
    historical_data = pd.DataFrame({
        'Year': [2018, 2019, 2020, 2021, 2022],
        'Recycled Quantity': [800, 850, 900, 950, 1000]
    })
    lunar_ecocycle.predict_recycling(historical_data)
