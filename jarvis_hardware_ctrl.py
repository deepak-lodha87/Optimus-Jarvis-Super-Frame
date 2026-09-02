import time

class HardwareController:
    def __init__(self):
        self.battery_level = 85  # Simulated battery
        self.storage_free = "12GB"

    def access_hardware(self, component):
        print(f"\033[1;36m[HARDWARE]\033[0m Connecting to {component}...")
        time.sleep(1.5)
        
        if component == "Flashlight":
            print(" \033[1;33m[ACTION]\033[0m Lumos Protocol Activated. Torch is ON.")
        elif component == "Battery":
            print(f" \033[1;32m[STATUS]\033[0m Battery is at {self.battery_level}%. Systems are Nominal.")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, I have established a secure link \nwith your device hardware. Your mobile is \nnow an extension of my core. Everything \nis under control.\033[0m")

if __name__ == "__main__":
    ctrl = HardwareController()
    ctrl.access_hardware("Battery")
    ctrl.access_hardware("Flashlight")
