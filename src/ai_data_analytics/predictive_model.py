# predictive_model.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

class PredictiveModel:
    def __init__(self, historical_data):
        self.historical_data = historical_data
        self.model = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

    def prepare_data(self):
        """Prepare the data for training and testing."""
        X = self.historical_data[['Year']]
        y = self.historical_data['Recycled Quantity']
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
        plt.xlabel('Actual Recycled Quantity (kg)')
        plt.ylabel('Predicted Recycled Quantity (kg)')
        plt.title('Predicted vs Actual Recycling Quantity')
        plt.legend()
        plt.tight_layout()
        plt.show()

    def predict_future(self, future_years):
        """Predict recycling quantities for future years."""
        future_data = pd.DataFrame({'Year': future_years})
        future_predictions = self.model.predict(future_data)
        return future_data.assign(Predicted_Recycled_Quantity=future_predictions)

# Example usage
if __name__ == "__main__":
    # Sample historical data
    historical_data = pd.DataFrame({
        'Year': [2018, 2019, 2020, 2021, 2022],
        'Recycled Quantity': [800, 850, 900, 950, 1000]
    })

    # Create a PredictiveModel instance
    predictive_model = PredictiveModel(historical_data)

    # Prepare data
    predictive_model.prepare_data()

    # Train the model
    predictive_model.train_model()

    # Evaluate the model
    predictive_model.evaluate_model()

    # Predict future recycling quantities for the next 5 years
    future_years = list(range(2023, 2028))
    future_predictions = predictive_model.predict_future(future_years)
    print("Future Predictions:")
    print(future_predictions)
