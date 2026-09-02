import time

def upgrade_system():
    print("\n\033[1;31m[ALERT]: Advancing to Next Evolutionary Phases...\033[0m")
    phases = [2102, 2103, 2104]
    descriptions = ["Armor Structural Integrity", "Arc Reactor Synchronization", "Autonomous Flight Logic"]
    
    for i in range(len(phases)):
        time.sleep(0.6)
        print(f"Installing Phase {phases[i]}: {descriptions[i]}... \033[1;32mDONE\033[0m")

def phase_2102_logic():
    print("\n\033[1;36m[PHASE 2102]: Initializing Nanotech Armor Blueprints...\033[0m")
    print(">> Material: Gold-Titanium Alloy with Carbon Nanotube layering.")
    print(">> Status: Blueprint Loaded into Memory.")

def phase_2103_logic():
    print("\n\033[1;33m[PHASE 2103]: Calibrating Energy Output...\033[0m")
    print(">> Current Output: 1.21 Gigawatts.")
    print(">> Stability: 99.9% - Optimal for Flight.")

if __name__ == "__main__":
    print("="*60)
    upgrade_system()
    print("-" * 40)
    phase_2102_logic()
    phase_2103_logic()
    print("\n\033[1;32m[JARVIS]: System is now operational at Phase 2103.\033[0m")
    print("="*60)
