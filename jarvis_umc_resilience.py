import time
import random

class UniversalMachineController:
    def __init__(self):
        self.circuit_protection = "OFF"
        self.altitude = 500 # Meters
        self.battery_charge = 85 # %

    def p3473_emp_shield(self, emp_detected):
        if emp_detected:
            self.circuit_protection = "FARADAY_SHIELD_ACTIVE"
            return "\033[1;33m[SECURITY] EMP Attack Detected! Hardening Circuits. Faraday Cage Activated.\033[0m"
        return "[STATUS] Electrical systems secure."

    def p3474_auto_parachute(self, fall_velocity):
        if fall_velocity > 30 and self.altitude < 100:
            return "\033[1;31m[EMERGENCY] Freefall Detected! Deploying High-Velocity Parachutes.\033[0m"
        return "[STATUS] Altitude and velocity stable."

    def p3475_nano_lubrication(self, temp):
        if temp < -50:
            return "\033[1;36m[THERMAL] Extreme Cold! Releasing Nano-Lubricants to prevent engine seizure.\033[0m"
        return "[STATUS] Oil viscosity optimal."

    def p3476_kinetic_harvester(self, braking_force):
        energy_gained = braking_force * 0.1
        self.battery_charge += energy_gained
        return f"\033[1;32m[ENERGY] Braking Energy Captured. Battery Level: {self.battery_charge:.1f}%.\033[0m"

    def p3477_emergency_beacon(self):
        return "\033[1;35m[COMMS] Satellite Link Lost. Switching to Long-Range Radio Beacon. SOS Active.\033[0m"

if __name__ == "__main__":
    umc = UniversalMachineController()
    print("-" * 60)
    print("   JARVIS UMC: RESILIENCE & RECOVERY (P3473-3477)")
    print("-" * 60)
    
    print(umc.p3473_emp_shield(True))
    print(umc.p3474_auto_parachute(45))
    print(umc.p3475_nano_lubrication(-60))
    print(umc.p3476_kinetic_harvester(15))
    print(umc.p3477_emergency_beacon())
    
    print("-" * 60)
    print("STATUS: Resilience Grid Online. Systems Hardened.")
    print("-" * 60)
