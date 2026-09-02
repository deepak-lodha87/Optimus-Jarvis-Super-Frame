import os
import json
import time

def execute_vanguard_protocol():
    os.system('clear')
    print("\033[1;31m[VANGUARD]\033[0m Initiating Force-Handshake with GPS Hardware...")
    
    # Cleaning any stuck background process
    os.system("pkill termux-api")
    time.sleep(1)
    os.system("termux-api-start")
    
    print("\033[1;33m[SYNC]\033[0m Waiting for Satellite Lock... (This may take 15 seconds)")
    
    # We use -p network as a backup if GPS fails
    os.system("termux-location -p gps -n 1 > loc.json")
    
    if not os.path.exists("loc.json") or os.stat("loc.json").st_size == 0:
        print("\033[1;36m[RETRY]\033[0m GPS weak. Switching to Network Triangulation...")
        os.system("termux-location -p network > loc.json")

    try:
        with open("loc.json", "r") as f:
            data = json.load(f)
            lat, lon = data['latitude'], data['longitude']
            
            print(f"\n\033[1;32m[SYSTEM UNLOCKED]\033[0m Precision Coordinates: {lat}, {lon}")
            
            # Using absolute direct Google Maps link with max zoom
            map_url = f"https://www.google.com/maps/search/?api=1&query={lat},{lon}"
            
            os.system(f'termux-tts-speak "Deepak sir, hardware lock bypassed. System integrity at 100 percent."')
            os.system(f"termux-open-url '{map_url}'")
    except:
        print("\033[1;31m[CRITICAL FAILURE]\033[0m System still locked. Please restart your phone.")

if __name__ == "__main__":
    execute_vanguard_protocol()
