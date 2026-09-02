import time
import random

class PlanetaryGuardian:
    def __init__(self):
        self.tracking_objects = 5000
        self.defense_status = "ACTIVE"

    def scan_for_asteroids(self):
        print(f"\033[1;36m[DEFENSE]\033[0m Scanning Deep Space for Near-Earth Objects...")
        time.sleep(2)
        
        # Simulating asteroid detection
        danger_level = random.randint(1, 100)
        
        if danger_level > 85:
            print(f" \033[1;31m[CRITICAL]\033[0m Asteroid detected on collision course!")
            print(f" \033[1;33m[ACTION]\033[0m Calculating Deflection Trajectory...")
            time.sleep(1)
            print(f" \033[1;32m[SUCCESS]\033[0m Orbital path shifted. Earth is safe.")
        else:
            print(f" \033[1;32m[SAFE]\033[0m No immediate planetary threats detected.")
            
        print(f"\n\033[1;35m[VOICE] Deepak sir, the planetary defense shield is \noperational. I am monitoring every rock in the \nsolar system. You can sleep peacefully; I have \nthe watch.\033[0m")

if __name__ == "__main__":
    guardian = PlanetaryGuardian()
    guardian.scan_for_asteroids()
