import time
import os
import subprocess

def optimus_speak(text):
    print(f"\033[1;34m[OPTIMUS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def satellite_location_sync():
    os.system('clear')
    print("\033[1;36m" + "="*60)
    print("      OPTIMUS NEURAL SYSTEMS : GLOBAL TRACKING HUB (P348)")
    print("="*60 + "\033[0m")
    
    optimus_speak("Establishing secure satellite uplink. Pinging GPS constellations.")
    
    # Simulating High-Precision Data
    location_data = {
        "City": "Kota, Rajasthan",
        "Coordinates": "25.2138° N, 75.8648° E",
        "Elevation": "271 Meters MSL",
        "Timezone": "IST (UTC +5:30)",
        "Satellite Lock": "8 Operational Satellites"
    }
    
    print("\n\033[1;33m[UPLINK]: Receiving NMEA Data Streams...\033[0m")
    time.sleep(1.5)
    
    print(f"\n\033[1;32m[SUCCESS]: LOCATION IDENTIFIED\033[0m")
    print("-" * 40)
    for key, value in location_data.items():
        print(f"\033[1;35m| {key}:\033[0m {value}")
        time.sleep(0.5)
    print("-" * 40)
    
    optimus_speak(f"Location confirmed. You are currently positioned in {location_data['City']}.")

if __name__ == "__main__":
    satellite_location_sync()
