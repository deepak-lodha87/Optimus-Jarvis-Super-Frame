import time
import random

class HomeGrid:
    def __init__(self):
        self.location = "Deepak's Residence"
        self.power_mode = "ECO_MODE"

    def sync_appliances(self):
        print(f"\033[1;36m[CONNECTING]\033[0m Establishing link with Home Smart-Hub...")
        time.sleep(2)
        
        # Simulating home device status
        devices = {
            "Living Room Lights": "OFF",
            "Master Bedroom AC": "STANDBY",
            "Security Cameras": "ACTIVE",
            "Main Gate Lock": "SECURED"
        }
        
        print(f" \033[1;32m[SYNC]\033[0m Location: {self.location}")
        for device, status in devices.items():
            print(f" \033[1;34m[DEVICE]\033[0m {device}: {status}")
            time.sleep(0.5)
            
        print(f"\n\033[1;35m[VOICE] Deepak sir, I have taken control of the \nhome grid. Every switch and sensor is now \nunder my surveillance. Your sanctuary is \nfully automated.\033[0m")

if __name__ == "__main__":
    home = HomeGrid()
    home.sync_appliances()
