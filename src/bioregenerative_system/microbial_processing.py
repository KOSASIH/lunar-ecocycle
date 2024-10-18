# microbial_processing.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

class MicrobialProcessing:
    def __init__(self, microbial_data):
        self.microbial_data = microbial_data
        self.model = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

    def prepare_data(self):
        """Prepare the data for training and testing."""
        X = self.microbial_data[['Temperature', 'pH', 'Nutrient_Concentration']]
        y = self.microbial_data['Biomass_Yield']
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    def train_model(self):
        """Train the Random Forest Regressor model."""
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.model.fit(self.X_train, self.y_train)

    def evaluate_model(self):
        """Evaluate the model's performance."""
        predictions = self.model.predict(self.X_test)
        mse = mean_squared_error(self.y_test, predictions)
        r2 = r2_score(self.y_test, predictions)
        print(f"Mean Squared Error: {mse:.2f}")
        print(f"R^2 Score: {r2:.2f}")

        # Visualize predictions vs actual values
        plt.figure(figsize=(10, 5))
        plt.scatter(self.y_test, predictions, color='blue', label='Predictions')
        plt.plot([self.y_test.min(), self.y_test.max()], [self.y_test.min(), self.y_test.max()], color='red', lw=2, label='Ideal Fit')
        plt.xlabel('Actual Biomass Yield (g/L)')
        plt.ylabel('Predicted Biomass Yield (g/L)')
        plt.title('Predicted vs Actual Biomass Yield')
        plt.legend()
        plt.tight_layout()
        plt.show()

    def predict_future_yield(self, future_conditions):
        """Predict biomass yield under future conditions."""
        future_data = pd.DataFrame(future_conditions)
        future_predictions = self.model.predict(future_data)
        return future_data.assign(Predicted_Biomass_Yield=future_predictions)

# Example usage
if __name__ == "__main__":
    # Sample microbial data (temperature, pH, nutrient concentration, biomass yield)
    microbial_data = pd.DataFrame({
        'Temperature': [30, 32, 31, 29, 28, 33, 34, 30, 31, 29],
        'pH': [6.5, 6.8, 6.7, 6.4, 6.3, 6.9, 7.0, 6.5, 6.6, 6.4],
        'Nutrient_Concentration': [1.0, 1.2, 1.1, 0.9, 0.8, 1.3, 1.4, 1.0, 1.1, 0.9],
        'Biomass_Yield': [5.0, 5.5, 5.2, 4.8, 4.5, 5.7, 6.0, 5.1, 5.3, 4.9]
    })

    # Create a MicrobialProcessing instance
    microbial_processor = MicrobialProcessing(microbial_data)

    # Prepare data
    microbial_processor.prepare_data()

    # Train the model
    microbial_processor.train_model()

    # Evaluate the model
    microbial_processor.evaluate_model()

    # Predict future biomass yield under new conditions
    future_conditions = [
        {'Temperature': 31, 'pH': 6.6, 'Nutrient_Concentration': 1.1},
        {'Temperature': 32, 'pH': 6.7, 'Nutrient_Concentration': 1.2},
        {'Temperature': 30, 'pH': 6.5, 'Nutrient_Concentration': 1.0}
    ]
    future_predictions = microbial_processor.predict_future_yield(future_conditions)
    print("Future Predictions:")
    print(future_predictions)
