import time
import random

class UniversalMachineController:
    def __init__(self):
        self.cabin_o2 = 21 # %
        self.tire_adhesion = 1.0 # Standard
        self.defense_active = False

    def p3228_oxygen_boost(self):
        self.cabin_o2 = 28
        return f"\033[1;32m[BIO] Oxygen Level Boosted to {self.cabin_o2}% for Peak Alertness.\033[0m"

    def p3229_roll_cage_expansion(self):
        return "\033[1;31m[SAFETY] Impact Detected! Pneumatic Roll-Cage Expanded. Interior Secured.\033[0m"

    def p3230_molecular_grip(self, surface_type):
        if surface_type == "WET":
            self.tire_adhesion = 1.8
            return "\033[1;34m[TIRES] Activating Hydro-Grip Molecules. Traction increased by 80%.\033[0m"
        return "[TIRES] Standard Grip Mode Active."

    def p3231_hud_vision_v3(self):
        return "\033[1;36m[HUD] 3D Augmented Reality Overlay Active. Targets Tagged in 500m.\033[0m"

    def p3232_sonic_confuser(self):
        self.defense_active = True
        return "\033[1;35m[DEFENSE] Emitting 18kHz Infrasound Waves. Perimeter Disorientation Engaged.\033[0m"

if __name__ == "__main__":
    umc = UniversalMachineController()
    print("-" * 60)
    print("   JARVIS UMC: SAFETY & SURFACE MASTERY (P3228-3332)")
    print("-" * 60)
    
    print(umc.p3228_oxygen_boost())
    print(umc.p3231_hud_vision_v3())
    print(umc.p3230_molecular_grip("WET"))
    print(umc.p3232_sonic_confuser())
    print(umc.p3229_roll_cage_expansion())
    
    print("-" * 60)
    print("STATUS: Interior Safety & Road Adhesion Locked.")
    print("-" * 60)
