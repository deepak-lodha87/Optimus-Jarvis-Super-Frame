import os
import time
import requests  # Ab ye library aapke system mein hai!

class RealityControl:
    def __init__(self):
        self.phase = 1000026
        self.user = "Deepak sir"

    def speak(self, text):
        os.system(f'termux-tts-speak "{text}"')

    def execute_real_command(self):
        print(f"\033[1;32m[SYSTEM]\033[0m Reality Bridge is ACTIVE.")
        self.speak(f"{self.user}, establishing real-world link.")
        
        # Testing the link with a Live Satellite Server
        print(f"\033[1;34m[LIVE]\033[0m Fetching real-time Starlink metadata...")
        try:
            # Asli internet request
            url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=starlink&FORMAT=json"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                print(f"\033[1;32m[SUCCESS]\033[0m Linked with Orbital Registry.")
                self.speak("Deepak sir, the connection is real. I am now reading live satellite positions.")
                # Asli data ka ek hissa dikhana
                data = response.json()
                print(f" > Currently Tracking: {data[0]['OBJECT_NAME']}")
            else:
                print("\033[1;31m[FAILED]\033[0m Server returned an error.")
        except Exception as e:
            print(f"\033[1;31m[ERROR]\033[0m Connection failed: {e}")

if __name__ == "__main__":
    rc = RealityControl()
    rc.execute_real_command()
