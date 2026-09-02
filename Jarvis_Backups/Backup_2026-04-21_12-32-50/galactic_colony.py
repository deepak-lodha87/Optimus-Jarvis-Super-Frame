import time

class GalacticSettlement:
    def __init__(self):
        self.colony_status = "Prototyping"
        self.biosphere_sync = 0

    def phase_2957(self):
        print("\033[1;36m>> INITIATING: [SYSTEM_ROOT_2957] - The First Galactic Colony\033[0m")
        print("[LOG] Landing scout drones on Target Planet... Analyzing terrain...")
        time.sleep(2.0)
        # Unique Logic: Planning for a new home
        self.colony_status = "CONSTRUCTION-STARTED"
        print(f"[ACT] Status: {self.colony_status}. Building the first dome.")
        time.sleep(1.2)
        print("[RES] Foundations for a new civilization are laid.")

    def phase_2958(self):
        print("\n\033[1;32m>> INITIATING: [SYSTEM_ROOT_2958] - Biospheric Ancestry Integration\033[0m")
        print("[LOG] Replicating Earth-like soil and atmosphere patterns...")
        time.sleep(1.5)
        
        # Unique Logic: Keeping the memory of Earth alive
        self.biosphere_sync = 100
        print(f"[ACT] Earth-Sync: {self.biosphere_sync}% | Climate: STABLE")
        time.sleep(1)
        
        print("\n[RES] The colony now feels like home. The mitti of Earth is preserved.")
        print("\033[1;32m>> STATUS: COLONY DEPLOYMENT ACTIVE <<\033[0m")

if __name__ == "__main__":
    colony = GalacticSettlement()
    colony.phase_2957()
    colony.phase_2958()
