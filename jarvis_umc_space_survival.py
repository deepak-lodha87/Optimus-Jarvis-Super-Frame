import time
import random

class UniversalMachineController:
    def __init__(self):
        self.radiation_exposure = 0 # mSv
        self.shield_status = "STABLE"
        self.energy_mode = "MAX_POWER"

    def p3403_radiation_shield(self, cosmic_ray_level):
        if cosmic_ray_level > 50:
            self.shield_status = "LEAD_NANO_SHIELD_ACTIVE"
            return "\033[1;35m[DEFENSE] Cosmic Radiation detected. Activating Lead-Nano-Polymer shielding.\033[0m"
        return "[STATUS] Radiation levels within safe limits."

    def p3404_solar_flare_sync(self, flare_detected):
        if flare_detected:
            return "\033[1;31m[WARNING] Solar Flare Alert! Diverting power to Magnetic Deflector Shield.\033[0m"
        return "[STATUS] Solar activity normal."

    def p3405_deep_sleep_protocol(self, distance_km):
        if distance_km > 1000000:
            self.energy_mode = "ULTRA_LOW_HIBERNATION"
            return "\033[1;34m[ENERGY] Long Distance Detected. Entering Hibernation. Only Life-Support remains active.\033[0m"
        return "[STATUS] Energy mode: Operational."

    def p3406_meteoroid_defense(self):
        return "\033[1;32m[TACTICAL] Laser Defense System active. Vaporizing micro-meteoroids in flight path.\033[0m"

    def p3407_reentry_thermal_mgmt(self, surface_temp):
        if surface_temp > 1500:
            return "\033[1;33m[AERO] Atmosphere Re-entry. Deploying Ablative Heat Shield. Hull temp: STABLE.\033[0m"
        return "[STATUS] Surface temperature normal."

if __name__ == "__main__":
    umc = UniversalMachineController()
    print("-" * 60)
    print("   JARVIS UMC: SPACE SURVIVAL MODULE (P3503-3507)")
    print("-" * 60)
    
    print(umc.p3403_radiation_shield(75))
    print(umc.p3404_solar_flare_sync(True))
    print(umc.p3405_deep_sleep_protocol(2000000))
    print(umc.p3406_meteoroid_defense())
    print(umc.p3407_reentry_thermal_mgmt(2500))
    
    print("-" * 60)
    print("STATUS: Deep-Space Protocols Synced. Ready for Mission.")
    print("-" * 60)
