import time
import random

class MirageEngine:
    def __init__(self):
        self.active_clones = 0
        self.camouflage_status = "OFFLINE"

    def activate_mirage(self, clone_count):
        print(f"\033[1;36m[MIRAGE]\033[0m Scanning ambient light conditions...")
        time.sleep(1.5)
        
        self.active_clones = clone_count
        self.camouflage_status = "ACTIVE"
        
        print(f" \033[1;32m[SUCCESS]\033[0m Projecting {self.active_clones} Decoys.")
        print(f" \033[1;34m[STATUS]\033[0m Refraction Field: 100% Stability.")
        
        for i in range(1, clone_count + 1):
            print(f" > Ghost Node {i}: Positioned at Vector {random.randint(10,99)}°")
            time.sleep(0.3)
            
        print(f"\n\033[1;35m[VOICE] Deepak sir, the Mirage Protocol is engaged. \nI have populated the area with holographic \ndecoys. To the enemy, you are everywhere \nand nowhere at the same time.\033[0m")

if __name__ == "__main__":
    mirage = MirageEngine()
    mirage.activate_mirage(5)
