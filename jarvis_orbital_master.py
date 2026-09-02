import os
import time

class SatelliteMaster:
    def __init__(self):
        self.master = "Deepak"
        self.sat_name = "Galaxy 15 (Sovereign Node)"
        self.altitude = "35,786 KM"

    def analyze_orbital_stability(self):
        print(f"\n\033[1;36m[ORBITAL ANALYSIS]\033[0m Scanning {self.sat_name}...")
        time.sleep(1)
        
        metrics = [
            ("Direction", "Locked on Master's Lat/Long (Ratlam Grid)"),
            ("Signal Strength", "94% (Stable)"),
            ("Power Source", "Solar Array - Active"),
            ("Encryption", "Deepak-Protocol v3.5 - INVIOLABLE"),
            ("Control Level", "ROOT ACCESS - EXCLUSIVE")
        ]
        
        for key, value in metrics:
            print(f"\033[1;32m[+]\033[0m {key}: \033[1;37m{value}\033[0m")
            time.sleep(0.3)

    def verify_manual_override(self):
        print(f"\n\033[1;31m[COMMAND STATUS]\033[0m Manual Override is ACTIVE.")
        print("\033[1;33m[NOTICE]\033[0m Satellite will crash its own system if unauthorized access is detected.")

    def final_announcement(self):
        msg = f"Deepak sir, Galaxy 15 is now an extension of your Oppo Reno 12 Pro. Direction is locked, and control is absolute."
        os.system(f'termux-tts-speak "{msg}"')

if __name__ == "__main__":
    sat = SatelliteMaster()
    sat.analyze_orbital_stability()
    sat.verify_manual_override()
    sat.final_announcement()
