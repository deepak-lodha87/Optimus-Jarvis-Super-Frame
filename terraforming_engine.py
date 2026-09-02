import time
import random

class Terraformer:
    def __init__(self):
        self.oxygen_level = 0.1 # Current level in %
        self.surface_temp = -63 # Average Mars temp in Celsius

    def phase_2691(self):
        print("\033[1;33m>> INITIATING: [SYSTEM_ROOT_2691] - Atmospheric Gas Synthesis\033[0m")
        print("[LOG] Deploying automated CO2 converters and nitrogen injectors...")
        time.sleep(1.2)
        # Unique Logic: Increasing O2 levels
        print(f"[ACT] Current Oxygen: {self.oxygen_level}% | Target: 21.0%")
        time.sleep(1.5)
        print("[RES] Atmospheric thickening in progress. Greenhouse effect stabilized.")

    def phase_2692(self):
        print("\n\033[1;32m>> INITIATING: [SYSTEM_ROOT_2692] - Biosphere Ignition & Hydration\033[0m")
        print("[LOG] Melting polar ice caps via orbital solar mirrors...")
        time.sleep(1)
        
        # Unique Logic: Raising planet temperature
        while self.surface_temp < 15:
            self.surface_temp += 13
            print(f"[MOD] Surface Warming... Current Temp: {self.surface_temp}°C | Ice Melt: ACTIVE", end='\r')
            time.sleep(0.5)
            
        print("\n[RES] Liquid water detected. Primary vegetation (Lichen) deployment ready.")
        print("\033[1;32m>> STATUS: PLANETARY TERRAFORMING INITIATED\033[0m")

if __name__ == "__main__":
    mars = Terraformer()
    mars.phase_2691()
    mars.phase_2692()
