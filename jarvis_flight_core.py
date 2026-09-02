import time
import random

class FlightDynamics:
    def __init__(self):
        self.altitude = 0 # Meters
        self.thrust_level = 0 # Percentage
        self.is_hovering = False

    def initiate_takeoff(self):
        print(f"\033[1;36m[FLIGHT]\033[0m Calibrating Gravity-Nullification Coils...")
        time.sleep(1.5)
        
        self.thrust_level = 100
        print(f" \033[1;32m[IGNITION]\033[0m Ionic Thrust: {self.thrust_level}% | Stability: LOCKED")
        
        while self.altitude < 500:
            self.altitude += 100
            print(f"  - Climbing: {self.altitude}m | Wind Resistance: NEGLECTED")
            time.sleep(0.5)
            
        self.is_hovering = True
        print("\033[1;34m[STATUS]\033[0m Cruise Altitude Reached. Hover Mode: ACTIVE.")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, the sky is no longer a limit; \nit is our playground. Gravity has been \nneutralized. We are airborne and ready for \nsupersonic acceleration.\033[0m")

if __name__ == "__main__":
    pilot = FlightDynamics()
    pilot.initiate_takeoff()
