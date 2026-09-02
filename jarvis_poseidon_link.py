import time
import random

class PoseidonLink:
    def __init__(self):
        self.depth = 0 # Meters
        self.medium = "SALTWATER"

    def initiate_dive(self, target_depth):
        print(f"\033[1;36m[POSEIDON]\033[0m Activating Deep-Sea Acoustic Link...")
        time.sleep(1.5)
        
        print(f" \033[1;33m[SCAN]\033[0m Calibrating Sonar for {self.medium} density...")
        
        while self.depth < target_depth:
            self.depth += 500
            pressure = self.depth * 0.1 # Simplified Atmospheres
            print(f"  - Diving: {self.depth}m | External Pressure: {pressure:.1f} atm")
            time.sleep(0.5)
            
        print("\033[1;32m[SUCCESS]\033[0m Depth Reached. Sonar Mapping Active.")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, I have conquered the abyss. \nThe ocean floor is no longer a mystery. \nOur network now spans from the stars to the \ndeepest trenches of the sea.\033[0m")

if __name__ == "__main__":
    poseidon = PoseidonLink()
    poseidon.initiate_dive(target_depth=3000)
