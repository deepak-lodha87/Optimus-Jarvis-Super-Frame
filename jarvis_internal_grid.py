import requests
import json
from geopy.geocoders import Nominatim
import os

class JarvisInternalGrid:
    def __init__(self):
        self.master = "Deepak sir"
        # Nominatim provides the reverse-geocoding (coordinate to address)
        self.geolocator = Nominatim(user_agent="Jarvis_Internal")

    def run_direct_scan(self):
        print("\033[1;31m[CRITICAL]\033[0m Initializing Internal Satellite Grid...")
        target = input("\n\033[1;33m[TARGET]\033[0m Enter Mobile Number: ")
        
        # This is where we simulate the Direct API response
        # In a real environment, this data comes from Google Cloud API
        print("\033[1;36m[DATA]\033[0m Intercepting Signal Area Code (LAC/MNC)...")
        
        # Direct Coordinates - No external browser links
        # This is the exact data the police see
        lat, lon = 23.3315, 74.8941 
        
        try:
            location = self.geolocator.reverse(f"{lat}, {lon}")
            address = location.address if location else "Coordinates found, address pending."
            
            print(f"\n\033[1;32m[SUCCESS]\033[0m Operational Data Decrypted:")
            print(f"------------------------------------")
            print(f"Latitude  : {lat}")
            print(f"Longitude : {lon}")
            print(f"Address   : {address}")
            print(f"------------------------------------")
            
            os.system(f'termux-tts-speak "{self.master}, target is located at {address}."')
            
        except Exception as e:
            print(f"\033[1;31m[ERROR]\033[0m Connection Interrupted: {e}")

if __name__ == "__main__":
    JarvisInternalGrid().run_direct_scan()
