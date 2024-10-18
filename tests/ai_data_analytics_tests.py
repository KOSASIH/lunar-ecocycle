import unittest
from predictive_model import PredictiveModel  # Assuming a PredictiveModel class exists

class TestPredictiveModel(unittest.TestCase):
    def setUp(self):
        self.model = PredictiveModel()

    def test_train_model(self):
        result = self.model.train_model()
        self.assertIn("Model trained", result)

    def test_make_prediction(self):
        result = self.model.make_prediction([1, 2, 3])
        self.assertIsInstance(result, float)

if __name__ == "__main__":
    unittest.main()
