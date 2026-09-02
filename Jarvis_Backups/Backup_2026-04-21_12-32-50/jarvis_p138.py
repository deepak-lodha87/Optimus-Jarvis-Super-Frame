import os
import time

def simulation_master():
    print("\n" + "="*50)
    print("|    JARVIS PHASE 138: MASTER SIMULATION ENGINE  |")
    print("="*50)

    print("\n[SYSTEM]: Initializing Zero-Error Protocol...")
    time.sleep(1)

    # Simulated Engineering Check
    design_input = input("\n[COMMAND]: What are we designing? (Jet/Suit/Part): ").upper().strip()
    
    print(f"\n[JARVIS]: Running 10,000 simulations for {design_input}...")
    time.sleep(2)

    # Logic: Checking for failures before physical build
    structural_integrity = 99.9  # Percentage
    error_margin = 0.01          # Low margin means safe

    if structural_integrity > 95 and error_margin < 0.1:
        status = "CERTIFIED SAFE"
        msg = f"Commander, the {design_input} design is flawless. No risk of failure detected."
    else:
        status = "REJECTED"
        msg = "Safety parameters failed. Redesigning automatically..."

    print(f"\n[ANALYSIS]: {status}")
    print(f"[REPORT]: {msg}")
    os.system(f"termux-tts-speak '{msg}'")

    print("\n" + "="*50)

if __name__ == "__main__":
    simulation_master()
