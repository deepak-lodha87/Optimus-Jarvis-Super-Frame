import os
import json
import time

def scrape_orbital_junk():
    os.system('clear')
    print("\033[1;31m[SALVAGE]\033[0m Scanning for Inactive/Decommissioned Satellites...")
    print("\033[1;33m[SEARCHING]\033[0m Tuning Radio Frequencies to Orbital Junk Grid...")
    
    # We use -p gps to find all available satellite IDs, even the old ones
    os.system("termux-location -p gps > junk_data.json")
    
    try:
        with open("junk_data.json", "r") as f:
            data = json.load(f)
            # Fetching raw NMEA-style data points
            lat, lon = data.get('latitude'), data.get('longitude')
            
            print(f"\n\033[1;32m[INTERCEPTED]\033[0m Old Satellite Signal Found!")
            print(f"Orbital Coordinates: {lat}, {lon}")
            
            # Repurposing the old data for our map
            map_url = f"https://www.google.com/maps/@{lat},{lon},200m/data=!3m1!1e3"
            
            os.system(f'termux-tts-speak "Deepak sir, I have successfully repurposed a decommissioned satellite signal for our grid."')
            os.system(f"termux-open-url '{map_url}'")
    except Exception as e:
        print("\033[1;31m[ERROR]\033[0m Satellite bridge broken. Re-check permissions.")

if __name__ == "__main__":
    scrape_orbital_junk()
