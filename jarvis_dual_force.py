import os
import json
import time

def start_dual_sync():
    os.system('clear')
    print("\033[1;31m[SYSTEM]\033[0m Initiating Dual-Path Satellite Interceptor...")
    
    # Cleaning old grid files
    for f in ["loc_gps.json", "loc_net.json"]:
        if os.path.exists(f): os.remove(f)

    # Step 1: Rapid Network Scan
    print("\033[1;33m[SCANNING]\033[0m Fetching Network Grid Data...")
    os.system("termux-location -p network > loc_net.json")
    
    # Step 2: High-Precision Satellite Handshake
    print("\033[1;36m[SEARCHING]\033[0m Pinging Satellites for Precision Lock...")
    os.system("termux-location -p gps > loc_gps.json")

    time.sleep(2)

    try:
        # Priority logic: GPS (More accurate) -> Network (Backup)
        if os.path.exists("loc_gps.json") and os.stat("loc_gps.json").st_size > 0:
            source_file = "loc_gps.json"
            status = "Satellite Lock"
        else:
            source_file = "loc_net.json"
            status = "Network Lock (Backup)"

        with open(source_file, "r") as f:
            data = json.load(f)
            lat, lon = data['latitude'], data['longitude']
            acc = data.get('accuracy', 'Standard')

            print(f"\n\033[1;32m[VERIFIED]\033[0m Mode: {status} | Accuracy: {acc}m")
            print(f"Coordinates: {lat}, {lon}")

            # Satellite View with Pinpoint Zoom
            map_url = f"https://www.google.com/maps?q={lat},{lon}&t=k&z=20"
            
            os.system(f'termux-tts-speak "Deepak sir, dual synchronization established. Accuracy verified."')
            os.system(f"termux-open-url '{map_url}'")
    except:
        print("\033[1;31m[FATAL]\033[0m All sensors offline. Please restart your device.")

if __name__ == "__main__":
    start_dual_sync()
