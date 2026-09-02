import os
import json
import time

class SatelliteJCB:
    def __init__(self):
        self.master = "Deepak sir"
        self.status = "OFFLINE"

    def update_orbital_firmware(self):
        os.system('clear')
        print("\033[1;31m[JCB-CORE]\033[0m Scanning for decommissioned satellite hardware...")
        time.sleep(1)
        
        # Simulating the connection to old satellite grid
        print("\033[1;33m[UPLINK]\033[0m Handshake established. Accessing Legacy Firmware...")
        
        # Security Patch: Locking out other companies
        print("\033[1;36m[SECURITY]\033[0m Injecting Personal Firewall... Lock 100% complete.")
        
        # Getting the high-precision satellite coordinates
        os.system("termux-location -p gps -n 1 > update_sat.json")
        
        try:
            with open("update_sat.json", "r") as f:
                data = json.load(f)
                lat, lon = data['latitude'], data['longitude']
                
                print(f"\n\033[1;32m[SYSTEM UPDATE SUCCESSFUL]\033[0m")
                print(f"Satellite ID: JCB-ORBIT-01 | Status: SECURED")
                print(f"Coordinates Locked: {lat}, {lon}")
                
                # Opening satellite view for Master
                map_url = f"https://www.google.com/maps/search/?api=1&query={lat},{lon}&t=k&z=21"
                
                os.system(f'termux-tts-speak "{self.master}, the satellite firmware has been updated for personal use. Access is now exclusive to Optimus Jarvis Super-Frame."')
                os.system(f"termux-open-url '{map_url}'")
        except:
            print("\033[1;31m[ALERT]\033[0m Update failed. Ensure you are under clear sky for a direct uplink.")

if __name__ == "__main__":
    SatelliteJCB().update_orbital_firmware()
