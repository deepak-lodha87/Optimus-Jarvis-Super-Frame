import time
import random

class UniversalMachineController:
    def __init__(self):
        self.oxygen_level = 21 # %
        self.brake_pressure = "NORMAL"

    def p3413_oxygen_pump(self, cabin_air_quality):
        if cabin_air_quality < 50:
            self.oxygen_level = 25
            return "\033[1;32m[SURVIVAL] Low Air Quality! Extracting Oxygen from Atmosphere.\033[0m"
        return "[STATUS] Cabin air fresh."

    def p3414_hydro_braking(self, surface_wet):
        if surface_wet:
            self.brake_pressure = "MAX_HYDRAULIC"
            return "\033[1;33m[SAFETY] Wet Surface! Increasing Brake Fluid Pressure for Grip.\033[0m"
        return "[STATUS] Braking system standard."

    def p3415_dream_state_sync(self, brain_activity):
        if brain_activity == "LOW":
            return "\033[1;34m[NEURAL] Deep Sleep Detected. Dimming Lights & Activating Silent Security.\033[0m"
        return "[NEURAL] User Alert."

    def p3416_heat_shielding(self):
        return "\033[1;35m[STEALTH] Atomic Heat Shield Active. Exterior Temperature: Constant.\033[0m"

    def p3417_static_discharge(self):
        return "\033[1;36m[SAFETY] Static Charge Detected. Grounding Hull via Conductive Tyres.\033[0m"

if __name__ == "__main__":
    umc = UniversalMachineController()
    print("-" * 60)
    print("   JARVIS UMC: SURVIVAL & NEURAL MAPPING (P3413-3417)")
    print("-" * 60)
    
    print(umc.p3413_oxygen_pump(40))
    print(umc.p3414_hydro_braking(True))
    print(umc.p3415_dream_state_sync("LOW"))
    print(umc.p3416_heat_shielding())
    print(umc.p3417_static_discharge())
    
    print("-" * 60)
    print("STATUS: Life Support & Stealth Protocols Active.")
    print("-" * 60)
