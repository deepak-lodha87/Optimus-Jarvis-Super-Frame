import os
import json
import time

def satellite_lock():
    os.system('clear')
    print("\033[1;31m[SATELLITE COMMAND]\033[0m Disengaging Mobile Tracing... Shifting to 100% Satellite Focus.")
    
    # Cleaning environment for pure GPS signal
    os.system("pkill -f termux-location")
    
    print("\033[1;33m[SIGNAL]\033[0m Searching for Orbital Satellites...")
    # Force pure GPS provider (-p gps)
    os.system("termux-location -p gps > sat_data.json")
    
    time.sleep(3)

    try:
        if os.path.exists("sat_data.json") and os.stat("sat_data.json").st_size > 0:
            with open("sat_data.json", "r") as f:
                data = json.load(f)
                lat, lon = data['latitude'], data['longitude']
                satellites = data.get('satellites', 'Direct Lock')
                
                print(f"\n\033[1;32m[ORBITAL LOCK]\033[0m Target Coordinates: {lat}, {lon}")
                print(f"Status: Connected via {satellites} Satellites.")
                
                # Maximum Satellite View Zoom (z=21, t=k)
                map_url = f"https://www.google.com/maps/search/?api=1&query={lat},{lon}&t=k&z=21"
                
                os.system(f'termux-tts-speak "Deepak sir, satellite synchronization complete. Mobile tracing disengaged as per protocol."')
                os.system(f"termux-open-url '{map_url}'")
                return

        print("\033[1;31m[ERROR]\033[0m No direct satellite line-of-sight. Please move to a window.")
    except:
        print("\033[1;31m[SYSTEM]\033[0m Hardware bypass required. Check GPS switch.")

if __name__ == "__main__":
    satellite_lock()
