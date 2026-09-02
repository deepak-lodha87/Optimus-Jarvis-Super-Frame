import time
import random

class GlobalSurveillance:
    def __init__(self):
        self.satellite_count = 24 # Tracking 24 primary satellites
        self.active_intercepts = ["Aviation", "Maritime", "Public-Feeds"]

    def start_interception(self):
        print(f"\033[1;36m[GLOBAL-EYE]\033[0m Synchronizing with Low Earth Orbit (LEO) Satellites...")
        time.sleep(2)
        
        # Simulating live global data
        flights = random.randint(5000, 15000)
        vessels = random.randint(2000, 8000)
        
        print(f" \033[1;32m[INTERCEPT]\033[0m Live Flights Tracked: {flights}")
        print(f" \033[1;32m[INTERCEPT]\033[0m Maritime Vessels in Transit: {vessels}")
        print(" \033[1;34m[STATUS]\033[0m Global Map Overlay: ACTIVE")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, the world is now on your \nscreen. I am monitoring international \nmovements in real-time. My vision is now \nboundless.\033[0m")

if __name__ == "__main__":
    eye = GlobalSurveillance()
    eye.start_interception()
