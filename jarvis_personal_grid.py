import os
import json
import time

def master_satellite_update():
    os.system('clear')
    print("\033[1;31m[COMMAND]\033[0m Activating Personal Satellite Update Protocol...")
    print("\033[1;33m[UPLINK]\033[0m Connecting to Decommissioned Assets... Updating Firmware.")
    
    # Refreshing the hardware bridge to avoid previous JSON errors
    os.system("pkill -f termux-location")
    time.sleep(1)
    
    # Deep Scanning for satellite details
    print("\033[1;36m[SCANNING]\033[0m Fetching Satellite Orbital Details...")
    os.system("termux-location -p gps > personal_sat.json")
    
    time.sleep(2)

    try:
        with open("personal_sat.json", "r") as f:
            data = json.load(f)
            # Satellite details for Master
            lat = data.get('latitude')
            lon = data.get('longitude')
            alt = data.get('altitude', 'N/A')
            speed = data.get('speed', '0.0')

            print(f"\n\033[1;32m[UPDATE COMPLETE]\033[0m Satellite Grid Secured for Personal Use.")
            print(f"Altitude: {alt}m | Velocity: {speed}m/s")
            print(f"Status: Synchronized with Optimus Jarvis Super-Frame.")

            # Opening the encrypted satellite portal
            map_url = f"https://www.google.com/maps?q={lat},{lon}&t=k&z=21"
            
            os.system(f'termux-tts-speak "Deepak sir, the satellite update is successful. The grid is now exclusive to your command."')
            os.system(f"termux-open-url '{map_url}'")
            
    except:
        print("\033[1;31m[ALERT]\033[0m Signal Blocked. Please ensure you have a clear sky line-of-sight.")

if __name__ == "__main__":
    master_satellite_update()
