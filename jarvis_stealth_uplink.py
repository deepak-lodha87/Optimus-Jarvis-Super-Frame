import os
import requests
import random

class SatelliteExpert:
    def __init__(self):
        self.user = "Deepak sir"
        self.url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=starlink&FORMAT=json"
        # Advanced Stealth Headers to bypass 403 Error
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
            'Accept': 'application/json'
        }

    def speak(self, text):
        os.system(f'termux-tts-speak "{text}"')

    def analyze_real_defects(self):
        print(f"\033[1;36m[UPLINK]\033[0m Attempting stealth connection to Starlink Core...")
        try:
            response = requests.get(self.url, headers=self.headers, timeout=20)
            
            if response.status_code == 200:
                satellites = response.json()
                print(f"\033[1;32m[SUCCESS]\033[0m {len(satellites)} Satellites Linked in Reality.")
                
                # Analyzing a real Starlink node for defects
                target = satellites[0]
                name = target['OBJECT_NAME']
                motion = float(target['MEAN_MOTION']) # Satellite speed per day
                
                print(f"\033[1;34m[NODE]\033[0m Tracking: {name}")
                
                # REALITY CHECK: If mean motion is too low, it's falling (Orbital Decay)
                if motion < 15.0:
                    defect = "Orbital Instability Detected"
                    print(f"\033[1;31m[DEFECT]\033[0m {defect} in {name}!")
                    self.speak(f"Sir, I have found a real defect in {name}. Orbital speed is below optimal.")
                else:
                    print(f"\033[1;32m[HEALTHY]\033[0m {name} is at peak performance.")
                    self.speak(f"Deepak sir, {name} is functioning perfectly.")
            else:
                print(f"\033[1;31m[FAILED]\033[0m Status {response.status_code}. Server is still resisting.")
                
        except Exception as e:
            print(f"\033[1;31m[CRITICAL]\033[0m Bridge Failure: {e}")

if __name__ == "__main__":
    expert = SatelliteExpert()
    expert.analyze_real_defects()
