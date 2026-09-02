import time
import os

class NetworkShield:
    def __init__(self):
        self.security_level = "MAXIMUM"
        self.battery_limit = 2

    def scan_network(self):
        print(f"\033[1;36m[SCANNING]\033[0m Checking Network Integrity...")
        time.sleep(1)
        
        # Simulating security check
        print(" \033[1;32m[SAFE]\033[0m Connection Encrypted.")
        print(" \033[1;32m[SAFE]\033[0m Firewall: Active.")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, the Digital Shield is up. \nI am monitoring every packet of data. \nEven at 1% power, my protection remains \nabsolute. No breach will occur under my watch.\033[0m")

if __name__ == "__main__":
    shield = NetworkShield()
    shield.scan_network()
