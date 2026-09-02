# Optimus Jarvis Super-Frame: Phase 491-492
# Feature: Thermal Management Shield & Overheat Mitigation

import time
import random

class JarvisThermalShield:
    def __init__(self):
        self.code_ver = "492.Thermal-Guard"
        self.critical_temp = 45.0  # Celsius

    def code_491_monitor_sensors(self):
        print(f"\n[MODULE 491] Accessing Internal Thermal Sensors...")
        time.sleep(1.2)
        # Simulating a temperature reading
        current_temp = random.uniform(35.0, 48.0)
        print(f"[SYSTEM] Core Temperature: {current_temp:.1f}°C")
        return current_temp

    def code_492_mitigate_heat(self, temp):
        print("\n[MODULE 492] Analyzing Thermal Profile...")
        time.sleep(1)
        
        if temp >= self.critical_temp:
            print("[CRITICAL] Overheat Warning! Temperature exceeds safe limit.")
            print("[ACTION] Enabling Passive Cooling Mode. Scaling down CPU Clock.")
            print("[ACTION] Pausing non-essential Jarvis background tasks.")
        else:
            print("[STATUS] Temperature Stable. Thermal overhead is within limits.")

if __name__ == "__main__":
    t_shield = JarvisThermalShield()
    print(f"--- {t_shield.code_ver}: Operational ---")
    
    current_temp = t_shield.code_491_monitor_sensors()
    t_shield.code_492_mitigate_heat(current_temp)
    
    print("\n--- Phase 492 Complete. Hardware Safety Protocol is Online. ---")
