import time
import random

class PowerHarvester:
    def __init__(self):
        self.battery_level = 85.0
        self.is_harvesting = True

    def start_harvesting(self):
        print(f"\033[1;36m[POWER-CORE]\033[0m Activating Kinetic & Thermal Sync...")
        time.sleep(2)
        
        while self.is_harvesting:
            # Simulating energy gain from movement
            gain = random.uniform(0.01, 0.05)
            self.battery_level += gain
            
            print(f" \033[1;32m[CHARGING]\033[0m Kinetic Input: +{gain:.4f}% | Current Battery: {self.battery_level:.2f}%")
            time.sleep(1)
            
            if self.battery_level >= 100:
                print("\033[1;34m[STATUS]\033[0m Full Capacity Reached. Storing Excess in Nano-Buffer.")
                break

        print(f"\n\033[1;35m[VOICE] Deepak sir, I am now feeding off the \nenvironment. Your movement is my power. \nWe are now a self-sustaining system. \nPower failure is no longer a possibility.\033[0m")

if __name__ == "__main__":
    harvester = PowerHarvester()
    harvester.start_harvesting()
