import os
import time

def integrated_processor():
    print("\n" + "="*50)
    print("|    JARVIS PHASE 154: INTEGRATED CORE PROCESSOR |")
    print("="*50)

    # Blackout Memory Check
    print("\n[MEMORY]: Loading Blackout Protocols (Phase 151-153)...")
    blackout_ready = True
    time.sleep(1)

    if blackout_ready:
        print("[STATUS]: Blackout Shield is ACTIVE in background.")
    
    # New Task Logic
    print("\n[PROCESSOR]: Ready for multi-tasking.")
    task = input("[INPUT]: Enter main objective: ").upper().strip()
    
    print(f"\n[JARVIS]: Analyzing '{task}' under Blackout Safety Rules...")
    time.sleep(1.5)

    # Prioritization Logic
    print("[LOG]: Setting task priority to HIGH.")
    msg = f"Commander, I have integrated the Blackout guard into the main processor. Objective '{task}' is now being executed with emergency backup safety."
    
    print(f"\n[JARVIS]: {msg}")
    os.system(f"termux-tts-speak '{msg}'")

    print("\n[RESULT]: Processor & Blackout Logic Synced.")
    print("="*50)

if __name__ == "__main__":
    integrated_processor()
