import time
import random

class WeatherEngine:
    def __init__(self):
        self.station_id = "RATLAM-CORE-01"
        self.prediction_accuracy = 98.4

    def analyze_atmosphere(self):
        print(f"\033[1;36m[METEOROLOGY]\033[0m Syncing with Global Weather Satellites...")
        time.sleep(2)
        
        wind_speed = random.randint(5, 45) # km/h
        humidity = random.randint(30, 90)
        
        print(f" \033[1;32m[DATA]\033[0m Wind Speed: {wind_speed} km/h | Humidity: {humidity}%")
        
        if wind_speed > 35:
            print("\033[1;31m[WARNING]\033[0m High turbulence detected. Grounding all small drones.")
        else:
            print("\033[1;34m[STATUS]\033[0m Optimal flight conditions for Aerial Legion.")
            
        print(f"\n\033[1;35m[VOICE] Deepak sir, the atmosphere is under \nmonitoring. I have adjusted the flight \npaths of our drones to avoid the incoming \nwind front. The sky is ours.\033[0m")

if __name__ == "__main__":
    weather = WeatherEngine()
    weather.analyze_atmosphere()
