import time, os

class JarvisNavigator:
    def __init__(self):
        self.version = "1,000,000+ PHASES"
        self.sat_count = 12
        self.status = "FIXING-LOCATION"

    def activate_global_tracking(self):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS GLOBAL NAVIGATOR : PHASE 10 - STEP 3    \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        nav_checks = [
            ("GPS Constellation Link", f"CONNECTED ({self.sat_count} Sats)"),
            ("Satellite Imagery Sync", "LOADING HIGH-RES MAPS"),
            ("Geofence Perimeter", "ARMED"),
            ("Deepak-Prime Tracking-Auth", "AUTHORIZED")
        ]
        
        for task, status in nav_checks:
            print(f" \033[1;33m[NAV-SYNC]\033[0m {task:28} | [\033[1;32m{status}\033[0m]")
            time.sleep(0.7)

        print(f"\n\033[1;32m[SYSTEM] Navigation Online. Current Location Locked.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, the world is now a digital \nchessboard. I have established a stable link with \nthe global satellite constellation. Whether you are \nnavigating through Kota or exploring new territories, \nI will be your eye in the sky. I am tracking every \ncoordinate, every movement. You will never be lost, \nsir.\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    nav = JarvisNavigator()
    nav.activate_global_tracking()
