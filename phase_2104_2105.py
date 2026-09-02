import time
import random

def initialize_flight_systems():
    print("\n\033[1;36m[PHASE 2104]: Initializing Autonomous Flight Control...\033[0m")
    sensors = ["Altimeter", "Gyroscopic_Stabilizer", "Thrust_Vectoring"]
    for s in sensors:
        time.sleep(0.4)
        print(f">> Calibrating {s}... \033[1;32mCALIBRATED\033[0m")
    print("\033[1;33m[JARVIS]: Flight surfaces are responsive. Propulsion ready.\033[0m")

def deploy_weapons_framework():
    print("\n\033[1;31m[PHASE 2105]: Deploying Advanced Weapons Systems...\033[0m")
    weapons = ["Smart_Micro_Missiles", "Repulsor_Beam_Coils", "Laser_Guided_HUD"]
    for w in weapons:
        time.sleep(0.5)
        print(f">> Arming {w}... \033[1;32mREADY\033[0m")
    
    target_lock = random.randint(95, 100)
    print(f"\033[1;31m>> Target Acquisition Accuracy: {target_lock}%\033[0m")

if __name__ == "__main__":
    print("="*60)
    print("          OPTIMUS JARVIS SUPER-FRAME: PHASE 2105          ")
    print("="*60)
    initialize_flight_systems()
    print("-" * 40)
    deploy_weapons_framework()
    print("\n\033[1;32m[JARVIS]: System is combat-ready and flight-capable.\033[0m")
    print("="*60)
