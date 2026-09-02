import time
import random

class UniversalMachineController:
    def __init__(self):
        self.water_tank_level = 0 # Liters
        self.brake_response = "OPTIMAL"
        self.dust_shield = "OFF"

    def p3353_water_extraction(self, humidity):
        if humidity > 40:
            self.water_tank_level += 0.5
            return f"\033[1;34m[LIFE-SUPPORT] Humidity: {humidity}%. Extracting H2O. Tank: {self.water_tank_level}L.\033[0m"
        return "[STATUS] Humidity low. Extraction paused."

    def p3354_fluid_brake_tune(self, oil_temp):
        if oil_temp > 120:
            self.brake_response = "STIFFENED"
            return "\033[1;31m[MECHANICAL] Brake Oil Hot. Adjusting Pressure for Instant Bite.\033[0m"
        return "[STATUS] Brake fluid pressure normal."

    def p3355_laser_tracking(self, steering_angle):
        return f"\033[1;33m[VISION] Swiveling Laser Beams {steering_angle} Degrees to Illuminate Corner.\033[0m"

    def p3356_satellite_uplink(self):
        return "\033[1;32m[COMMS] Global Satellite Uplink Established. High-Speed Data Sync Active.\033[0m"

    def p3357_dust_repulsion(self):
        self.dust_shield = "ON"
        return "\033[1;35m[SURFACE] Electro-Static Field Active. Repelling Dust Particles from Chassis.\033[0m"

if __name__ == "__main__":
    umc = UniversalMachineController()
    print("-" * 60)
    print("   JARVIS UMC: LIFE SUPPORT & PRECISION (P3353-3357)")
    print("-" * 60)
    
    print(umc.p3353_water_extraction(65))
    print(umc.p3354_fluid_brake_tune(135))
    print(umc.p3355_laser_tracking(15))
    print(umc.p3356_satellite_uplink())
    print(umc.p3357_dust_repulsion())
    
    print("-" * 60)
    print("STATUS: Survival & Visibility Protocols Operational.")
    print("-" * 60)
