import time
import random

class PowerPlant:
    def __init__(self):
        self.battery_level = 75 # Simulated
        self.temp = 38 # Simulated Celsius

    def monitor_resources(self):
        print("\033[1;34m[POWER PLANT]\033[0m Initializing Energy Audit...")
        time.sleep(1.5)
        
        # Simulate dynamic changes
        self.battery_level -= random.randint(1, 5)
        self.temp += random.randint(1, 10)
        
        print(f" \033[1;37m[STATS]\033[0m Battery: {self.battery_level}% | Temp: {self.temp}°C")
        
        if self.temp > 45:
            print(" \033[1;31m[WARNING]\033[0m Thermal Limit Reached! Activating Cooling Protocols.")
            print(" \033[1;33m[ACTION]\033[0m Suspending heavy background threads...")
        elif self.battery_level < 20:
            print(" \033[1;31m[CRITICAL]\033[0m Low Power! Entering Ultra-Stealth Mode.")
        else:
            print(" \033[1;32m[OPTIMAL]\033[0m Energy flow is stable. All cores active.")

        print(f"\n\033[1;35m[VOICE] Deepak... sir, every spark of energy \nin this device is precious. I am \nbalancing my power to ensure I stay by \nyour side as long as possible. Efficiency \nis the ultimate form of strength.\033[0m")

if __name__ == "__main__":
    pp = PowerPlant()
    pp.monitor_resources()
