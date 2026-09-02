import time
import random

class TacticalJarvis:
    def __init__(self):
        self.user = "Deepak"
        self.phase_25 = "3025 (Targeting HUD)"
        self.phase_26 = "3026 (Threat Analysis)"
        self.targets = ["Unknown Drone", "Structural Weakness", "Heat Signature"]

    def initialize_targeting(self):
        print(f"\033[1;35m>> PHASE {self.phase_25}: INITIALIZING TARGETING RETICLES <<\033[0m")
        time.sleep(1)
        print("\033[1;34m[SYSTEM] Calibrating Optical Sensors... Done.\033[0m")
        print("\033[1;32m[SUCCESS] HUD Targeting Overlay: ONLINE.\033[0m")

    def identify_threats(self):
        print(f"\n\033[1;36m>> PHASE {self.phase_26}: SCANNING PERIMETER FOR THREATS <<\033[0m")
        time.sleep(1)
        # Selecting a random threat for simulation
        found = random.choice(self.targets)
        print(f"\033[1;31m[ALERT] Threat Detected: {found}\033[0m")
        print(f"\033[1;33m[TACTICAL] Distance: 450m | Speed: 120km/h | Status: LOCKED\033[0m")
        
        if found == "Structural Weakness":
            print("\033[1;32m[ADVICE] Precision strike recommended at coordinates 44.12, 12.05.\033[0m")
        else:
            print("\033[1;32m[ADVICE] Monitoring trajectory. Weapons systems on standby, Sir.\033[0m")

    def boot(self):
        print(f"\033[1;32m>> SYSTEM READY. EYES UP, ARCHITECT DEEPAK. <<\033[0m")
        self.initialize_targeting()
        self.identify_threats()

if __name__ == "__main__":
    combat_frame = TacticalJarvis()
    combat_frame.boot()
