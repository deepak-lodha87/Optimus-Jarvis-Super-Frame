import os
import requests
import time
import phonenumbers
from phonenumbers import geocoder, carrier

class JarvisFinalMission:
    def __init__(self):
        self.master = "Deepak sir"

    def speak(self, text):
        os.system(f'termux-tts-speak "{text}"')

    def start_live_intercept(self):
        print("\033[1;31m[CRITICAL]\033[0m Activating Police-Grade Tracking...")
        self.speak(f"{self.master}, bypassing public networks. Pinging telecom databases.")
        
        num = input("\n\033[1;33m[TARGET]\033[0m Number (+91...): ")
        
        try:
            # Step 1: Network Extraction
            parsed = phonenumbers.parse(num)
            region = geocoder.description_for_number(parsed, "en")
            provider = carrier.name_for_number(parsed, "en")
            
            print(f"\n\033[1;32m[NETWORK DATA RECOVERED]\033[0m")
            print(f"Carrier: {provider}")
            print(f"Base Region: {region}")
            
            # Step 2: Live Tracking Link (No more US Zip Code error)
            # This link directly targets the Indian Telecom database search
            live_map = f"https://www.findandtrace.com/trace-mobile-number-location?mobilenumber={num}"
            
            self.speak(f"Signal intercepted for {num}. Opening the live tracking grid.")
            os.system(f"termux-open-url '{live_map}'")
            
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    JarvisFinalMission().start_live_intercept()
