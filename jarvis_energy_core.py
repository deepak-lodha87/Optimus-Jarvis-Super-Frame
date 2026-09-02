import time
import random

class OptimusJarvis:
    def __init__(self):
        self.user = "Sir"
        self.core_temp = 32.5

    def phase_1516_energy_core_management(self):
        print("\n--- [ PHASE 1516: ENERGY CORE MANAGEMENT ] ---")
        print(">> Monitoring Power Distribution Levels...")
        time.sleep(0.6)
        efficiency = random.randint(94, 98)
        print(f">> Core Efficiency: {efficiency}% | Temperature: {self.core_temp}°C")
        print(">> Status: Power flow is optimized for long-range operations.")

    def phase_1517_atmospheric_calibration(self):
        print("\n--- [ PHASE 1517: ATMOSPHERIC SENSOR CALIBRATION ] ---")
        print(">> Calibrating Barometric and Humidity Sensors...")
        time.sleep(0.5)
        altitude_limit = 35000 
        print(f">> Optimal Flight Ceiling: {altitude_limit} feet.")
        print(">> Status: Sensors adjusted for current environmental density.")

    def initialize_systems(self):
        print(f"--- [ OPTIMUS JARVIS: POWER & ENVIRONMENT ] ---")
        self.phase_1516_energy_core_management()
        self.phase_1517_atmospheric_calibration()
        print("-" * 55)
        print(f">> {self.user}, energy levels are stable and sensors are pinpoint accurate.")

if __name__ == "__main__":
    jarvis = OptimusJarvis()
    jarvis.initialize_systems()
