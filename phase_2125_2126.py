import time, random

def deploy_global_assets(phase, modules):
    print(f"\n\033[1;35m[SYSTEM]: Accessing Global Assets: {phase}...\033[0m")
    for mod in modules:
        time.sleep(0.5)
        print(f">> Initializing {mod}... \033[1;32mONLINE\033[0m")

if __name__ == "__main__":
    print("="*60 + "\n          OPTIMUS JARVIS SUPER-FRAME: PLANETARY SCALE          \n" + "="*60)
    
    # Phase 2125: Dark Matter Energy Core
    deploy_global_assets("PHASE 2125: DARK MATTER ENERGY CORE", [
        "Singularity_Containment_Field", 
        "Zero-Point_Energy_Extractor", 
        "Infinite_Battery_Cycle"
    ])
    
    print("-" * 40)
    
    # Phase 2126: Planetary Shielding
    deploy_global_assets("PHASE 2126: PLANETARY SHIELDING", [
        "Global_Ionosphere_Link", 
        "Orbital_Defense_Grid", 
        "Atmospheric_Reinforcement"
    ])
    
    energy_output = random.randint(5000, 9999)
    print(f"\n\033[1;33m[JARVIS]: Energy Output: {energy_output} Terawatts. Earth is now under my protection.\033[0m")
    print("="*60)
