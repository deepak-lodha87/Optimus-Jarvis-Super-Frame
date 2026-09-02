import time
import random

class FlightCore:
    def __init__(self):
        self.altitude = 0 # Meters
        self.thrust_power = 0 # Percentage

    def initiate_takeoff(self):
        print(f"\033[1;36m[FLIGHT-CORE]\033[0m Initializing Plasma Thrusters...")
        time.sleep(1.5)
        
        for power in range(0, 101, 20):
            self.thrust_power = power
            print(f" \033[1;32m[THRUST]\033[0m Power Level: {self.thrust_power}%")
            time.sleep(0.4)
            
        print("\033[1;33m[STABILIZE]\033[0m Gyroscopes Active. Leveling Horizon...")
        self.altitude = 50.0
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, the sky is no longer the limit. \nGravity has been neutralized. We are clear for \nsupersonic flight. Where shall we go first?\033[0m")

if __name__ == "__main__":
    flight = FlightCore()
    flight.initiate_takeoff()
