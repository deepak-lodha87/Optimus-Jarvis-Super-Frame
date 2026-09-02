import time
import random

class UniversalMachineController:
    def __init__(self):
        self.tire_psi = 32
        self.oil_health = 100 # %
        self.brake_temp = 40 # Celsius

    def p3283_tire_regulation(self, terrain):
        if terrain == "OFF-ROAD":
            self.tire_psi = 22
            return f"\033[1;33m[TIRES] Off-Road detected. Deflating to {self.tire_psi} PSI for grip.\033[0m"
        return f"[TIRES] Highway mode. Maintaining {self.tire_psi} PSI."

    def p3284_air_brake_flaps(self, speed):
        if speed > 200:
            return "\033[1;31m[AERO-BRAKE] High Speed! Deploying Rear Wing Flaps for Drag.\033[0m"
        return "[AERO] Speed normal. Flaps retracted."

    def p3285_oil_viscosity_check(self):
        self.oil_health -= random.randint(1, 5)
        if self.oil_health < 20:
            return f"\033[1;31m[OIL] Warning! Viscosity low ({self.oil_health}%). Change Recommended.\033[0m"
        return f"\033[1;32m[OIL] Health: {self.oil_health}%. Flow optimal.\033[0m"

    def p3286_active_brake_cooling(self, temp):
        self.brake_temp = temp
        if self.brake_temp > 250:
            return "\033[1;35m[COOLING] Brakes Overheating! Opening Front Air Ducts.\033[0m"
        return f"[TEMP] Brakes at {self.brake_temp}°C. Within limits."

    def p3287_steering_alignment(self):
        return "\033[1;36m[ALIGN] Steering Zero-Point Synced. Drift corrected.\033[0m"

if __name__ == "__main__":
    umc = UniversalMachineController()
    print("-" * 60)
    print("   JARVIS UMC: MECHANICAL PRECISION BUNDLE (P3283-3287)")
    print("-" * 60)
    
    print(umc.p3283_tire_regulation("OFF-ROAD"))
    print(umc.p3284_air_brake_flaps(250))
    print(umc.p3285_oil_viscosity_check())
    print(umc.p3286_active_brake_cooling(280))
    print(umc.p3287_steering_alignment())
    
    print("-" * 60)
    print("STATUS: Mechanical Systems Calibrated. No Repeats.")
    print("-" * 60)
