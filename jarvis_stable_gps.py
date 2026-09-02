import os
import json
import time

def get_true_location():
    print("\033[1;31m[SYSTEM]\033[0m Accessing Satellite Hardware...")
    
    # Force updating the location data
    os.system("termux-location > loc.json")
    
    if os.stat("loc.json").st_size == 0:
        print("\033[1;33m[ERROR]\033[0m Satellite signal weak or Permission denied.")
        return

    try:
        with open("loc.json", "r") as f:
            data = json.load(f)
            lat, lon = data['latitude'], data['longitude']
            
        print(f"\n\033[1;32m[SUCCESS]\033[0m Target Locked: {lat}, {lon}")
        map_url = f"https://www.google.com/maps/search/?api=1&query={lat},{lon}"
        os.system(f"termux-open-url '{map_url}'")
        
    except Exception as e:
        print(f"\033[1;31m[FAILED]\033[0m Data packet corrupted. Restarting sensor...")

if __name__ == "__main__":
    get_true_location()
