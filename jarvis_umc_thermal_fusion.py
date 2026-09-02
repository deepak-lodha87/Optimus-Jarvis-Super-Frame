import time
import random

class UniversalMachineController:
    def __init__(self):
        self.thermal_ghost = "INACTIVE"
        self.tire_tread_health = 60 # %
        self.noise_profile = "MECHANICAL"

    def p3343_thermal_decoy(self):
        self.thermal_ghost = "ACTIVE"
        print("\033[1;31m[STEALTH] Masking Engine Heat... Projecting Decoy Heat Signature 50m Away.\033[0m")
        return "[SUCCESS] Heat-Seeking Tracking Neutralized."

    def p3344_fusion_primer(self):
        return "\033[1;33m[POWER] Injecting H2 Fusion Primer. Combustion Efficiency: 98%.\033[0m"

    def p3345_tread_regeneration(self):
        if self.tire_tread_health < 70:
            print("\033[1;34m[MAINTENANCE] Tires Worn. Activating Molecular Surface Re-Texturing...\033[0m")
            self.tire_tread_health = 95
            return f"[SUCCESS] Tire Grip Restored to {self.tire_tread_health}%."
        return "[STATUS] Tread depth optimal."

    def p3346_battery_insulation(self, ext_temp):
        if ext_temp < 0:
            return "\033[1;36m[THERMAL] External Freezing Detected. Activating Internal Battery Warmers.\033[0m"
        return "[STATUS] Battery operating temperature stable."

    def p3347_acoustic_masking(self):
        self.noise_profile = "WHITE_NOISE"
        return "\033[1;35m[GHOST] Sound Profile Masked. Machine Sounding as Ambient Wind.\033[0m"

if __name__ == "__main__":
    umc = UniversalMachineController()
    print("-" * 60)
    print("   JARVIS UMC: THERMAL & FUSION BUNDLE (P3343-3347)")
    print("-" * 60)
    
    print(umc.p3343_thermal_decoy())
    print(umc.p3344_fusion_primer())
    print(umc.p3345_tread_regeneration())
    print(umc.p3346_battery_insulation(-15))
    print(umc.p3347_acoustic_masking())
    
    print("-" * 60)
    print("STATUS: Acoustic and Thermal Stealth Fully Locked.")
    print("-" * 60)
