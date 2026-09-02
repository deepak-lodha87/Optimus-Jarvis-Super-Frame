import time, random

def deploy_module(name, tasks):
    print(f"\n\033[1;36m[SYSTEM]: Initializing {name}...\033[0m")
    for task in tasks:
        time.sleep(0.4)
        print(f">> {task}... \033[1;32mSTABLE\033[0m")

if __name__ == "__main__":
    print("="*60 + "\n          OPTIMUS JARVIS SUPER-FRAME: MULTI-PHASE LOAD          \n" + "="*60)
    
    # Phase 2113: Sonic Weaponry
    deploy_module("PHASE 2113: SONIC WEAPONRY", [
        "Frequency_Modulator_Active", 
        "Non-Lethal_Pulse_Cannon", 
        "Acoustic_Pressure_Sync"
    ])
    
    print("-" * 40)
    
    # Phase 2114: X-Ray & Multi-Spectrum Vision
    deploy_module("PHASE 2114: X-RAY VISION", [
        "Thermal_Overlay_Engaged", 
        "Lead-Filtering_Algorithm", 
        "Structural_Density_Scan"
    ])
    
    print(f"\n\033[1;33m[JARVIS]: Detection accuracy at {random.randint(97,99)}%. Ready to see through obstacles.\033[0m")
    print("="*60)
