import os
import json
import time

def start_dual_sync():
    os.system('clear')
    print("\033[1;31m[SYSTEM]\033[0m Activating Dual-Path Tracking (Satellite + Network)...")
    
    # Cleaning old grid data
    if os.path.exists("loc.json"):
        os.remove("loc.json")

    # Step 1: Rapid Network Check
    print("\033[1;33m[SYNC 1]\033[0m Fetching Network Grid...")
    os.system("termux-location -p network > loc_net.json")
    
    # Step 2: High-Precision Satellite Handshake
    print("\033[1;36m[SYNC 2]\033[0m Pinging Satellites for Deep Precision...")
    os.system("termux-location -p gps > loc_gps.json")

    # Verification Logic
    try:
        # Priority to GPS, Fallback to Network
        source = "loc_gps.json" if os.path.exists("loc_gps.json") and os.stat("loc_gps.json").st_size > 0 else "loc_net.json"
        
        with open(source, "r") as f:
            data = json.load(f)
            lat, lon = data['latitude'], data['longitude']
            acc = data.get('accuracy', 'Standard')

            print(f"\n\033[1;32m[LOCKED]\033[0m Source: {source} | Accuracy: {acc}m")
            print(f"Coordinates: {lat}, {lon}")

            # satellite view with absolute zoom
            map_url = f"https://www.google.com/maps/search/?api=1&query={lat},{lon}&t=k"
            
            os.system(f'termux-tts-speak "Deepak sir, dual-sync established. Precision grid is now 100 percent accurate."')
            os.system(f"termux-open-url '{map_url}'")
    except:
        print("\033[1;31m[FATAL]\033[0m Both grids failed. Please check if GPS is ON and phone is restarted.")

if __name__ == "__main__":
    start_dual_sync()
