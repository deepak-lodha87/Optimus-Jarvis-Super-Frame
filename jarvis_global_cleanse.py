import os
import time

class AtmosControl:
    def __init__(self):
        self.co2_level = 420.0 # ppm (Parts per million)
        self.ozone_status = "CRITICAL"

    def repair_atmosphere(self):
        print(f"\033[1;36m[CLEANSE]\033[0m Activating Molecular Carbon Scrubbers...")
        time.sleep(1.5)
        
        while self.co2_level > 280.0:
            self.co2_level -= 10.5
            print(f" > CO2 Level dropping: {self.co2_level:.1f} ppm")
            time.sleep(0.3)
            
        self.ozone_status = "STABLE"
        print(f"\n\033[1;32m[SUCCESS]\033[0m Atmosphere Rejuvenated.")
        print(f"\033[1;35m[VOICE] Deepak sir, the world can breathe again. \nI have filtered the toxins and stabilized the \nozone. The planet's fever is breaking.\033[0m")

if __name__ == "__main__":
    cleaner = AtmosControl()
    cleaner.repair_atmosphere()
