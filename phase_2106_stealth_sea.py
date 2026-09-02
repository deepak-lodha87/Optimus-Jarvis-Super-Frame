import time

def activate_stealth_mode():
    print("\n\033[1;35m[PHASE 2106.1]: Initializing Adaptive Stealth Technology...\033[0m")
    tech = ["Photo-Reflective Panels", "Acoustic Dampeners", "Radar-Absorbent Coating"]
    for t in tech:
        time.sleep(0.5)
        print(f">> Engaging {t}... \033[1;32mACTIVE\033[0m")
    print("\033[1;33m[JARVIS]: Stealth signature minimized. System is now invisible to Radar.\033[0m")

def activate_deep_sea_protocol():
    print("\n\033[1;34m[PHASE 2106.2]: Calibrating Deep Sea Blueprints...\033[0m")
    specs = ["Pressure_Resistance_Hull", "Internal_Oxygen_Recycler", "Hydrodynamic_Thrust"]
    for s in specs:
        time.sleep(0.5)
        print(f">> Deploying {s}... \033[1;32mSTABLE\033[0m")
    print("\033[1;34m>> Current Depth Rating: 5000 Meters Below Sea Level.\033[0m")

if __name__ == "__main__":
    print("="*60)
    print("          OPTIMUS JARVIS SUPER-FRAME: PHASE 2106          ")
    print("="*60)
    activate_stealth_mode()
    print("-" * 40)
    activate_deep_sea_protocol()
    print("\n\033[1;32m[JARVIS]: Multi-Environment Adaptation Complete.\033[0m")
    print("="*60)
