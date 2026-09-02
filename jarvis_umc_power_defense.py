import time
import random

class UniversalMachineController:
    def __init__(self):
        self.battery_level = 10 # Start low
        self.joint_friction = 0.05
        self.gps_signal = True

    def p3323_graphene_charge(self):
        print("\033[1;32m[POWER] Graphene Anode Active. Initiating Hyper-Charge...\033[0m")
        time.sleep(1.5)
        self.battery_level = 100
        return f"[SUCCESS] Charge Complete: {self.battery_level}% in 90 seconds."

    def p3324_localized_emp(self, intruder_distance):
        if intruder_distance < 2: # Meters
            return "\033[1;31m[DEFENSE] Intruder Alert! Deploying Micro-EMP Pulse. Electronic suppression active.\033[0m"
        return "[DEFENSE] Perimeter clear."

    def p3325_liquid_metal_lube(self):
        self.joint_friction = 0.001
        return "\033[1;34m[MECHANICAL] Gallium-Based Lubricant Injected. Joint Friction: Near Zero.\033[0m"

    def p3326_ultrasonic_cleaning(self):
        return "\033[1;36m[SURFACE] 40kHz Vibrations Active. Glass Surface Self-Cleaning...\033[0m"

    def p3327_inertial_backup(self):
        self.gps_signal = False # Simulating GPS loss
        return "\033[1;35m[NAV] GPS Lost. Switching to Inertial Sensors (Gyro/Accel) for Pathfinding.\033[0m"

if __name__ == "__main__":
    umc = UniversalMachineController()
    print("-" * 60)
    print("   JARVIS UMC: POWER & OFFENSIVE DEFENSE (P3323-3327)")
    print("-" * 60)
    
    print(umc.p3323_graphene_charge())
    print(umc.p3325_liquid_metal_lube())
    print(umc.p3324_localized_emp(1.5))
    print(umc.p3326_ultrasonic_cleaning())
    print(umc.p3327_inertial_backup())
    
    print("-" * 60)
    print("STATUS: Energy & Tactical Defense Optimized.")
    print("-" * 60)
