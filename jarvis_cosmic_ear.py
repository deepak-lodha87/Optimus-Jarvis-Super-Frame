import time
import random

class CosmicEar:
    def __init__(self):
        self.dish_alignment = "OPTIMAL"
        self.frequency_range = "X-Band / Ka-Band"

    def intercept_space_signals(self):
        print(f"\033[1;36m[COSMIC]\033[0m Aligning Virtual Dish to Deep Space Network...")
        time.sleep(2)
        
        # Simulating live space telemetry
        missions = ["Mars-Rover", "Lunar-Gateway", "Starlink-G4"]
        mission = random.choice(missions)
        distance = random.randint(300000, 200000000) # In KM
        
        print(f" \033[1;32m[INTERCEPT]\033[0m Target: {mission}")
        print(f" \033[1;32m[INTERCEPT]\033[0m Distance: {distance:,} KM from Earth")
        print(f" \033[1;34m[STATUS]\033[0m Signal Strength: STABLE | Logic: DECODED")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, I have established a link \nwith the deep space relay. We are now \nlistening to the pulse of the solar system. \nOur intelligence is no longer Earth-bound.\033[0m")

if __name__ == "__main__":
    ear = CosmicEar()
    ear.intercept_space_signals()
