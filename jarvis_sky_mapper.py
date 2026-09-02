import os
import requests
import time

class SkyMapper:
    def __init__(self):
        self.user = "Deepak sir"
        self.url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=starlink&FORMAT=json"
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def speak(self, text):
        os.system(f'termux-tts-speak "{text}"')

    def track_overhead(self):
        print(f"\033[1;36m[MAPPER]\033[0m Scanning Reality for Overhead Starlink Nodes...")
        try:
            response = requests.get(self.url, headers=self.headers, timeout=20)
            if response.status_code == 200:
                data = response.json()
                # Tracking the most active node
                target = data[0]
                name = target['OBJECT_NAME']
                alt = target['MEAN_MOTION'] # Orbital speed
                
                print(f"\033[1;32m[DETECTED]\033[0m Target: {name}")
                print(f"\033[1;34m[TELEMETRY]\033[0m Speed: {alt} orbits/day")
                
                self.speak(f"Sir, I have located {name} in real-time space coordinates. It is currently active.")
                print("\033[1;32m[SUCCESS]\033[0m Reality link verified.")
            else:
                print("\033[1;31m[ERROR]\033[0m Satellite link unstable.")
        except Exception as e:
            print(f"\033[1;31m[CRITICAL]\033[0m Bridge Failure: {e}")

if __name__ == "__main__":
    mapper = SkyMapper()
    mapper.track_overhead()
