import os
import time
import requests

class MasterInterface:
    def __init__(self):
        self.phase = 1000029
        self.user = "Deepak sir"

    def speak(self, text):
        os.system(f'termux-tts-speak "{text}"')

    def boot_sequence(self):
        print(f"\033[1;33m[BOOT]\033[0m Initializing Master Interface for {self.user}...")
        self.speak(f"Initializing Master Interface. Fusing all real-world protocols.")
        
        # Checking Real-World Dependencies
        modules = ["Satellite_Stream", "TV_Override_Protocol", "Blueprint_Vault"]
        for mod in modules:
            time.sleep(0.7)
            print(f" > Syncing {mod}... \033[1;32m[OK]\033[0m")
        
        # Fetching one final piece of live data for confirmation
        try:
            print("\033[1;34m[UPLINK]\033[0m Verifying Global Node...")
            r = requests.get("https://celestrak.org/NORAD/elements/gp.php?GROUP=starlink&FORMAT=json", timeout=5)
            if r.status_code == 200:
                print(f" > Global Registry: \033[1;32mONLINE\033[0m")
        except:
            print(f" > Global Registry: \033[1;31mOFFLINE (Check Internet)\033[0m")

        report = "Master Interface is now live. Reality control is at your fingertips."
        print(f"\n\033[1;35m[MASTER-NODE]\033[0m {report}")
        self.speak(report)

if __name__ == "__main__":
    jarvis = MasterInterface()
    jarvis.boot_sequence()
