import time, os

class JarvisSkyEye:
    def __init__(self):
        self.version = "1,000,000+ PHASES"
        self.orbital_status = "STABLE"

    def engage_satellite_uplink(self):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS SKY-EYE : PHASE 11 - STEP 4             \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        feeds = [
            ("LEO Satellite Constellation", "CONNECTED"),
            ("Thermal Infrared Mapping", "ONLINE"),
            ("SAR Radar Penetration", "ACTIVE"),
            ("Deepak-Prime Surveillance-Auth", "AUTHORIZED")
        ]
        
        for feed, status in feeds:
            print(f" \033[1;33m[UPLINK]\033[0m {feed:28} | Status: [\033[1;32m{status}\033[0m]")
            time.sleep(0.7)

        print(f"\n\033[1;32m[SYSTEM] Sky-Eye Live. Monitoring Global Threat Level: GREEN.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I have established a direct \nlink with the orbital grid. The entire planet is \nnow under our watch. Nothing moves on the surface \nwithout my knowledge. I am monitoring signals, \nheat signatures, and satellite feeds in real-time. \nYou have the ultimate high ground, sir.\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    eye = JarvisSkyEye()
    eye.engage_satellite_uplink()
