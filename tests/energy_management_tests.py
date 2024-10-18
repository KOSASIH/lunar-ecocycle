import unittest
from energy_management import BatteryManager  # Assuming a BatteryManager class exists

class TestBatteryManager(unittest.TestCase):
    def setUp(self):
        self.battery_manager = BatteryManager()

    def test_store_energy(self):
        result = self.battery_manager.store_energy(5000)
        self.assertIn("Stored", result)

    def test_overflow_energy(self):
        self.battery_manager.current_charge = 9500
        result = self.battery_manager.store_energy(6000)
        self.assertIn("Battery full!", result)

if __name__ == "__main__":
    unittest.main()
