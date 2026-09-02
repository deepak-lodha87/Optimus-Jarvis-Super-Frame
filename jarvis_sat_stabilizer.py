import os
import json
import time

def stabilize_signal():
    os.system('clear')
    print("\033[1;31m[VANGUARD]\033[0m Satellite Stabilization Mode: ACTIVE.")
    print("\033[1;33m[ADVICE]\033[0m Deepak sir, please stand under the open sky.")
    
    # Infinite loop until accurate lock is achieved
    while True:
        os.system("termux-location -p gps -n 1 > sat_lock.json")
        
        if os.path.exists("sat_lock.json") and os.stat("sat_lock.json").st_size > 0:
            with open("sat_lock.json", "r") as f:
                data = json.load(f)
                lat, lon = data.get('latitude'), data.get('longitude')
                acc = data.get('accuracy')
                
                if lat and lon:
                    print(f"\n\033[1;32m[STABLE LOCK]\033[0m Accuracy: {acc} meters.")
                    map_url = f"https://www.google.com/maps/search/?api=1&query={lat},{lon}&t=k&z=21"
                    os.system(f'termux-tts-speak "Signal stabilized. Grid locked at {acc} meters precision."')
                    os.system(f"termux-open-url '{map_url}'")
                    break
        
        print("\033[1;31m[SEARCHING]\033[0m Signal weak. Retrying in 5 seconds...")
        time.sleep(5)

if __name__ == "__main__":
    stabilize_signal()
