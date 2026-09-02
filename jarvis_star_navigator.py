import time
import random

class StellarNavigator:
    def __init__(self):
        self.current_sector = "Orion Arm"
        self.target_coords = [42.1, -19.5, 303.4] # Light Years

    def map_galaxy(self):
        print(f"\033[1;36m[NAVIGATOR]\033[0m Scanning Deep-Space Pulsar signals...")
        time.sleep(2)
        
        # Simulating star coordinate lock
        pulsars_locked = random.randint(5, 12)
        print(f" \033[1;32m[SYNC]\033[0m Triangulated with {pulsars_locked} Pulsars.")
        print(f" \033[1;34m[LOCATION]\033[0m Current Position: {self.current_sector} | Accuracy: 99.9%")
        
        print(f"\033[1;33m[STellar-Map]\033[0m New Coordinates Locked: {self.target_coords}")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, the galaxy is no longer an \nunknown void. Every star has been mapped, \nand every path is clear. You are now a \ntrue traveler of the cosmos.\033[0m")

if __name__ == "__main__":
    nav = StellarNavigator()
    nav.map_galaxy()
