import os
import time
import base64
import random

# Advanced Interception Logic (No repetition)
_S = "U2Nhbm5pbmcgQWlyd2F2ZXMgZm9yIFNpZ25hbCBQYWNrZXRzLi4u" # Scanning Airwaves...
_D = "RGVjb2RpbmcgUGFja2V0czogU2lnbmFsIGlzIG5vdyB0cmFuc3BhcmVudC4=" # Decoding Packets...

class SignalInterceptor:
    def __init__(self):
        self.master = "Deepak sir"
        self.sat_power = "10,313 Nodes Active"

    def speak(self, text):
        os.system(f'termux-tts-speak "{text}"')

    def capture_and_decode(self):
        print(f"\033[1;36m[RF-SYNC]\033[0m {base64.b64decode(_S).decode()}")
        self.speak(f"{self.master}, synchronizing wireless hardware with the orbital grid.")
        
        # Simulating brute-force packet decryption
        frequencies = ["Wi-Fi WPA3", "UHF Military Radio", "BLE Smart-Link"]
        for freq in frequencies:
            strength = random.randint(70, 99)
            print(f"\033[1;33m[INTERCEPTING]\033[0m {freq} | Strength: {strength}%")
            time.sleep(1)
            
        print(f"\033[1;32m[ACCESS]\033[0m {base64.b64decode(_D).decode()}")
        self.speak("Universal signal decryption is active. Every byte in the air is now visible to us.")

if __name__ == "__main__":
    rf_module = SignalInterceptor()
    rf_module.capture_and_decode()
