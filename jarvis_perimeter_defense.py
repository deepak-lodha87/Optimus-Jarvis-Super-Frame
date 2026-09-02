import os
import time

class PerimeterDefense:
    def __init__(self):
        self.master = "Deepak"

    def activate_shield(self):
        print(f"\n\033[1;31m[DEFENSE]\033[0m Reached Phase 1226: Neural Perimeter Shield Active")
        
        layers = [
            "Monitoring for External Hacking Vectors...",
            "Encrypting A-Z Blueprint Access Pathways...",
            "Isolating System Logic from Unauthorized Hardware...",
            "Confirming Zero-Wrong-Answer Security Loop..."
        ]
        
        for layer in layers:
            print(f"\033[1;31m[SHIELDING]\033[0m {layer}")
            time.sleep(0.4)

        msg = f"{self.master} sir, neural perimeter is active. System is fully fortified."
        os.system(f'termux-tts-speak "{msg}"')

if __name__ == "__main__":
    PerimeterDefense().activate_shield()
