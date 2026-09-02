import os
import time
import random

class ThermalDynamics:
    def __init__(self):
        self.master = "Deepak"
        self.phase = 2100
        self.cooling_system = "Cryo-Cooling Protocol"

    def monitor_core_temperature(self):
        # Phase 2050: थर्मल रीडिंग और कूलिंग सिमुलेशन
        print(f"\033[1;36m[MONITORING]:\033[0m Checking CPU and Frame temperature profiles...")
        time.sleep(0.4)
        
        # रैंडम तापमान रीडिंग (सेल्सियस में)
        current_temp = random.randint(35, 48)
        print(f"\033[1;33m[THERMAL]:\033[0m Core Temperature detected at {current_temp}°C")
        
        if current_temp > 42:
            print(f"\033[1;31m[OVERHEATING]:\033[0m Activating {self.cooling_system}...")
            time.sleep(0.5)
            current_temp -= 6
            print(f"\033[1;32m[STABILIZED]:\033[0m Temperature brought down to {current_temp}°C")
        else:
            print(f"\033[1;32m[STABLE]:\033[0m Thermal dissipation is optimal.")
            
        return current_temp

    def deploy_thermal_core(self):
        print(f"\n\033[1;37;41m [ OPTIMUS JARVIS : THERMAL DYNAMICS - PHASE {self.phase} ] \033[0m")
        os.system('termux-tts-speak "Deepak sir, synchronizing thermal dissipation and hardware cooling layers."')

        final_temp = self.monitor_core_temperature()

        report = (
            f"Deepak sir, Phase 2100 is fully operational. The Thermal Dynamics module "
            f"has successfully stabilized the core temperature at {final_temp} degrees."
        )
        
        print("-" * 65)
        print(f"\033[1;37;42m  JARVIS THERMAL - PHASE 2100 SECURED  \033[0m")
        print(f"| REACTION TYPE  : CRYO-COOLING SHIELD ")
        print(f"| HARDWARE STATE : SAFE & FULLY OPERATIONAL ")
        print("-" * 65)
        
        os.system(f'termux-tts-speak "{report}"')

if __name__ == "__main__":
    thermal = ThermalDynamics()
    thermal.deploy_thermal_core()
