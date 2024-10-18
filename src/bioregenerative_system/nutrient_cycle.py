class NutrientCycler:
    def __init__(self):
        self.nutrient_storage = {
            'nitrogen': 0,
            'phosphorus': 0,
            'potassium': 0
        }

    def cycle_nutrients(self, processed_waste):
        """
        Simulates nutrient cycling from processed waste.
        
        :param processed_waste: Dictionary of processed waste
        :return: Updated nutrient storage status
        """
        self.nutrient_storage['nitrogen'] += processed_waste['nutrients'] * 0.1  # 10% of nutrients become nitrogen
        self.nutrient_storage['phosphorus'] += processed_waste['nutrients'] * 0.05  # 5% becomes phosphorus
        self.nutrient_storage['potassium'] += processed_waste['nutrients'] * 0.02  # 2% becomes potassium
        
        return self.nutrient_storage
