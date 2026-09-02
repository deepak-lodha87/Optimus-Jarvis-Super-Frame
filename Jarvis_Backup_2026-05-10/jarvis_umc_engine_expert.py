import time

class UniversalMachineController:
    def __init__(self):
        self.tank_safety = "STABLE"
        self.radiator_shutter = "CLOSED"
        self.chain_lube_level = 100

    def p3289_fuel_inerting(self):
        print("\033[1;34m[SAFETY] Displacing Oxygen in Fuel Tank with Nitrogen...\033[0m")
        self.tank_safety = "INERTED"
        return f"[SUCCESS] Explosion Risk: 0%. Tank Status: {self.tank_safety}."

    def p3290_auto_lubrication(self):
        self.chain_lube_level -= 2
        return "\033[1;32m[MAINTENANCE] Chain Friction Detected. Applying Synthetic Lubricant.\033[0m"

    def p3291_radiator_shutter_control(self, temp):
        if temp > 95:
            self.radiator_shutter = "OPEN"
            return "\033[1;31m[THERMAL] High Temp! Opening Radiator Shutters for Airflow.\033[0m"
        return f"[AERO] Temp Stable ({temp}°C). Shutters Closed for Drag Reduction."

    def p3292_exhaust_tuning(self, rpm):
        if rpm > 8000:
            return "\033[1;35m[PERFORMANCE] Adjusting Exhaust Valves for Maximum Scavenging.\033[0m"
        return "[STATUS] Exhaust Back-Pressure: Optimized."

if __name__ == "__main__":
    umc = UniversalMachineController()
    print("-" * 60)
    print("   JARVIS UMC: ENGINE & SAFETY EXPERT (P3288-3292)")
    print("-" * 60)
    
    print(umc.p3289_fuel_inerting())
    print(umc.p3290_auto_lubrication())
    print(umc.p3291_radiator_shutter_control(102))
    print(umc.p3292_exhaust_tuning(8500))
    
    print("-" * 60)
    print("STATUS: Advance Engine Components Synced.")
    print("-" * 60)
