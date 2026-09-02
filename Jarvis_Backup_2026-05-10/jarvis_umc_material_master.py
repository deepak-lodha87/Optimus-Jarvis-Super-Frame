import time
import random

class UniversalMachineController:
    def __init__(self):
        self.circuit_integrity = 100
        self.visibility_index = 100 # Lower is better
        self.external_ice_layer = 0 # mm

    def p3273_liquid_metal_repair(self):
        # Simulating a circuit break
        self.circuit_integrity = 85
        print("\033[1;31m[CIRCUIT] Break detected in Node-B4. Deploying Gallium Alloy...\033[0m")
        time.sleep(1.2)
        self.circuit_integrity = 100
        return "\033[1;32m[SUCCESS] Connection Restored via Autonomous Rewiring.\033[0m"

    def p3274_optical_camo_v2(self):
        self.visibility_index = 2
        return "\033[1;36m[CAMO] High-Def Projectors Synced. Active Transparency Engaged.\033[0m"

    def p3275_hydro_braking_logic(self, medium):
        if medium == "WATER":
            print("\033[1;34m[BRAKE] Water Detected. Opening High-Drag Flaps...\033[0m")
            return "[STATUS] Kinetic Energy Absorbed by Fluid Resistance. Deceleration Optimal."
        return "[BRAKE] Standard Braking Active."

    def p3276_nano_air_filter(self):
        return "\033[1;35m[BIO] Nano-Lattice Filter Active. Blocking 99.9% Toxins.\033[0m"

    def p3277_ultrasonic_deice(self):
        self.external_ice_layer = 15 # Simulated ice
        print(f"\033[1;33m[DE-ICE] Ice Detected: {self.external_ice_layer}mm. Activating Ultrasonic Pulse...\033[0m")
        time.sleep(0.8)
        self.external_ice_layer = 0
        return "[SUCCESS] Ice Layer Shattered and Removed."

if __name__ == "__main__":
    umc = UniversalMachineController()
    print("-" * 60)
    print("   JARVIS UMC: MATERIAL & FLUID MASTERY (P3273-3277)")
    print("-" * 60)
    
    print(umc.p3273_liquid_metal_repair())
    print(umc.p3274_optical_camo_v2())
    print(umc.p3275_hydro_braking_logic("WATER"))
    print(umc.p3276_nano_air_filter())
    print(umc.p3277_ultrasonic_deice())
    
    print("-" * 60)
    print("STATUS: Molecular & Terrain Optimization Complete.")
    print("-" * 60)
