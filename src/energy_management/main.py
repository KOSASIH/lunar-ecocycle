import logging
from solar_panel_control import SolarPanelController
from battery_management import BatteryManager

def main():
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    
    # Initialize solar panel controller
    solar_panel_controller = SolarPanelController()
    
    # Harvest energy from solar panels
    energy_harvested = solar_panel_controller.harvest_energy()
    logging.info(f"Energy harvested: {energy_harvested} Wh")
    
    # Initialize battery manager
    battery_manager = BatteryManager()
    
    # Store harvested energy in the battery
    battery_status = battery_manager.store_energy(energy_harvested)
    logging.info(f"Battery status: {battery_status}")

if __name__ == "__main__":
    main()
