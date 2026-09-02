import os
import json
import time

def emergency_trace():
    os.system('clear')
    print("\033[1;31m[CRITICAL]\033[0m Optimus Jarvis: Initiating Emergency Override...")
    
    # Resetting the API Bridge
    os.system("termux-api-start")
    time.sleep(2)
    
    # Trying with Network first (Fastest)
    print("\033[1;33m[SCANNING]\033[0m Searching for Network Grid...")
    os.system("termux-location -p network > loc.json")
    
    if os.path.exists("loc.json") and os.stat("loc.json").st_size > 0:
        try:
            with open("loc.json", "r") as f:
                data = json.load(f)
                lat, lon = data['latitude'], data['longitude']
                print(f"\n\033[1;32m[SUCCESS]\033[0m Signal Intercepted: {lat}, {lon}")
                os.system(f"termux-open-url 'https://www.google.com/maps/search/?api=1&query={lat},{lon}&t=k'")
                return
        except:
            pass

    # If Network fails, use Raw GPS (Precision)
    print("\033[1;31m[FAIL]\033[0m Network failed. Forcing RAW GPS handshake...")
    os.system("termux-location -p gps > loc.json")
    # Yahan se code map open karega...
    
if __name__ == "__main__":
    emergency_trace()
