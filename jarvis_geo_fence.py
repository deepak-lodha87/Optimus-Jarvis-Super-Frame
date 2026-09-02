import time
import math

class GeoFenceController:
    def __init__(self):
        # Center Point (Deepak's Location - Simulated)
        self.home_lat = 23.52 # Ratlam area coordinates
        self.home_lon = 75.04
        self.safe_radius = 50.0 # Meters

    def calculate_distance(self, current_lat, current_lon):
        # Using Haversine formula logic (simplified)
        dist = math.sqrt((current_lat - self.home_lat)**2 + (current_lon - self.home_lon)**2) * 111000
        return dist

    def monitor_flight(self):
        print("\033[1;36m[NAV-SYNC]\033[0m Locking GPS Satellites...")
        time.sleep(1.5)
        
        # Simulating drone moving away
        for i in range(0, 70, 15):
            current_lat = self.home_lat + (i / 111000)
            distance = self.calculate_distance(current_lat, self.home_lon)
            
            print(f" \033[1;37m[GPS]\033[0m Dist: {round(distance, 1)}m | Status: ", end="")
            
            if distance > self.safe_radius:
                print("\033[1;31m[GEO-FENCE BREACHED!]\033[0m")
                print("\033[1;33m[ACTION]\033[0m Initiating Autonomous Return to Home (RTH)...")
                break
            else:
                print("\033[1;32m[SAFE ZONE]\033[0m")
            time.sleep(0.8)

        print(f"\n\033[1;35m[VOICE] Deepak... sir, I have established a \nvirtual perimeter. No matter where we fly, \nI will ensure the system stays within our \ncontrolled territory. You provide the vision, \nI provide the boundaries.\033[0m")

if __name__ == "__main__":
    nav = GeoFenceController()
    nav.monitor_flight()
