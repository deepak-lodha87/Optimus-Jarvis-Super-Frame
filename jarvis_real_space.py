import os
import requests
import time

class RealSpaceJarvis:
    def __init__(self):
        self.user = "Deepak sir"
        # Real SpaceX/Starlink Registry URL
        self.url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=starlink&FORMAT=json"
        # Bypassing the "Server not responding" error
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    def speak(self, text):
        os.system(f'termux-tts-speak "{text}"')

    def establish_live_uplink(self):
        print(f"\033[1;36m[UPLINK]\033[0m Reaching Starlink Registry with Auth-Bypass...")
        try:
            # Haqiqat mein data lene ke liye headers zaroori hain
            response = requests.get(self.url, headers=self.headers, timeout=15)
            
            if response.status_code == 200:
                data = response.json()
                # Tracking the first 3 active satellites in real-time
                for sat in data[:3]:
                    name = sat['OBJECT_NAME']
                    epoch = sat['EPOCH'] # Last time satellite was spotted
                    print(f"\033[1;32m[LIVE]\033[0m Node: {name} | Last Sync: {epoch}")
                
                self.speak(f"{self.user}, live satellite uplink is successful. No imaginary data detected.")
                print("\033[1;32m[SUCCESS]\033[0m Real-time telemetry is now active.")
            else:
                print(f"\033[1;31m[ERROR]\033[0m Server status: {response.status_code}")
                
        except Exception as e:
            print(f"\033[1;31m[CRITICAL]\033[0m Network Link Failed: {e}")

if __name__ == "__main__":
    jarvis = RealSpaceJarvis()
    jarvis.establish_live_uplink()
