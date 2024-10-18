import random

class ResourceExtractor:
    def __init__(self):
        self.resources = {
            'water': 0,
            'oxygen': 0,
            'minerals': 0
        }

    def extract_resources(self):
        """
        Simulates the extraction of resources from lunar regolith.
        
        :return: Dictionary of extracted resources
        """
        self.resources['water'] = self.extract_water()
        self.resources['oxygen'] = self.extract_oxygen()
        self.resources['minerals'] = self.extract_minerals()
        return self.resources

    def extract_water(self):
        """
        Simulates water extraction from lunar regolith.
        
        :return: Amount of water extracted in liters
        """
        return random.randint(1, 10)  # Simulate extraction of 1 to 10 liters

    def extract_oxygen(self):
        """
        Simulates oxygen extraction from lunar regolith.
        
        :return: Amount of oxygen extracted in kilograms
        """
        return random.uniform(0.5, 2.0)  # Simulate extraction of 0.5 to 2 kg

    def extract_minerals(self):
        """
        Simulates mineral extraction from lunar regolith.
        
        :return: Amount of minerals extracted in kilograms
        """
        return random.randint(5, 20)  # Simulate extraction of 5 to 20 kg
