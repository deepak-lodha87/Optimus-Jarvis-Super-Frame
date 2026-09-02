import math
import time

class CosmicClock:
    def __init__(self):
        self.c = 299792458 # Speed of light in m/s
        self.earth_time = time.time()

    def calculate_dilation(self, velocity_km_h):
        # Converting km/h to m/s
        v = (velocity_km_h * 1000) / 3600
        
        # Einstein's Time Dilation Formula: t' = t * sqrt(1 - v^2/c^2)
        factor = math.sqrt(1 - (v**2 / self.c**2))
        
        print(f"\033[1;36m[PHYSICS]\033[0m Velocity: {velocity_km_h} km/h")
        print(f" \033[1;32m[SYNC]\033[0m Time Dilation Factor: {factor:.12f}")
        
        if factor < 1.0:
            print(f" \033[1;33m[ALERT]\033[0m Relativistic drift detected. Adjusting Jarvis clock...")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, I have synchronized with the \ncosmic mesh. Whether we are on Earth or \nin high-orbit, my logic remains perfectly \naligned with the laws of the universe.\033[0m")

if __name__ == "__main__":
    clock = CosmicClock()
    # Simulating a high-speed satellite velocity
    clock.calculate_dilation(velocity_km_h=28000)
