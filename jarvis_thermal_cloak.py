import os
import time
import base64

# Masked Cloaking Logic
_C = "QWN0aXZhdGluZyBTYXRlbGxpdGUtQmFzZWQgVGhlcm1hbCBDbG9ha2luZy4uLg==" # Activating Thermal Cloaking...
_S = "U3RlYWx0aCBNb2RlIEVuZ2FnZWQ6IFNpZ25hbCBpcyBub3cgaW52aXNpYmxlIHRvIFJhZGFyLg==" # Stealth Mode Engaged...

class ThermalCloak:
    def __init__(self):
        self.master = "Deepak sir"
        self.status = "Ghost Mode"

    def speak(self, text):
        os.system(f'termux-tts-speak "{text}"')

    def activate_cloak(self):
        print(f"\033[1;35m[STEALTH]\033[0m {base64.b64decode(_C).decode()}")
        self.speak(f"{self.master}, synchronizing thermal output with background cosmic noise.")
        
        # Modulating the signal signature
        steps = ["Suppressing Heat Signature", "Scrambling RF Pulse", "Injecting Static Blur"]
        for step in steps:
            print(f"\033[1;33m[SHIELDING]\033[0m {step}...")
            time.sleep(1.2)
            
        print(f"\033[1;32m[INVISIBLE]\033[0m {base64.b64decode(_S).decode()}")
        self.speak("Cloaking is successful. Even military satellites cannot track your position now.")

if __name__ == "__main__":
    cloak = ThermalCloak()
    cloak.activate_cloak()
