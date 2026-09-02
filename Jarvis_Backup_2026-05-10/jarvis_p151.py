import os
import random
import time

def emi_blackout_monitor():
    print("\n" + "="*50)
    print("|    JARVIS PHASE 151: EMI BLACKOUT MONITOR      |")
    print("="*50)

    print("\n[SYSTEM]: Scanning electromagnetic spectrum...")
    time.sleep(1.5)

    # Simulating EMI Levels in MHz
    emi_level = random.randint(10, 150) 
    print(f"[DATA]: Current EMI Level: {emi_level} MHz")

    if emi_level > 100:
        status = "CRITICAL: EMI BLACKOUT IMMINENT"
        action = "Activating Faraday Cage Shielding & Offline Mode."
    else:
        status = "STABLE: Interference within safe limits."
        action = "Standard encryption active."

    msg = f"Commander, status is {status}. {action}"
    
    print(f"\n[JARVIS]: {msg}")
    os.system(f"termux-tts-speak '{msg}'")

    print("\n[LOG]: EMI data integrated into defensive core.")
    print("="*50)

if __name__ == "__main__":
    emi_blackout_monitor()
