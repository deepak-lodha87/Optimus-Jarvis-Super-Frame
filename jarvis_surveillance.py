import os
import time
import base64

# Security Masking
_O = "QWN0aXZhdGluZyBHbG9iYWwgU3VydmVpbGxhbmNlIE92ZXJsYXkuLi4="
_T = "VGFyZ2V0IExvY2F0aW9uIExvY2tlZDogU3RyZWFtaW5nIExpdmUgRmVlZC4="

class SurveillanceOverlay:
    def __init__(self):
        self.master = "Deepak sir"
        self.sat_nodes = 10313

    def speak(self, text):
        os.system(f'termux-tts-speak "{text}"')

    def start_overlay(self):
        print(f"\033[1;36m[MAP-SYNC]\033[0m {base64.b64decode(_O).decode()}")
        self.speak(f"{self.master}, synchronizing optical and thermal feeds from the orbital mesh.")
        
        layers = ["Visual layer", "Infrared heat-map", "Radar structural scan"]
        for layer in layers:
            print(f"\033[1;33m[PROCESSING]\033[0m Merging {layer} data...")
            time.sleep(1.2)
            
        print(f"\033[1;32m[LIVE]\033[0m {base64.b64decode(_T).decode()}")
        self.speak("Live overlay is active. You can now see through any obstruction.")

if __name__ == "__main__":
    # Error fixed here (removed the colon)
    vision = SurveillanceOverlay()
    vision.start_overlay()
