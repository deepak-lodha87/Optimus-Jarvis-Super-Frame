import os
import random
import time

def anti_jamming_protocol():
    print("\n" + "="*50)
    print("|    JARVIS PHASE 152: ANTI-JAMMING PROTOCOL     |")
    print("="*50)

    print("\n[SYSTEM]: EMI Blackout detected in primary band...")
    time.sleep(1)
    
    # List of secure backup frequencies (in GHz)
    secure_channels = [2.4, 5.8, 10.2, 15.5, 24.0]
    
    print("[LOG]: Initiating Adaptive Frequency Hopping...")
    
    for i in range(3):
        new_freq = random.choice(secure_channels)
        print(f"[ACTION]: Hopping to secure channel: {new_freq} GHz")
        time.sleep(0.8)

    msg = "Commander, we have bypassed the EMI Blackout. Communication is now secure on a multi-band hopping sequence."
    
    print(f"\n[JARVIS]: {msg}")
    os.system(f"termux-tts-speak '{msg}'")

    print("\n[STATUS]: Encryption keys re-synced. System resilient.")
    print("="*50)

if __name__ == "__main__":
    anti_jamming_protocol()
