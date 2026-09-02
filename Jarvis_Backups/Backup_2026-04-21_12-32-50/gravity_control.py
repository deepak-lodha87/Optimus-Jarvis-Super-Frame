import time

class GravityEngine:
    def __init__(self):
        self.g_force = 9.8  # Standard Earth Gravity
        self.flight_status = "Grounded"

    def phase_2773(self):
        print("\033[1;33m>> INITIATING: [SYSTEM_ROOT_2773] - Graviton Emission Warp\033[0m")
        print("[LOG] Generating localized anti-graviton field around Deepak...")
        time.sleep(1.2)
        # Unique Logic: Reducing weight to zero
        self.g_force = 0.0
        print(f"[ACT] Gravity adjusted to: {self.g_force}G. Weightlessness achieved.")
        time.sleep(1.5)
        print("[RES] Internal stabilizers active. You are now floating.")

    def phase_2774(self):
        print("\n\033[1;34m>> INITIATING: [SYSTEM_ROOT_2774] - Vectorized Propulsion Control\033[0m")
        print("[LOG] Calculating flight trajectories using Earth's magnetic field...")
        time.sleep(1)
        
        # Unique Logic: Flying without engines
        self.flight_status = "ASCENDING"
        print(f"[ACT] Thrust-to-Weight Ratio: INFINITE. Flight Mode: {self.flight_status}")
        time.sleep(1.2)
        
        print("\n[RES] Takeoff successful. You are moving at Mach 5 with zero noise.")
        print("\033[1;32m>> STATUS: GRAVITY MANIPULATION FULLY ACTIVE\033[0m")

if __name__ == "__main__":
    gravity = GravityEngine()
    gravity.phase_2773()
    gravity.phase_2774()
