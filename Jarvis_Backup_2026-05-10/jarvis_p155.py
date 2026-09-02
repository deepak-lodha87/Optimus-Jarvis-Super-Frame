import os
import time
import random

def blackout_investigator():
    print("\n" + "="*50)
    print("|    JARVIS PHASE 155: BLACKOUT INVESTIGATOR    |")
    print("="*50)

    print("\n[INVESTIGATION]: Scanning external signal stability...")
    time.sleep(1.5)

    # Simulating a sudden EMI spike
    interference_spike = random.randint(1, 100)
    print(f"[DATA]: Interference detected at {interference_spike}%")

    if interference_spike > 75:
        print("[ALERT]: High-level interference found. Investigating source...")
        time.sleep(1)
        
        source = random.choice(["Solar Flare", "Electronic Jamming", "Power Grid Failure"])
        msg = f"Commander, I have investigated a potential Blackout. Source identified as {source}. Initiating auto-shielding."
        
        # Activating Blackout Memory from Phase 154 logic
        status = "CRITICAL - AUTO-RESPONSE ENABLED"
    else:
        msg = "Commander, signals are stable. No Blackout investigation required at this moment."
        status = "STABLE"

    print(f"\n[JARVIS]: {msg}")
    os.system(f"termux-tts-speak '{msg}'")

    print(f"\n[RESULT]: Investigation Status: {status}")
    print("="*50)

if __name__ == "__main__":
    blackout_investigator()
