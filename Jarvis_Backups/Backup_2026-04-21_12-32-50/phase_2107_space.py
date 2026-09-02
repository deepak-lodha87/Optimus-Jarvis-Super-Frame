import time

def initialize_space_flight():
    print("\n\033[1;35m[PHASE 2107.1]: Activating Vacuum-Ready Propulsion...\033[0m")
    modules = ["Ion_Thrusters", "Zero_G_Stabilization", "Solar_Radiation_Shielding"]
    for m in modules:
        time.sleep(0.5)
        print(f">> Initializing {m}... \033[1;32mREADY\033[0m")
    print("\033[1;33m[JARVIS]: Suit is now sealed for Space Vacuum.\033[0m")

def atmospheric_reentry_protocols():
    print("\n\033[1;31m[PHASE 2107.2]: Calibrating Re-entry Heat Shield...\033[0m")
    systems = ["Thermal_Ablative_Coating", "Automatic_Parachute_Deployment", "Descent_Thrusters"]
    for s in systems:
        time.sleep(0.5)
        print(f">> Deploying {s}... \033[1;32mOPTIMAL\033[0m")
    print("\033[1;31m>> Current Heat Tolerance: 3000°C.\033[0m")

if __name__ == "__main__":
    print("="*60)
    print("          OPTIMUS JARVIS SUPER-FRAME: PHASE 2107          ")
    print("="*60)
    initialize_space_flight()
    print("-" * 40)
    atmospheric_reentry_protocols()
    print("\n\033[1;32m[JARVIS]: Space exploration protocols are now online.\033[0m")
    print("="*60)
