import time, secrets, math

class JarvisAerospace:
    def __init__(self):
        self.nav_id = f"NASp-{secrets.token_hex(2).upper()}"
        self.altitude = 0 # in meters

    def launch_sequence(self, target_alt):
        print(f"\n\033[1;37m--- NEURAL-AUTO-SPACE V1 ACTIVE (ID: {self.nav_id}) ---\033[0m")
        print(f"\033[1;36m[LAUNCH] Initiating ascent to {target_alt}m...\033[0m")
        time.sleep(2)
        
        while self.altitude < target_alt:
            self.altitude += target_alt // 5
            temp = 15 - (0.0065 * self.altitude) # Standard Lapse Rate
            print(f"\033[1;32m[ALTITUDE] {self.altitude}m | Outside Temp: {temp:.2f}°C\033[0m")
            time.sleep(0.5)
            
        print("\033[1;33m[SYNC] Satellite uplink established. Global coverage: 100%\033[0m")
        print(f"\033[1;35m[VOICE] Deepak, the Super-Frame is now monitoring the orbital layer. We have the high ground.\033[0m")

if __name__ == "__main__":
    pilot = JarvisAerospace()
    pilot.launch_sequence(10000) # Testing 10km altitude
