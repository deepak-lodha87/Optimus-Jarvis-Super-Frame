import os
import json
import time

def get_location():
    print("\033[1;31m[CRITICAL]\033[0m Activating Satellite Interceptor...")
    
    # Force updating the location data to a file
    os.system("termux-location > loc.json")
    
    # Check if file is empty or not created
    if not os.path.exists("loc.json") or os.stat("loc.json").st_size == 0:
        print("\033[1;33m[ALERT]\033[0m GPS hardware not responding. Please enable Location in Settings.")
        return

    try:
        with open("loc.json", "r") as f:
            data = json.load(f)
            lat = data.get('latitude')
            lon = data.get('longitude')
            
            if lat and lon:
                print(f"\n\033[1;32m[LOCKED]\033[0m Target Coordinates: {lat}, {lon}")
                # Direct Map marker with Pinpoint
                map_url = f"https://www.google.com/maps/search/?api=1&query={lat},{lon}"
                
                os.system(f'termux-tts-speak "Deepak sir, hardware lock established. Opening the exact grid."')
                os.system(f"termux-open-url '{map_url}'")
            else:
                print("\033[1;31m[ERROR]\033[0m Signal weak. Move to an open area.")

    except Exception as e:
        print(f"\033[1;31m[FAILED]\033[0m Data packet corrupted. Retrying...")

if __name__ == "__main__":
    get_location()
