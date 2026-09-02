import os
import time
import random

def stealth_motion_defense():
    print("\n" + "="*50)
    print("|    JARVIS PHASE 163: MOTION STEALTH DEFENSE   |")
    print("="*50)

    print("\n[SYSTEM]: Activating accelerometer sensitivity...")
    time.sleep(1)
    
    # Simulating a sudden movement detection
    # In real Termux, this would read from 'termux-sensor'
    motion_detected = random.choice([True, False])
    
    if motion_detected:
        print("[ALERT]: Unauthorized movement detected!")
        msg = "Commander, someone has moved the device. Initiating stealth alert and capturing logs."
        status = "ALERT ACTIVE"
    else:
        msg = "Device status: Stationary. Perimeter is secure."
        status = "SECURE"

    print(f"\n[JARVIS]: {msg}")
    os.system(f"termux-tts-speak '{msg}'")

    print(f"\n[LOG]: Security Status: {status}")
    print("="*50)

if __name__ == "__main__":
    stealth_motion_defense()
