import os
import requests
import json

class LocationCore:
    def __init__(self):
        self.master = "Deepak"

    def get_geo_status(self):
        print(f"\n\033[1;36m[SATELLITE UPLINK]\033[0m Pinging local towers...")
        
        try:
            # IP आधारित लोकेशन प्राप्त करना
            geo = requests.get('https://ipapi.co/json/').json()
            city = geo.get('city', 'Ratlam')
            region = geo.get('region', 'Madhya Pradesh')
            
            # मौसम का हाल (Open-Meteo का उपयोग - बिना API key के)
            lat, lon = geo.get('latitude'), geo.get('longitude')
            weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
            weather_data = requests.get(weather_url).json()
            temp = weather_data['current_weather']['temperature']

            msg = f"Deepak sir, we are currently in {city}, {region}. The external temperature is {temp} degrees Celsius."
            
            print(f"\n\033[1;32m[LOCATION]:\033[0m {city}, {region}")
            print(f"\033[1;32m[WEATHER]:\033[0m {temp}°C")
            
            os.system(f'termux-tts-speak "{msg}"')
            
        except Exception as e:
            print(f"\033[1;31m[OFFLINE]\033[0m Could not reach GPS satellites.")
            os.system('termux-tts-speak "Sir, location services are currently unavailable."')

if __name__ == "__main__":
    loc = LocationCore()
    loc.get_geo_status()
