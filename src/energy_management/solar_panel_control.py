import random

class SolarPanelController:
    def __init__(self):
        self.efficiency = 0.18  # 18% efficiency for solar panels

    def harvest_energy(self):
        """
        Simulates energy harvesting from solar panels.
        
        :return: Amount of energy harvested in watt-hours
        """
        sunlight_hours = random.uniform(4, 8)  # Simulate 4 to 8 hours of sunlight
        energy_harvested = sunlight_hours * 1000 * self.efficiency  # 1000 W panel
        return round(energy_harvested, 2)  # Return energy in Wh
