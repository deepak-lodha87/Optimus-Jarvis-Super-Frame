import time
import random

class UniversalMachineController:
    def __init__(self):
        self.battery_status = "OPTIMAL"
        self.cabin_pressure = 1.0 # Atmosphere
        self.drone_count = 0

    def p3443_thermal_insulation(self, outside_temp):
        if outside_temp < -10:
            self.battery_status = "HEATING_ACTIVE"
            return f"\033[1;36m[THERMAL] Outside Temp: {outside_temp}°C. Activating Nano-Heaters for Battery Core.\033[0m"
        return "[STATUS] Battery operating in safe thermal range."

    def p3444_pressurization(self, altitude_m):
        if altitude_m > 4000:
            self.cabin_pressure = 1.05
            return "\033[1;34m[BIO] High Altitude Detected. Increasing Cabin Pressure for Pilot Comfort.\033[0m"
        return "[STATUS] Cabin pressure synchronized with sea level."

    def p3445_drone_swarm_sync(self, active_drones):
        self.drone_count = active_drones
        return f"\033[1;32m[SWARM] Quantum-Link established with {self.active_drones} Units. Formation: Delta-Shield.\033[0m"

    def p3446_sensor_jammer(self):
        return "\033[1;35m[STEALTH] Hull Magnetization Active. Scrambling nearby Radar & Sonar signals.\033[0m"

    def p3447_water_generation(self, humidity):
        if humidity > 30:
            return "\033[1;33m[RESOURCES] Extracting H2O from Atmosphere. Reservoir filling...\033[0m"
        return "[STATUS] Low humidity. Water extraction on standby."

if __name__ == "__main__":
    umc = UniversalMachineController()
    umc.active_drones = 50
    print("-" * 60)
    print("   JARVIS UMC: SURVIVAL & SWARM (P3443-3447)")
    print("-" * 60)
    
    print(umc.p3443_thermal_insulation(-40))
    print(umc.p3444_pressurization(5500))
    print(umc.p3445_drone_swarm_sync(50))
    print(umc.p3446_sensor_jammer())
    print(umc.p3447_water_generation(65))
    
    print("-" * 60)
    print("STATUS: Survival & Tactical Grid Online.")
    print("-" * 60)
