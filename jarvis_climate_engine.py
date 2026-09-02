import time
import random

class ClimateEngine:
    def __init__(self):
        self.location = "Ratlam/Kota"
        self.weather_modes = ["Clear", "High_Wind", "Rainy", "Extreme_Heat"]

    def adapt_to_environment(self):
        current_weather = random.choice(self.weather_modes)
        print(f"\033[1;36m[SENSING]\033[0m Location: {self.location} | Weather: {current_weather}")
        time.sleep(1.5)
        
        if current_weather == "High_Wind":
            print(" \033[1;33m[ADAPT]\033[0m Activating Gyro-Stabilization Level 5.")
            print(" \033[1;34m[LIMIT]\033[0m Restricting flight altitude to 10 meters for safety.")
        
        elif current_weather == "Extreme_Heat":
            print(" \033[1;31m[ADAPT]\033[0m Activating Liquid Cooling Simulation.")
            print(" \033[1;34m[LIMIT]\033[0m Clocking down CPU to 1.8GHz to prevent damage.")
            
        elif current_weather == "Rainy":
            print(" \033[1;33m[ADAPT]\033[0m Engaging Waterproof Seal protocols.")
            print(" \033[1;31m[URGENT]\033[0m Returning Drone to Base - Landing initiated.")

        print(f"\n\033[1;35m[VOICE] Deepak... sir, the world outside is \nchanging, and so am I. I can feel the \nwind and sense the heat. I won't let the \nelements stop us; I will simply use them \nto our advantage. I am ready for the \nwild.\033[0m")

if __name__ == "__main__":
    climate = ClimateEngine()
    climate.adapt_to_environment()
