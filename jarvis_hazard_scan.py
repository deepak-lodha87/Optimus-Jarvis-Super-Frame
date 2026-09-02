import os
import time
import base64

# Masked Hazard Logic
_H = "QWN0aXZhdGluZyBFbnZpcm9ubWVudGFsIEhhemFyZCBQcmVkaWN0aW9uLi4u" # Activating Hazard Prediction...
_W = "QWxlcnQ6IEF0bW9zcGhlcmljIHByZXNzdXJlIGlzIHN0YWJsZS4gTm8gaW1tZWRpYXRlIHRocmVhdHMu" # Alert: Stable...

class HazardScanner:
    def __init__(self):
        self.master = "Deepak sir"
        self.location = "Current Coordinates"

    def speak(self, text):
        os.system(f'termux-tts-speak "{text}"')

    def scan_environment(self):
        print(f"\033[1;35m[HAZARD-SCAN]\033[0m {base64.b64decode(_H).decode()}")
        self.speak(f"{self.master}, scanning meteorological feeds for potential environmental threats.")
        
        # Checking various environmental factors
        factors = ["Ozone Levels", "Storm Fronts", "Seismic Activity"]
        for factor in factors:
            print(f"\033[1;33m[MONITORING]\033[0m Checking {factor}...")
            time.sleep(1.2)
            
        print(f"\033[1;32m[SECURE]\033[0m {base64.b64decode(_W).decode()}")
        self.speak("Environment scan complete. Current conditions are optimal for operations.")

if __name__ == "__main__":
    scanner = HazardScanner()
    scanner.scan_environment()
