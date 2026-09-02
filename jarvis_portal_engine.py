import time
import math
import random

class PortalStabilizer:
    def __init__(self, target_coord):
        self.target_coord = target_coord
        self.stability_index = 0.0
        self.is_active = False
        self.energy_draw = 0.0 # Measured in Exajoules

    def calculate_warp_field(self):
        """Calculates the curvature needed for the portal"""
        print(f"\033[1;34m[MATH]\033[0m Computing Riemann curvature tensor for {self.target_coord}...")
        # Complex logic simulation
        for i in range(1, 6):
            self.stability_index += random.uniform(10.5, 19.5)
            print(f" > Analyzing Space-Time Fabric: {self.stability_index:.2f}% Synced")
            time.sleep(0.4)

    def engage_anchors(self):
        """Prevents the portal from drifting in space"""
        if self.stability_index > 75.0:
            print("\033[1;32m[ANCHOR]\033[0m Locking Spatial Coordinates...")
            time.sleep(1)
            self.is_active = True
        else:
            print("\033[1;31m[ERROR]\033[0m Stability too low to anchor.")

    def run_portal_diagnostics(self):
        """Real-time monitoring of the gateway"""
        print("-" * 40)
        print(f"PORTAL STATUS: {'\033[1;32mSTABLE\033[0m' if self.is_active else '\033[1;31mUNSTABLE\033[0m'}")
        print(f"TARGET: {self.target_coord}")
        print(f"FLUX VARIANCE: {random.uniform(0.001, 0.005)}% (Optimal)")
        print("-" * 40)

def main():
    print(f"\033[1;35m[VOICE] Deepak sir, initiating Phase 200,006. \nPreparing to tear the fabric of reality safely.\033[0m")
    
    # Initialize engine for a specific star system
    engine = PortalStabilizer(target_coord="Andromeda-Sector-7G")
    
    engine.calculate_warp_field()
    engine.engage_anchors()
    
    if engine.is_active:
        engine.run_portal_diagnostics()
        print(f"\n\033[1;32m[GATEWAY OPEN]\033[0m You may proceed, sir.")

if __name__ == "__main__":
    main()
