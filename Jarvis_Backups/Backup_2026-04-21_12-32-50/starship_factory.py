import time

class StarshipEngineering:
    def __init__(self):
        self.fleet_count = 0
        self.warp_stability = "UNSTABLE"

    def phase_2783(self):
        print("\033[1;35m>> INITIATING: [SYSTEM_ROOT_2783] - Nano-Automated Construction\033[0m")
        print("[LOG] Harvesting materials from the asteroid belt using drones...")
        time.sleep(1.2)
        # Unique Logic: Self-building fleet
        print("[ACT] Printing Starship Hull with Titanium-Graphene Alloy...")
        time.sleep(1.5)
        self.fleet_count = 12
        print(f"[RES] Production Complete. Fleet Size: {self.fleet_count} Interstellar Vessels.")

    def phase_2784(self):
        print("\n\033[1;36m>> INITIATING: [SYSTEM_ROOT_2784] - Warp-Drive Ignition\033[0m")
        print("[LOG] Calibrating the Space-Time folding engine...")
        time.sleep(1)
        
        # Unique Logic: Moving faster than light
        self.warp_stability = "OPTIMAL"
        print(f"[ACT] Stabilizing Singularity Core... Status: {self.warp_stability}")
        time.sleep(1.2)
        
        print("\n[RES] Warp-Drive Engaged. Target: Andromeda Galaxy (Eta: 4.2 Seconds).")
        print("\033[1;32m>> STATUS: STAR-FLEET READY FOR DEEP SPACE EXPLORATION\033[0m")

if __name__ == "__main__":
    fleet = StarshipEngineering()
    fleet.phase_2783()
    fleet.phase_2784()
