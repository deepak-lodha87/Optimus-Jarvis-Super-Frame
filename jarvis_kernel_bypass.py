import os
import json
import time

def force_system_reboot():
    os.system('clear')
    print("\033[1;31m[CRITICAL]\033[0m Executing Kernel Bypass... Purging stale buffers.")
    
    # Cleaning old files
    if os.path.exists("loc.json"):
        os.remove("loc.json")

    # Restarting API bridge
    print("\033[1;33m[RESTARTING]\033[0m Termux API Service Bridge...")
    os.system("termux-api-start")
    time.sleep(3)

    # Forcing location fetch with maximum timeout
    print("\033[1;36m[SEARCHING]\033[0m Pinging Satellites... Please stay under open sky if possible.")
    os.system("termux-location -p gps > loc.json")

    if os.path.exists("loc.json") and os.stat("loc.json").st_size > 0:
        try:
            with open("loc.json", "r") as f:
                data = json.load(f)
                lat, lon = data['latitude'], data['longitude']
                acc = data.get('accuracy', 'Unknown')
                
                print(f"\n\033[1;32m[LOCKED]\033[0m Accuracy: {acc} meters.")
                print(f"Coordinates: {lat}, {lon}")
                
                # Opening map with pinpoint accuracy
                map_url = f"https://www.google.com/maps/search/?api=1&query={lat},{lon}&t=k&z=19"
                os.system(f'termux-tts-speak "Deepak sir, kernel bypass successful. Location locked."')
                os.system(f"termux-open-url '{map_url}'")
                return
        except:
            pass

    print("\033[1;31m[FATAL ERROR]\033[0m Hardware still locked. Manual intervention required.")

if __name__ == "__main__":
    force_system_reboot()
