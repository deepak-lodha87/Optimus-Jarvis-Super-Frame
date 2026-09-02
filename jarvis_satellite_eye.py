import time
import random

class SatelliteEye:
    def __init__(self):
        self.location = "Ratlam / Madhya Pradesh"
        self.satellite_link = "INSAT-3DR_ACTIVE"

    def scan_atmosphere(self):
        print(f"\033[1;36m[CONNECTING]\033[0m Establishing link with {self.satellite_link}...")
        time.sleep(2)
        
        # Simulating satellite data analysis
        temp = random.randint(35, 45)
        humidity = random.randint(20, 60)
        cloud_cover = random.choice(["Clear Sky", "Partly Cloudy", "Heavy Precipitation Imminent"])
        
        print(f" \033[1;32m[SCANNING]\033[0m Location: {self.location}")
        print(f" \033[1;34m[DATA]\033[0m Temperature: {temp}°C | Humidity: {humidity}%")
        print(f" \033[1;34m[DATA]\033[0m Atmospheric Condition: {cloud_cover}")
        
        if "Heavy" in cloud_cover:
            print("\n\033[1;31m[ALERT] Unstable weather detected. Recommend staying indoors.\033[0m")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, the eye in the sky is active. \nI am monitoring atmospheric shifts over your \ncurrent coordinates. No surprises from nature \nwill reach you unannounced.\033[0m")

if __name__ == "__main__":
    eye = SatelliteEye()
    eye.scan_atmosphere()
