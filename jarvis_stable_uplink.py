import os
import requests
import time

class PersistentJarvis:
    def __init__(self):
        self.user = "Deepak sir"
        self.url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=starlink&FORMAT=json"
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def speak(self, text):
        os.system(f'termux-tts-speak "{text}"')

    def connect_with_retries(self, max_attempts=3):
        print(f"\033[1;36m[UPLINK]\033[0m Initializing stable link to Starlink Core...")
        
        for i in range(max_attempts):
            try:
                # Increased timeout to 30 seconds to prevent "Read timed out"
                response = requests.get(self.url, headers=self.headers, timeout=30)
                
                if response.status_code == 200:
                    data = response.json()
                    print(f"\033[1;32m[SUCCESS]\033[0m Reality Link Active! {len(data)} satellites synced.")
                    self.speak(f"{self.user}, connection is stable now.")
                    return data
                
            except requests.exceptions.Timeout:
                print(f"\033[1;33m[RETRYING]\033[0m Attempt {i+1} timed out. Re-stabilizing...")
                time.sleep(2)
            except Exception as e:
                print(f"\033[1;31m[ERROR]\033[0m Critical failure: {e}")
                break
        
        self.speak("Sir, the server is extremely busy. I suggest we wait 60 seconds.")
        return None

if __name__ == "__main__":
    jarvis = PersistentJarvis()
    jarvis.connect_with_retries()
