import time
import random

class UniversalMachineController:
    def __init__(self):
        self.oxygen_level = 21 # Percentage
        self.gyro_balance = "STABLE"
        self.sos_active = False

    def p3378_oxygen_extraction(self, ambient_o2):
        if ambient_o2 < 18:
            print("\033[1;31m[BIO-ALERT] Low Oxygen! Activating Molecular Sieve Extraction...\033[0m")
            self.oxygen_level = 23
            return "[SUCCESS] Oxygen Level Restored. Pilot Alertness: High."
        return "[STATUS] Cabin Air Quality: Optimal."

    def p3379_gyro_stability(self, lean_angle):
        if abs(lean_angle) > 45:
            self.gyro_balance = "CORRECTING"
            return "\033[1;34m[GYRO] Counter-Torque Applied. Maintaining Vertical Stability.\033[0m"
        return "[STATUS] Balance: Center of Gravity Locked."

    def p3380_sos_drone_launch(self):
        self.sos_active = True
        return "\033[1;32m[COMMS] Primary Link Dead. Deploying High-Altitude SOS Drone to Satellite Orbit.\033[0m"

    def p3381_magnetic_coolant_flow(self, engine_temp):
        if engine_temp > 105:
            return "\033[1;33m[THERMAL] Accelerating Magnetic Coolant Flow. Temperature dropping...\033[0m"
        return "[STATUS] Thermal levels safe."

    def p3382_glass_electrification(self):
        return "\033[1;35m[ARMOR] Applying Ion-Charge to Windshield. Tensile Strength: MAX.\033[0m"

if __name__ == "__main__":
    umc = UniversalMachineController()
    print("-" * 60)
    print("   JARVIS UMC: LIFE SUPPORT & EMERGENCY (P3378-3382)")
    print("-" * 60)
    
    print(umc.p3378_oxygen_extraction(15))
    print(umc.p3379_gyro_stability(50))
    print(umc.p3380_sos_drone_launch())
    print(umc.p3381_magnetic_coolant_flow(110))
    print(umc.p3382_glass_electrification())
    
    print("-" * 60)
    print("STATUS: Survival Protocols & Orbital Comms Synced.")
    print("-" * 60)
