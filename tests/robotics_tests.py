import unittest
from robotics import NavigationSystem  # Assuming a NavigationSystem class exists

class TestNavigationSystem(unittest.TestCase):
    def setUp(self):
        self.navigation = NavigationSystem()

    def test_navigate_to(self):
        result = self.navigation.navigate_to((10, 10))
        self.assertIn("Arrived at", result)

    def test_calculate_distance(self):
        distance = self.navigation.calculate_distance((0, 0), (3, 4))
        self.assertEqual(distance, 5)

if __name__ == "__main__":
    unittest.main()
