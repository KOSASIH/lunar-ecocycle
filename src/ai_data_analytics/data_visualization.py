# data_visualization.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualizer:
    def __init__(self, materials_data, recycling_data):
        self.materials_data = materials_data
        self.recycling_data = recycling_data

    def plot_material_properties(self):
        """Visualize material properties such as tensile strength and cost."""
        materials_df = pd.DataFrame(self.materials_data, columns=[
            "Name", "Density", "Melting Point", "Tensile Strength", "Cost", "Compatibility", "Environmental Impact", "Availability"
        ])
        
        plt.figure(figsize=(12, 6))
        sns.barplot(x='Name', y='Tensile Strength', data=materials_df, palette='viridis')
        plt.title('Tensile Strength of Materials')
        plt.ylabel('Tensile Strength (MPa)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_recycling_trends(self):
        """Visualize recycling trends over the years."""
        recycling_df = pd.DataFrame(self.recycling_data, columns=[
            "Material", "Type", "Quantity", "Recycling Rate"
        ])
        
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=recycling_df, x='Material', y='Quantity', marker='o', label='Quantity', color='blue')
        plt.title('Recycling Quantity by Material')
        plt.ylabel('Quantity (kg)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_recycling_rate_distribution(self):
        """Visualize the distribution of recycling rates."""
        recycling_df = pd.DataFrame(self.recycling_data, columns=[
            "Material", "Type", "Quantity", "Recycling Rate"
        ])
        
        plt.figure(figsize=(12, 6))
        sns.histplot(recycling_df['Recycling Rate'], bins=10, kde=True, color='green')
        plt.title('Distribution of Recycling Rates')
        plt.xlabel('Recycling Rate (%)')
        plt.ylabel('Frequency')
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Sample materials data (name, density, melting_point, tensile_strength, cost, compatibility, environmental_impact, availability)
    materials_data = [
        ("PLA", 1.24, 180, 50, 20, ["FDM"], 3, 8),
        ("ABS", 1.04, 220, 40, 25, ["FDM"], 5, 7),
        ("PETG", 1.27, 230, 50, 30, ["FDM", "SLS"], 4, 9),
        ("Nylon", 1.15, 260, 70, 35, ["FDM", "SLS"], 6, 6)
    ]

    # Sample recycling data (name, type, quantity, recycling_rate)
    recycling_data = [
        ("PET Bottles", "Plastic", 1000, 80),
        ("Aluminum Cans", "Metal", 500, 90),
        ("Glass Bottles", "Glass", 300, 70)
    ]

    # Create a DataVisualizer instance
    visualizer = DataVisualizer(materials_data, recycling_data)

    # Generate visualizations
    visualizer.plot_material_properties()
    visualizer.plot_recycling_trends()
    visualizer.plot_recycling_rate_distribution()
