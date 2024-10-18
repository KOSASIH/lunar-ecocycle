import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class PredictiveModel:
    def __init__(self):
        self.data = pd.read_csv("data.csv")  # Load data from CSV file
        self.X = self.data.drop("target", axis=1)  # Features
        self.y = self.data["target"]  # Target variable

    def train_model(self):
        """
        Trains a predictive model using a random forest classifier.
        """
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Model accuracy: {accuracy:.2f}")
