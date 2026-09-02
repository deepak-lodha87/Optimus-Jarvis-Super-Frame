import os
import time
import random

def satellite_uplink_sync():
    print("\n" + "="*50)
    print("|    JARVIS PHASE 158: SATELLITE UPLINK SYNC    |")
    print("="*50)

    print("\n[SYSTEM]: Local Network Down. Searching for Satellite Link...")
    time.sleep(1.5)

    # Simulating Sat-Link Search
    satellites = ["Starlink-X", "NavIC-Global", "DeepSpace-Relay"]
    selected_sat = random.choice(satellites)

    print(f"[SCANNING]: Found {selected_sat} signal...")
    time.sleep(1)

    msg = f"Commander, ground blackout is active. I have established a high-frequency link with {selected_sat}. System is back online via Space-Link."
    
    print(f"\n[JARVIS]: {msg}")
    os.system(f"termux-tts-speak '{msg}'")

    print(f"\n[STATUS]: OFFLINE SURVIVAL MODE ACTIVE.")
    print("="*50)

if __name__ == "__main__":
    satellite_uplink_sync()
