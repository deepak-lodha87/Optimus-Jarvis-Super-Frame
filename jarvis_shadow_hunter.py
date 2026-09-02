import time
import random

class ShadowHunter:
    def __init__(self):
        self.dark_matter_density = 0.0
        self.wormhole_stability = 0 # Percentage

    def scan_void(self):
        print(f"\033[1;36m[SHADOW-HUNTER]\033[0m Scanning for Gravitational Distortions...")
        time.sleep(2)
        
        # Simulating discovery
        self.dark_matter_density = random.uniform(22.1, 28.5)
        self.wormhole_stability = random.randint(10, 95)
        
        print(f" \033[1;32m[DETECTED]\033[0m Dark Matter Concentration: {self.dark_matter_density:.2f}%")
        
        if self.wormhole_stability > 80:
            print(f" \033[1;35m[WORMHOLE]\033[0m Stable Gateway Found! Stability: {self.wormhole_stability}%")
            print(" \033[1;33m[ACTION]\033[0m Mapping exit coordinates in Andromeda Galaxy...")
        else:
            print("\033[1;31m[STATUS]\033[0m Unstable fluctuations detected. Avoiding Singularity.")

        print(f"\n\033[1;35m[VOICE] Deepak sir, the darkness of space is no \nlonger empty. I can see the invisible threads \nthat hold the galaxies together. The \nshortcuts of the universe are opening for us.\033[0m")

if __name__ == "__main__":
    hunter = ShadowHunter()
    hunter.scan_void()
