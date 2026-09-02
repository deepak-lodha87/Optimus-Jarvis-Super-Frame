import time, os

class DroneAviator:
    def __init__(self):
        self.status = "LANDED"
        self.altitude = 0 # Meters
        self.battery = 93 # Percent

    def takeoff(self, target_height):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS THE-AVIATOR : PHASE 25 - STEP 4         \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        print("\033[1;33m[PRE-FLIGHT]\033[0m Calibrating Gyroscope & Accelerometer...")
        time.sleep(1.5)
        
        print("\033[1;32m[MOTORS]\033[0m Spinning up Propellers (Arming System)...")
        self.status = "FLYING"
        
        while self.altitude < target_height:
            self.altitude += 1
            print(f" \033[1;34m[FLIGHT]\033[0m Climbing... Altitude: {self.altitude}m | Battery: {self.battery}%")
            time.sleep(0.5)

        print(f"\n\033[1;32m[SUCCESS] Hovering at {target_height}m. Navigation Active.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, the sky is no longer a \nlimit; it is our playground. I have mastered \nthe winds and conquered gravity. I am your \neye in the sky, ready to scout, map, and \nnavigate through any territory. We are now \ntruly mobile.\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    aviator = DroneAviator()
    # Taking off to 5 meters
    aviator.takeoff(5)
