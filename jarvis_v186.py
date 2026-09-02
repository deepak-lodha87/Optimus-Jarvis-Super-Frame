import os
import time
import subprocess
import json

def get_location_weather():
    print("\n[SYSTEM]: Scanning local environment data...")
    time.sleep(1)
    try:
        # Termux API के जरिए लोकेशन डेटा (सिम्युलेटेड या API आधारित)
        loc_msg = "Commander Deepak, current sector: Kota, Rajasthan. Environment is stable."
        print(f"[JARVIS]: {loc_msg}")
        os.system(f"termux-tts-speak '{loc_msg}'")
        
        # Weather simulation
        weather_msg = "The external temperature is approximately 32 degrees Celsius. Clear skies."
        print(f"[JARVIS]: {weather_msg}")
        os.system(f"termux-tts-speak '{weather_msg}'")
        
    except Exception as e:
        print(f"[ERROR]: Could not retrieve environment data.")

def jarvis_main():
    print("\n" + "="*50)
    print("|    JARVIS PHASE 186: ENVIRONMENT INTEL    |")
    print("="*50)
    get_location_weather()
    print("\n[SYSTEM]: Optimus Jarvis Super-Frame is standing by.")
    print("="*50)

if __name__ == "__main__":
    jarvis_main()
