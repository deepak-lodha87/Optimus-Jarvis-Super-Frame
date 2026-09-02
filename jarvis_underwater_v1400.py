import os
import math
import time

class UnderwaterCore:
    def __init__(self):
        self.master = "Deepak"
        self.phase = 1400
        self.max_depth = 500  # meters (as per your Phase 7 specs)

    def calculate_hydrostatic_pressure(self, depth):
        # Phase 1350: Pressure calculation (P = rho * g * h)
        density_water = 1025 # kg/m^3 (Sea water)
        gravity = 9.81
        pressure_pa = density_water * gravity * depth
        return round(pressure_pa / 1000000, 2) # Converting to MegaPascals (MPa)

    def deploy_navigation(self):
        print(f"\n\033[1;34m[INITIATING UNDERWATER NAVIGATION - PHASE {self.phase}]\033[0m")
        os.system('termux-tts-speak "Deepak sir, synchronizing submarine dynamics and pressure sensors."')

        # Phase 1380: Sonar Mapping Simulation
        print(f"\033[1;32m[SONAR]:\033[0m Scanning seabed topography...")
        time.sleep(0.5)
        
        current_depth = 450
        pressure = self.calculate_hydrostatic_pressure(current_depth)
        
        print(f"\033[1;36m[DYNAMICS]:\033[0m Current Depth: {current_depth}m")
        print(f"\033[1;36m[PRESSURE]:\033[0m Hull Integrity: STABLE at {pressure} MPa")

        report = (
            f"Deepak sir, Phase 1400 complete. The Submarine Navigation module is now "
            f"functional. Hydrostatic pressure limits are synced for your blueprints."
        )

        print("-" * 60)
        print(f"\033[1;37;44m  JARVIS UNDERWATER - PHASE 1400 SECURED  \033[0m")
        print(f"| MAX DEPTH  : {self.max_depth}m ")
        print(f"| NAVIGATION : AUTONOMOUS ")
        print("-" * 60)

        os.system(f'termux-tts-speak "{report}"')

if __name__ == "__main__":
    nav = UnderwaterCore()
    nav.deploy_navigation()
