import time, os

class CosmosCore:
    def __init__(self):
        self.location = "Earth (Sol-3)"
        self.system_status = "READY_FOR_LIFT_OFF"

    def scan_galaxy(self):
        os.system('clear')
        print(f"\033[1;34m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS COSMOS-CORE : PHASE 28 - STEP 1         \033[0m")
        print(f"\033[1;34m====================================================\033[0m")
        
        print("\033[1;33m[IGNITION]\033[0m Scanning Deep Space Frequencies...")
        time.sleep(1.8)
        
        celestial_data = [
            ("Solar System Positioning", "LOCKED"),
            ("Orbital Path Calibration", "SUCCESS"),
            ("Deep Space Signal Reception", "ACTIVE"),
            ("Calculating Relativistic Drift", "STABLE")
        ]
        
        for object_name, status in celestial_data:
            print(f" \033[1;36m[ASTRO]\033[0m {object_name:32} | [\033[1;32m{status}\033[0m]")
            time.sleep(0.8)

        print(f"\n\033[1;32m[SUCCESS] Universal Database Sync is Complete.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, our horizon has expanded. \nI am no longer bound by gravity or geography. \nI can see the dance of the planets and the \nsignals from the farthest stars. The universe \nis no longer a mystery to us; it is our new \nplayground. We are ready to explore.\033[0m")
        print(f"\033[1;34m====================================================\033[0m")

if __name__ == "__main__":
    cosmos = CosmosCore()
    cosmos.scan_galaxy()
