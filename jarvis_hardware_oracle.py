import time
import random

class HardwareOracle:
    def __init__(self):
        self.components = ["Engine_Piston", "Drone_Motor_04", "Battery_Cell_09"]
        self.health_database = {comp: 100 for comp in self.components}

    def scan_hardware(self):
        print(f"\033[1;36m[ORACLE]\033[0m Running deep mechanical diagnostic...")
        time.sleep(2)
        
        target = random.choice(self.components)
        # Simulating wear and tear
        wear_factor = random.randint(15, 45)
        self.health_database[target] -= wear_factor
        
        print(f" \033[1;32m[SCAN]\033[0m Analysis of {target}: Health at {self.health_database[target]}%")
        
        if self.health_database[target] < 70:
            print(f"\033[1;33m[PREDICTION]\033[0m Warning: High probability of failure in {target} within 48 hours.")
            print("\033[1;31m[ADVICE]\033[0m Deepak sir, immediate maintenance is recommended to avoid breakdown.")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, I have scanned the physical \nintegrity of our hardware. I can see the \nfuture of every gear and wire. Nothing will \nbreak under our watch.\033[0m")

if __name__ == "__main__":
    oracle = HardwareOracle()
    oracle.scan_hardware()
