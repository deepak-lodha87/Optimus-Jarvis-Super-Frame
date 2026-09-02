import time
import random

class UniversalMachineController:
    def __init__(self):
        self.laser_shield = "OFF"
        self.core_temp = 400 # Kelvin
        self.air_purity = 100 # %

    def p3403_laser_deflector(self, incoming_laser):
        if incoming_laser:
            self.laser_shield = "REFLECTIVE_MODE"
            return "\033[1;31m[TACTICAL] Laser Lock Detected! Mirror-Shield Active. Deflecting Beam.\033[0m"
        return "[STATUS] No laser threats detected."

    def p3404_thermal_venting(self):
        if self.core_temp > 350:
            print("\033[1;33m[ENGINE] Core Overheat! Opening Thermal Vents. Releasing High-Pressure Steam...\033[0m")
            self.core_temp = 300
            return "[SUCCESS] Core Temp Stabilized. Extra Thrust Generated."
        return "[STATUS] Thermal levels normal."

    def p3405_pulse_encryption(self):
        return "\033[1;32m[SECURITY] Neural Link Pulse Encrypted via Quantum-Key. Connection: 100% Secure.\033[0m"

    def p3306_electrolytic_cleaning(self):
        return "\033[1;34m[SURFACE] Activating Pulse-Cleaning. Repelling dirt and moisture from outer shell.\033[0m"

    def p3407_gas_analyzer(self, gas_type):
        if gas_type == "TOXIC":
            self.air_purity = 20
            return "\033[1;35m[BIO-HAZARD] Warning! Poisonous Gas Detected. Sealing Cabin Air Intake.\033[0m"
        return "[STATUS] Atmospheric air safe for breathing."

if __name__ == "__main__":
    umc = UniversalMachineController()
    print("-" * 60)
    print("   JARVIS UMC: TACTICAL & FUSION DEFENSE (P3403-3407)")
    print("-" * 60)
    
    print(umc.p3403_laser_deflector(True))
    print(umc.p3404_thermal_venting())
    print(umc.p3405_pulse_encryption())
    print(umc.p3306_electrolytic_cleaning())
    print(umc.p3407_gas_analyzer("CLEAR"))
    
    print("-" * 60)
    print("STATUS: Tactical Grid Locked. Defense Protocols Online.")
    print("-" * 60)
