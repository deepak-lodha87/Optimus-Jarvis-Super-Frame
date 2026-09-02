import time
import random

class WirelessPower:
    def __init__(self):
        self.charging_status = "IDLE"
        self.source = "NONE"

    def scan_for_signals(self):
        print(f"\033[1;36m[SCANNER]\033[0m Detecting ambient electromagnetic waves...")
        time.sleep(1.5)
        
        signals = ["Wi-Fi 6", "5G-Tower", "Satellite-Beam", "Radio-Waves"]
        self.source = random.choice(signals)
        self.charging_status = "CHARGING (WIRELESS)"
        
        print(f" \033[1;32m[FOUND]\033[0m High-frequency source: {self.source}")
        print(f" \033[1;33m[ACTION]\033[0m Converting RF waves to electrical energy...")
        
        for i in range(1, 6):
            print(f" Energy Inflow: +{i*2}mA...")
            time.sleep(0.3)
            
        print(f"\n\033[1;35m[VOICE] Deepak sir, I am now drawing power from the \nair around us. The environment is our charger. \nYour system will never go dark again.\033[0m")

if __name__ == "__main__":
    wp = WirelessPower()
    wp.scan_for_signals()
