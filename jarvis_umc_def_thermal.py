import time
import random

class UniversalMachineController:
    def __init__(self):
        self.shield_status = "READY"
        self.battery_temp = 35 # Celsius
        self.hull_integrity = 100 # %

    def p3393_collision_shield(self, object_dist):
        if object_dist < 2:
            self.shield_status = "ACTIVE"
            return "\033[1;31m[DEFENSE] Imminent Collision! Deploying Electromagnetic Pulse Shield.\033[0m"
        return "[STATUS] Perimeter clear."

    def p3394_cryo_cooling(self):
        if self.battery_temp > 45:
            self.battery_temp = 20
            return "\033[1;36m[THERMAL] Battery Overheat! Injecting Cryogenic Coolant. Temp Stabilized.\033[0m"
        return "[STATUS] Battery temperature optimal."

    def p3395_pressure_comp(self, altitude_m):
        if altitude_m > 2500:
            return f"\033[1;33m[ALTITUDE] High Altitude Detected ({altitude_m}m). Adjusting Turbo-Pressure.\033[0m"
        return "[STATUS] Standard Atmospheric Pressure."

    def p3396_hull_auto_repair(self, impact_detected):
        if impact_detected:
            self.hull_integrity = 100
            return "\033[1;32m[REPAIR] Hull Breach Detected! Deploying Nano-Sealant Paste. Integrity Restored.\033[0m"
        return "[STATUS] Structural integrity 100%."

    def p3397_inertial_nav(self):
        return "\033[1;35m[NAV] GPS Signal Lost. Switching to Internal Gyroscope & Accelerometer Tracking.\033[0m"

if __name__ == "__main__":
    umc = UniversalMachineController()
    print("-" * 60)
    print("   JARVIS UMC: DEFENSE & THERMAL MASTERY (P3393-3397)")
    print("-" * 60)
    
    print(umc.p3393_collision_shield(1.5))
    print(umc.p3394_cryo_cooling())
    print(umc.p3395_pressure_comp(3500))
    print(umc.p3396_hull_auto_repair(True))
    print(umc.p3397_inertial_nav())
    
    print("-" * 60)
    print("STATUS: Tactical Survival & Thermal Protocols Synced.")
    print("-" * 60)
