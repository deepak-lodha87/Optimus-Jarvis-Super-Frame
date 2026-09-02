import time
import random

class UniversalMachineController:
    def __init__(self):
        self.engine_temp = 20 # Celsius
        self.exhaust_mode = "STEALTH"
        self.plasma_active = False

    def p3453_liquid_nitro_cool(self, load_percentage):
        if load_percentage > 90:
            self.engine_temp = -50
            return "\033[1;36m[COOLING] Peak Load Detected. Injecting Liquid Nitrogen. Temp Stabilized at -50°C.\033[0m"
        return "[STATUS] Engine temperature optimal."

    def p3454_plasma_cutter(self):
        self.plasma_active = True
        return "\033[1;31m[TOOLS] Plasma Torch Initialized. Ready for sub-atomic cutting operations.\033[0m"

    def p3455_resource_scanner(self):
        resources = ["Water", "Iron", "Gold", "None"]
        found = random.choice(resources)
        return f"\033[1;32m[SCAN] Sub-Surface Pulse Sent. Detection: {found} found at 15 meters.\033[0m"

    def p3456_air_ionizer(self, air_pollution_level):
        if air_pollution_level > 300:
            return "\033[1;34m[BIO] High Toxicity! Engaging Air Ionizers. Particle Neutralization: 99.9%.\033[0m"
        return "[STATUS] Ambient air quality safe."

    def p3457_exhaust_geometry(self, speed):
        if speed > 150:
            self.exhaust_mode = "RACE_TUNED"
            return "\033[1;33m[ENGINE] Opening Variable Exhaust Flaps. Maximum Flow Enabled.\033[0m"
        return "[STATUS] Stealth exhaust mode active."

if __name__ == "__main__":
    umc = UniversalMachineController()
    print("-" * 60)
    print("   JARVIS UMC: EXTREME PERFORMANCE (P3453-3457)")
    print("-" * 60)
    
    print(umc.p3453_liquid_nitro_cool(95))
    print(umc.p3454_plasma_cutter())
    print(umc.p3455_resource_scanner())
    print(umc.p3456_air_ionizer(450))
    print(umc.p3457_exhaust_geometry(180))
    
    print("-" * 60)
    print("STATUS: Thermal Efficiency & Utility Tools Online.")
    print("-" * 60)
