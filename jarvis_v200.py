import os
import time
import sys

def startup_sequence():
    print("\n[SYSTEM]: INITIATING CORE ACTIVATION PROTOCOL...")
    time.sleep(1)
    
    steps = [
        "Neural Bridges Linking",
        "Biometric Syncing",
        "Environmental Scan Online",
        "Satellite Uplink Established",
        "Optimus Super-Frame Loading"
    ]
    
    for step in steps:
        sys.stdout.write(f"\r[PROCESS]: {step}... [COMPLETED]")
        sys.stdout.flush()
        time.sleep(0.7)
    
    print("\n\n" + "*"*60)
    print("       WELCOME ONLINE, COMMANDER DEEPAK.       ")
    print("      JARVIS PHASE 200 IS FULLY OPERATIONAL     ")
    print("*"*60)
    
    final_msg = "Commander Deepak, I am Optimus Jarvis. My core is active, and I am ready to assist you. All systems are at 100 percent."
    os.system(f"termux-tts-speak '{final_msg}'")

def main_dashboard():
    print("\n--- ACTIVE COMMAND CENTER ---")
    print("1. Stealth Mode: [ACTIVE]")
    print("2. Sentry Guard: [MONITORING]")
    print("3. Power matrix: [STABLE]")
    print("4. System Intel: [OPTIMAL]")
    print("-" * 30)

if __name__ == "__main__":
    startup_sequence()
    main_dashboard()
