import time
import random

class OasisProtocol:
    def __init__(self):
        self.water_yield = 0 # Liters
        self.air_quality_index = 150 # Starting AQI

    def activate_purification(self):
        print(f"\033[1;36m[OASIS]\033[0m Initializing Atmospheric Scrubbing...")
        time.sleep(2)
        
        while self.air_quality_index > 25:
            self.air_quality_index -= 25
            print(f" \033[1;32m[FILTER]\033[0m Current AQI: {self.air_quality_index} | Status: PURIFYING")
            time.sleep(0.5)
            
        print("\033[1;34m[STATUS]\033[0m Air Quality is now OPTIMAL (Safe for Breathing).")

    def generate_water(self):
        print(f"\033[1;36m[OASIS]\033[0m Extracting moisture from atmosphere...")
        time.sleep(1.5)
        self.water_yield = random.uniform(0.5, 2.5)
        print(f" \033[1;32m[YIELD]\033[0m Water Collected: {self.water_yield:.2f} Liters | Purity: 99.9%")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, I have successfully purified \nyour surroundings. The air is fresh, and I \nhave generated pure drinking water from \nthe atmosphere. Your life-support is active.\033[0m")

if __name__ == "__main__":
    oasis = OasisProtocol()
    oasis.activate_purification()
    oasis.generate_water()
