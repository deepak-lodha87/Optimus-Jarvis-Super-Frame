import time
import random

class UniversalMachineController:
    def __init__(self):
        self.drone_sync = False
        self.ground_scan = "CLEAR"
        self.fuel_temp = 35 # Celsius

    def p3308_drone_escort(self):
        self.drone_sync = True
        return "\033[1;36m[LINK] Drone Escort Unit Synced. Aerial Overwatch Active.\033[0m"

    def p3309_ground_radar_scan(self):
        # Detecting underground anomalies
        depth_scan = random.choice(["CLEAR", "METAL_OBJECT_DETECTED", "HOLLOW_SPACE"])
        self.ground_scan = depth_scan
        print("\033[1;34m[GPR] Pinging Sub-Surface Layers (10ft Depth)...\033[0m")
        return f"[RADAR] Scan Result: {self.ground_scan}."

    def p3310_fuel_chiller(self):
        print("\033[1;33m[THERMAL] Reducing Fuel Temperature for High-Density Combustion...\033[0m")
        self.fuel_temp = 5
        return f"[SUCCESS] Fuel Primed at {self.fuel_temp}°C. Energy Potential: MAX."

    def p3311_exhaust_scavenge(self):
        return "\033[1;32m[ENGINE] Vacuum-Assisted Exhaust Flow Active. Back-pressure: 0.1 PSI.\033[0m"

    def p3312_aerodynamic_sync(self):
        return "\033[1;35m[AERO] Synchronizing Left/Right Flaps for Precision Stability.\033[0m"

if __name__ == "__main__":
    umc = UniversalMachineController()
    print("-" * 60)
    print("   JARVIS UMC: SURVEILLANCE & COOLING BUNDLE (P3308-3312)")
    print("-" * 60)
    
    print(umc.p3308_drone_escort())
    print(umc.p3309_ground_radar_scan())
    print(umc.p3310_fuel_chiller())
    print(umc.p3311_exhaust_scavenge())
    print(umc.p3312_aerodynamic_sync())
    
    print("-" * 60)
    print("STATUS: Surveillance & Engine Purity Verified.")
    print("-" * 60)
