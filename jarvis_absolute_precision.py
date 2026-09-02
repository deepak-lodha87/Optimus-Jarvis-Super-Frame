import os
import json
import time
import subprocess

def get_live_handshake():
    os.system('clear')
    print("\033[1;31m[VANGUARD]\033[0m Forcing Raw Sensor Stream... Purging Cache.")
    
    # Direct command execution to bypass file-save lag
    try:
        # Requesting location with a 20-second timeout for accuracy
        print("\033[1;33m[SYNC]\033[0m Pinging Satellites. Please wait 15 seconds...")
        result = subprocess.check_output(["termux-location", "-p", "gps", "-n", "1"])
        data = json.loads(result)
        
        lat = data.get('latitude')
        lon = data.get('longitude')
        acc = data.get('accuracy')
        
        if lat and lon:
            print(f"\n\033[1;32m[LOCKED]\033[0m Accuracy: {acc} meters.")
            print(f"Coordinates: {lat}, {lon}")
            
            # Map with High-Resolution Satellite View
            map_url = f"https://www.google.com/maps/search/?api=1&query={lat},{lon}&t=k"
            
            os.system(f'termux-tts-speak "Deepak sir, coordinate lock achieved. System integrity restored."')
            os.system(f"termux-open-url '{map_url}'")
        else:
            print("\033[1;31m[FAIL]\033[0m Data received but coordinates missing.")
            
    except Exception as e:
        print("\033[1;31m[SYSTEM ERROR]\033[0m Hardware Bridge still unresponsive.")
        print("Tip: Restart your phone to clear Android Kernel lock.")

if __name__ == "__main__":
    get_live_handshake()
