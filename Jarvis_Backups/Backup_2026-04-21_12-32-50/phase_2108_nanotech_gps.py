import time
import random

def initialize_nanotech_repair():
    print("\n\033[1;32m[PHASE 2108.1]: Activating Nanotech Self-Repair System...\033[0m")
    modules = ["Molecular_Sutures", "Structure_Regeneration", "Armor_Density_Calibration"]
    for m in modules:
        time.sleep(0.5)
        print(f">> Initializing {m}... \033[1;32mACTIVE\033[0m")
    
    repair_efficiency = random.randint(98, 100)
    print(f"\033[1;32m[JARVIS]: Self-repair efficiency at {repair_efficiency}%. Suit can heal in real-time.\033[0m")

def interstellar_gps_navigation():
    print("\n\033[1;34m[PHASE 2108.2]: Calibrating Time-Space GPS (Interstellar)...\033[0m")
    systems = ["Quantum_Positioning", "Star_Chart_Mapping", "Temporal_Sync_Clock"]
    for s in systems:
        time.sleep(0.5)
        print(f">> Syncing {s}... \033[1;32mSTABLE\033[0m")
    print("\033[1;36m>> Destination: Deep Space - Sector 7G. Navigation Locked.\033[0m")

if __name__ == "__main__":
    print("="*60)
    print("          OPTIMUS JARVIS SUPER-FRAME: PHASE 2108          ")
    print("="*60)
    initialize_nanotech_repair()
    print("-" * 40)
    interstellar_gps_navigation()
    print("\n\033[1;32m[JARVIS]: System is now self-sustaining and globally navigable.\033[0m")
    print("="*60)
