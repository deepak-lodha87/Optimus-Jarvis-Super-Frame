import time
import random

class ThermalRegulator:
    def __init__(self):
        self.core_temp = 35.0 # Starting Celsius
        self.battery_drain = "OPTIMIZED"

    def monitor_vitals(self):
        print(f"\033[1;36m[THERMAL]\033[0m Activating Liquid Cooling Simulation...")
        time.sleep(1.5)
        
        for i in range(5):
            # Simulating load vs cooling
            self.core_temp += random.uniform(0.5, 1.5)
            cooling_active = "TRUE" if self.core_temp > 38 else "STANDBY"
            
            print(f" \033[1;32m[LOG]\033[0m Core Temp: {self.core_temp:.1f}°C | Cooling: {cooling_active}")
            
            if self.core_temp > 40:
                print(" \033[1;33m[ACTION]\033[0m Reducing Voltage to Core 1-4... Stabilizing.")
                self.core_temp -= 2.0
            time.sleep(0.6)
            
        print(f"\n\033[1;35m[VOICE] Deepak sir, the system is running cool. \nI have balanced the power-to-thermal ratio. \nYou can now perform heavy tasks without \nworrying about overheating.\033[0m")

if __name__ == "__main__":
    regulator = ThermalRegulator()
    regulator.monitor_vitals()
