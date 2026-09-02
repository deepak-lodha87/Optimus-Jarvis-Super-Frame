import os
import time
import sys

def blackout_emergency():
    print("\n" + "!"*50)
    print("|    JARVIS PHASE 153: BLACKOUT EMERGENCY       |")
    print("!"*50)

    print("\n[ALERT]: Extreme EMI Pulse Detected!")
    print("[SYSTEM]: Total Communication Failure Imminent...")
    time.sleep(1)

    # Emergency Steps
    steps = [
        "Isolating Core CPU from external antenna...",
        "Shutting down high-sensitivity optical sensors...",
        "Switching to Internal Quartz Clock for timing...",
        "Activating Redundant Analog Backup..."
    ]

    for step in steps:
        print(f"[ACTION]: {step}")
        time.sleep(0.7)

    msg = "Commander, we are in total blackout. I have entered deep-sleep protection mode. Waiting for signal stability."
    
    print(f"\n[JARVIS]: {msg}")
    os.system(f"termux-tts-speak '{msg}'")

    print("\n[STATUS]: CORE PROTECTED. SYSTEM OFFLINE.")
    print("!"*50)

if __name__ == "__main__":
    blackout_emergency()
