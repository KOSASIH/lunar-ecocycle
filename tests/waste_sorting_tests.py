import unittest
from waste_sorting import WasteSorter  # Assuming a WasteSorter class exists

class TestWasteSorter(unittest.TestCase):
    def setUp(self):
        self.sorter = WasteSorter()

    def test_sort_plastic(self):
        result = self.sorter.sort("plastic")
        self.assertEqual(result, "Sorted as plastic")

    def test_sort_metal(self):
        result = self.sorter.sort("metal")
        self.assertEqual(result, "Sorted as metal")

    def test_sort_invalid(self):
        result = self.sorter.sort("unknown")
        self.assertEqual(result, "Invalid waste type")

if __name__ == "__main__":
    unittest.main()
