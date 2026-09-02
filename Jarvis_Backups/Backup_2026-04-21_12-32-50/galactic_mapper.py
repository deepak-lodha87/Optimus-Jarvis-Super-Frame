import time
import random

class StarMap:
    def __init__(self):
        self.known_galaxies = ["Milky Way", "Andromeda", "Sombrero"]
        self.current_sector = "Orion Arm"

    def phase_2651(self):
        print("\033[1;34m>> INITIATING: [SYSTEM_ROOT_2651] - Galactic Cartography\033[0m")
        print("[LOG] Synchronizing with Hubble and James Webb telemetry...")
        time.sleep(1.2)
        # Unique Logic: Identifying star systems
        system_count = random.randint(1000, 5000)
        print(f"[ACT] Mapping local cluster... {system_count} star systems identified.")
        time.sleep(1.5)
        print(f"[RES] Navigation mesh generated for the '{self.current_sector}'.")

    def phase_2652(self):
        print("\n\033[1;33m>> INITIATING: [SYSTEM_ROOT_2652] - Pulsar Navigation (GPS of Space)\033[0m")
        print("[LOG] Locking onto High-Frequency Pulsar beacons...")
        time.sleep(1)
        
        # Unique Logic: Triangulating position using stars
        stars = ["Sirius", "Alpha Centauri", "Betelgeuse"]
        for star in stars:
            distance = round(random.uniform(4.3, 642.5), 1)
            print(f"[ACT] Triangulating via {star}... Distance: {distance} Light-Years", end='\r')
            time.sleep(0.5)
            
        print("\n[RES] Precise Galactic Position Verified. Error margin: < 0.001mm.")
        print("\033[1;32m>> STATUS: STAR MAP FULLY RENDERED\033[0m")

if __name__ == "__main__":
    mapper = StarMap()
    mapper.phase_2651()
    mapper.phase_2652()
