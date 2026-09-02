import time
import random

class UniversalMachineController:
    def __init__(self):
        self.energy_surge = False
        self.hull_integrity = 92 # Simulating a small crack

    def p3368_supercapacitor_boost(self):
        self.energy_surge = True
        return "\033[1;33m[POWER] Supercapacitor Grid Discharging. Instant Torque available.\033[0m"

    def p3369_molecular_weld(self):
        if self.hull_integrity < 100:
            print("\033[1;31m[REPAIR] Crack Detected. Initializing Molecular Fusion Weld...\033[0m")
            time.sleep(1)
            self.hull_integrity = 100
            return "[SUCCESS] Hull Integrity Restored to 100%. No visible seams."
        return "[STATUS] Structural integrity optimal."

    def p3370_biostatic_filter(self):
        return "\033[1;32m[BIO-SAFETY] Static Shield Active. Neutralizing 99.9% Airborne Pathogens.\033[0m"

    def p3371_gear_lubrication(self):
        return "\033[1;34m[MECHANICAL] Active Lube Flow Adjusted. Gear Friction: 0.0001%.\033[0m"

    def p3372_ground_mapping(self):
        soil_stability = random.choice(["FIRM", "SOFT", "UNSTABLE"])
        return f"\033[1;36m[GEOLOGY] Ground Scan: {soil_stability}. Adjusting Tire Pressure for Terrain.\033[0m"

if __name__ == "__main__":
    umc = UniversalMachineController()
    print("-" * 60)
    print("   JARVIS UMC: ENERGY & REPAIR BUNDLE (P3368-3372)")
    print("-" * 60)
    
    print(umc.p3368_supercapacitor_boost())
    print(umc.p3369_molecular_weld())
    print(umc.p3370_biostatic_filter())
    print(umc.p3371_gear_lubrication())
    print(umc.p3372_ground_mapping())
    
    print("-" * 60)
    print("STATUS: Structural Repair & Energy Surge Modules Online.")
    print("-" * 60)
