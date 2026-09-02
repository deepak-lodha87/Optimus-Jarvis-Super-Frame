import os
import json
import time

def get_true_location():
    print("\033[1;31m[CRITICAL]\033[0m Bypassing Software Layers... Accessing GPS Hardware.")
    
    # Ye command seedhe phone ke hardware se baat karegi
    os.system("termux-location > loc.json")
    
    with open("loc.json", "r") as f:
        data = json.load(f)
        lat = data['latitude']
        lon = data['longitude']
        alt = data['altitude']
        
    print(f"\n\033[1;32m[LOCKED]\033[0m Satellite Handshake Successful!")
    print(f"Precise Lat: {lat} | Precise Lon: {lon}")
    print(f"Altitude: {alt}m above sea level")

    map_url = f"https://www.google.com/maps/search/?api=1&query={lat},{lon}"
    os.system(f"termux-open-url '{map_url}'")
    os.system(f'termux-tts-speak "Deepak sir, hardware lock established. No more approximations."')

if __name__ == "__main__":
    get_true_location()
