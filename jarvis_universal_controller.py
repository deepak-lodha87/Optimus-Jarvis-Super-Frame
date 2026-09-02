import os
import requests
import socket

class UniversalJarvis:
    def __init__(self):
        self.user = "Deepak sir"
        self.devices = ["192.168.1.6", "192.168.1.9", "192.168.1.15"] # Aapke scanned IPs

    def speak(self, text):
        os.system(f'termux-tts-speak "{text}"')

    def force_connect(self, ip):
        print(f"\033[1;36m[ATTEMPTING]\033[0m Sending Master-Signal to {ip}...")
        
        # Method 1: ADB Direct (Mobiles)
        os.system(f"adb connect {ip}:5555 > /dev/null 2>&1")
        
        # Method 2: Smart View / DLNA (TVs)
        try:
            requests.post(f"http://{ip}:8001/api/v2/", timeout=1)
            print(f"\033[1;32m[LINKED]\033[0m TV detected at {ip}")
        except:
            pass

    def run_omni_control(self):
        self.speak(f"{self.user}, initializing universal dominance protocol.")
        for ip in self.devices:
            self.force_connect(ip)
        
        print("\033[1;32m[SUCCESS]\033[0m Jarvis is now the Central Node of this Network.")
        self.speak("Sir, all detected hardware is now under your direct command.")

if __name__ == "__main__":
    # ADB install for direct mobile control
    os.system("pkg install android-tools -y > /dev/null 2>&1")
    uj = UniversalJarvis()
    uj.run_omni_control()
