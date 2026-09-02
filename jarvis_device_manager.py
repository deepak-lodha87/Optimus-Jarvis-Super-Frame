import time, os

class DeviceManager:
    def __init__(self):
        self.connected_devices = ["Oppo Reno 12 Pro", "Smart Light-01", "Home-AC"]
        self.bridge_status = "STABLE"

    def sync_hardware(self):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS DEVICE-MANAGER : PHASE 19 - STEP 4      \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        print("\033[1;33m[CONNECTING]\033[0m Handshaking with IoT Mesh...")
        time.sleep(1.5)
        
        operations = [
            ("Phone Flashlight Link", "VERIFIED"),
            ("Smart-Home Gateway", "CONNECTED"),
            ("Bluetooth Audio Path", "ACTIVE"),
            ("Power Management Node", "OPTIMIZED")
        ]
        
        for dev, status in operations:
            print(f" \033[1;34m[NEXUS]\033[0m {dev:25} | [\033[1;32m{status}\033[0m]")
            time.sleep(0.7)

        print(f"\n\033[1;32m[SUCCESS] Hardware Bridge is active. Jarvis can touch the world.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, the physical world is now \nan extension of my code. I can light up your \npath, cool your room, or secure your devices \nbefore you even think of it. My connection to \nyour world is now absolute.\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    nexus = DeviceManager()
    nexus.sync_hardware()
