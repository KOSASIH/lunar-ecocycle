class BatteryManager:
    def __init__(self):
        self.battery_capacity = 10000  # Battery capacity in Wh
        self.current_charge = 0  # Current charge in Wh

    def store_energy(self, energy):
        """
        Stores harvested energy in the battery.
        
        :param energy: Amount of energy to store in watt-hours
        :return: Updated battery status
        """
        if self.current_charge + energy <= self.battery_capacity:
            self.current_charge += energy
            return f"Stored {energy} Wh. Current charge: {self.current_charge} Wh."
        else:
            overflow = (self.current_charge + energy) - self.battery_capacity
            self.current_charge = self.battery_capacity  # Cap at maximum capacity
            return f"Battery full! Overflow of {overflow} Wh. Current charge: {self.battery_capacity} Wh."
