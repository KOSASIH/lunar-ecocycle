class WaterRecoverySystem:
    def __init__(self):
        self.purification_efficiency = 0.9  # 90% purification efficiency

    def recover_and_purify_water(self, raw_water):
        """
        Simulates the recovery and purification of water.
        
        :param raw_water: Amount of raw water in liters
        :return: Amount of purified water in liters
        """
        if raw_water <= 0:
            raise ValueError("No raw water available for purification.")
        
        purified_water = raw_water * self.purification_efficiency
        return purified_water
