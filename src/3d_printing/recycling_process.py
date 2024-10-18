# recycling_process.py

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

class RecyclingMaterial:
    def __init__(self, name, type, quantity, recycling_rate):
        self.name = name
        self.type = type  # Type of material (e.g., plastic, metal, glass)
        self.quantity = quantity  # Quantity in kg
        self.recycling_rate = recycling_rate  # Recycling rate as a percentage

    def __repr__(self):
        return f"{self.name} ({self.type}): Quantity={self.quantity} kg, Recycling Rate={self.recycling_rate}%"

class RecyclingProcess:
    def __init__(self):
        self.materials = []

    def add_material(self, material):
        self.materials.append(material)

    def calculate_recycled_quantity(self):
        total_recycled = 0
        for material in self.materials:
            recycled = material.quantity * (material.recycling_rate / 100)
            total_recycled += recycled
        return total_recycled

    def generate_report(self):
        report_data = {
            "Material": [],
            "Type": [],
            "Quantity (kg)": [],
            "Recycled Quantity (kg)": [],
            "Recycling Rate (%)": []
        }
        for material in self.materials:
            recycled_quantity = material.quantity * (material.recycling_rate / 100)
            report_data["Material"].append(material.name)
            report_data["Type"].append(material.type)
            report_data["Quantity (kg)"].append(material.quantity)
            report_data["Recycled Quantity (kg)"].append(recycled_quantity)
            report_data["Recycling Rate (%)"].append(material.recycling_rate)

        report_df = pd.DataFrame(report_data)
        print(report_df)

    def predict_recycling_trends(self, historical_data):
        # Assuming historical_data is a DataFrame with columns ['Year', 'Recycled Quantity']
        X = historical_data['Year'].values.reshape(-1, 1)
        y = historical_data['Recycled Quantity'].values

        model = LinearRegression()
        model.fit(X, y)

        future_years = np.array([[year] for year in range(X[-1][0] + 1, X[-1][0] + 6)])  # Predict for next 5 years
        predictions = model.predict(future_years)

        plt.figure(figsize=(10, 5))
        plt.scatter(X, y, color='blue', label='Historical Data')
        plt.plot(future_years, predictions, color='red', label='Predicted Trend')
        plt.xlabel('Year')
        plt.ylabel('Recycled Quantity (kg)')
        plt.title('Recycling Quantity Prediction')
        plt.legend()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Create a RecyclingProcess instance
    recycling_process = RecyclingProcess()

    # Add some materials
    recycling_process.add_material(RecyclingMaterial("PET Bottles", "Plastic", 1000, 80))
    recycling_process.add_material(RecyclingMaterial("Aluminum Cans", "Metal", 500, 90))
    recycling_process.add_material(RecyclingMaterial("Glass Bottles", "Glass", 300, 70))

    # Calculate total recycled quantity
    total_recycled = recycling_process.calculate_recycled_quantity()
    print(f"Total Recycled Quantity: {total_recycled} kg")

    # Generate a report
    print("\nRecycling Report:")
    recycling_process.generate_report()

    # Predict recycling trends
    historical_data = pd.DataFrame({
        'Year': [2018, 2019, 2020, 2021, 2022],
        'Recycled Quantity': [800, 850, 900, 950, 1000]
    })
    recycling_process.predict_recycling_trends(historical_data)
