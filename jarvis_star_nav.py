import time
import random

class StarNavigator:
    def __init__(self):
        self.catalog_stars = 1000000000 # 1 Billion Stars
        self.location_mode = "CELESTIAL"

    def get_stellar_fix(self):
        print(f"\033[1;36m[NAV]\033[0m Scanning Celestial Sphere for Pulsar Beacons...")
        time.sleep(2)
        
        pulsars = ["PSR B1919+21", "Crab Pulsar", "Vela Pulsar"]
        for p in pulsars:
            sync_accuracy = random.uniform(99.99, 99.999)
            print(f" \033[1;32m[LOCKED]\033[0m {p:15} | Sync: {sync_accuracy}%")
            time.sleep(0.5)
            
        print("\033[1;34m[STATUS]\033[0m Position established in Galactic Sector 001.")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, the stars are now our guide. \nEven if the world goes dark, I can find our \nway using the heartbeat of the universe. \nWe are never lost.\033[0m")

if __name__ == "__main__":
    nav = StarNavigator()
    nav.get_stellar_fix()
