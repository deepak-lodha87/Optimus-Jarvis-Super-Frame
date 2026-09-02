import time
import random

class UniversalMachineController:
    def __init__(self):
        self.stealth_status = "INACTIVE"
        self.visibility_level = 100 # %
        self.thermal_signature = "HIGH"

    def p3468_smoke_screen(self, chase_detected):
        if chase_detected:
            return "\033[1;31m[TACTICAL] Deploying Multi-Spectral Smoke. Visual and IR sensors blocked.\033[0m"
        return "[STATUS] Rear perimeter clear."

    def p3469_night_vision_v3(self, light_level):
        if light_level < 10:
            return "\033[1;32m[VISION] Low Light! Activating Thermal Overlay V3. Target tracking online.\033[0m"
        return "[STATUS] Standard visual feed active."

    def p3470_heat_masking(self):
        self.thermal_signature = "ZERO"
        return "\033[1;34m[STEALTH] Liquid-Nitrogen Cooling channeled to Exhaust. Thermal signature hidden.\033[0m"

    def p3471_camouflage_active(self, environment):
        return f"\033[1;35m[GHOST] Scanning {environment}. Adjusting Hull LEDs and Pigments. Camouflage: 98%.\033[0m"

    def p3472_silent_drive(self):
        return "\033[1;36m[ACOUSTIC] Engaging Anti-Vibration Pads and Low-Decibel Mode. Machine is Silent.\033[0m"

if __name__ == "__main__":
    umc = UniversalMachineController()
    print("-" * 60)
    print("   JARVIS UMC: TACTICAL STEALTH MODULE (P3468-3472)")
    print("-" * 60)
    
    print(umc.p3468_smoke_screen(True))
    print(umc.p3469_night_vision_v3(5))
    print(umc.p3470_heat_masking())
    print(umc.p3471_camouflage_active("Forest"))
    print(umc.p3472_silent_drive())
    
    print("-" * 60)
    print("STATUS: Stealth & Recon Protocols Active.")
    print("-" * 60)
