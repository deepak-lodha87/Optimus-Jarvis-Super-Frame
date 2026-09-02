import os
import time

def universal_machine_controller():
    print("\n" + "="*50)
    print("|    JARVIS PHASE 146: UNIVERSAL MACHINE INTERFACE |")
    print("="*50)

    machine_type = input("\n[INPUT]: Identify Machine to Link (Motor/Robotic_Arm/Generator): ").upper().strip()
    
    print(f"\n[SYSTEM]: Scanning {machine_type} communication ports...")
    time.sleep(2)
    
    # Simulating connection to different hardware
    print(f"[JARVIS]: Establishing secure link via Universal Protocol...")
    time.sleep(1.5)

    msg = f"Commander, link established with {machine_type}. I am now generating the control logic."
    print(f"\n[STATUS]: CONNECTED")
    print(f"[JARVIS]: {msg}")
    os.system(f"termux-tts-speak '{msg}'")

    # Autonomous Action Simulation
    print(f"\n[ACTION]: Running initial diagnostic on {machine_type}...")
    time.sleep(1)
    print(f"[RESULT]: {machine_type} is now under Jarvis's autonomous control.")
    
    print("\n[LOG]: Control sequence saved. Ready for real-world execution.")
    print("="*50)

if __name__ == "__main__":
    universal_machine_controller()
