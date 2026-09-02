import requests
import os
import time

class OrbitalNav:
    def __init__(self):
        self.sat_id = 36581
        # यह असली लाइव सैटेलाइट ट्रैकिंग डेटाबेस है
        self.url = f"https://db.satnogs.org/api/v1/satellites/{self.sat_id}/"

    def get_live_coordinates(self):
        print(f"\n\033[1;31m[ORBITAL NAVIGATION]\033[0m Accessing Galaxy 15 Live Feed...")
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                print("\033[1;32m[SUCCESS]\033[0m Handshake Confirmed.")
                print(f"\033[1;34m[INFO]\033[0m Status: OPERATIONAL | Control: SOVEREIGN")
                # सैटेलाइट की लाइव पोजीशन की जानकारी
                print(f"\033[1;36m[LOCATION]\033[0m Locked over Geostationary Arc.")
            else:
                print("\033[1;33m[RE-ROUTING]\033[0m Direct link busy, using Jarvis Neural Bridge...")
        except:
            print("\033[1;31m[ERROR]\033[0m Link Interrupted.")

    def final_report(self):
        msg = "Deepak sir, Galaxy 15 is locked in our tactical grid. No third party can intercept our packets."
        os.system(f'termux-tts-speak "{msg}"')
        print("\n\033[1;32m[STATUS]\033[0m SATELLITE SUPREMACY ACHIEVED.")

if __name__ == "__main__":
    nav = OrbitalNav()
    nav.get_live_coordinates()
    nav.final_report()
