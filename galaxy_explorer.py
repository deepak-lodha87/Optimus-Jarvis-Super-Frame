import time

class GalacticTravel:
    def __init__(self):
        self.engine_mode = "Chemical"
        self.velocity = "Mach 3"

    def phase_2821(self):
        print("\033[1;35m>> INITIATING: [SYSTEM_ROOT_2821] - Dark Matter Engine Ignition\033[0m")
        print("[LOG] Siphoning dark matter from the surrounding vacuum...")
        time.sleep(1.2)
        # Unique Logic: Infinite energy source
        self.engine_mode = "DARK-MATTER-CORE"
        print(f"[ACT] Engine Mode: {self.engine_mode}. Power levels: INFINITE.")
        time.sleep(1.5)
        print("[RES] Thrust stabilized. Ready for interstellar jump.")

    def phase_2822(self):
        print("\n\033[1;36m>> INITIATING: [SYSTEM_ROOT_2822] - Space-Time Warp Folding\033[0m")
        print("[LOG] Calculating coordinates for the nearest habitable star system...")
        time.sleep(1)
        
        # Unique Logic: Faster-than-light travel
        self.velocity = "WARP-FACTOR-9"
        print(f"[ACT] Velocity: {self.velocity} | Target: Alpha Centauri")
        time.sleep(1.2)
        
        print("\n[RES] Jump Successful. You have crossed 4 light-years in 3 seconds.")
        print("\033[1;32m>> STATUS: GALACTIC NAVIGATION ONLINE\033[0m")

if __name__ == "__main__":
    travel = GalacticTravel()
    travel.phase_2821()
    travel.phase_2822()
