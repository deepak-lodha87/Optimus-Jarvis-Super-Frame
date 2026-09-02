import os
import time
import random

class SatelliteLink:
    def __init__(self):
        self.master = "Deepak"
        self.sat_name = "STARK-ENT-01"

    def establish_uplink(self):
        print(f"\n\033[1;34m[UPLINK]\033[0m Connecting to {self.sat_name}...")
        time.sleep(1.5)
        print("\033[1;32m[SUCCESS]\033[0m Secure Handshake Confirmed.")

    def render_map(self):
        try:
            for _ in range(25):
                os.system('clear')
                lat = 23.33 + random.uniform(-0.01, 0.01) # रतलाम/कोटा रीजन सिमुलेशन
                lon = 75.03 + random.uniform(-0.01, 0.01)
                
                print(f"\033[1;36m      E.D.I.T.H. SATELLITE FEED | LIVE RECON")
                print("      ======================================\033[0m\n")
                
                # सैटेलाइट ग्रिड विज़ुअल
                for y in range(10):
                    line = "                "
                    for x in range(20):
                        if random.random() > 0.9:
                            line += "\033[1;31mX\033[0m" # टारगेट मार्क
                        else:
                            line += "\033[1;30m+\033[0m"
                    print(line)
                
                print(f"\n\033[1;37m      LAT: {lat:.4f} | LON: {lon:.4f}")
                print(f"      ALTITUDE: 450km | RESOLUTION: 0.5m\033[0m")
                time.sleep(0.15)
            
            msg = f"Deepak sir, E.D.I.T.H. link is online. I have a bird's-eye view of your surroundings. No movement goes unnoticed."
            os.system(f'termux-tts-speak "{msg}"')

        except KeyboardInterrupt:
            pass

if __name__ == "__main__":
    sat = SatelliteLink()
    sat.establish_uplink()
    sat.render_map()
