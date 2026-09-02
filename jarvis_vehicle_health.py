import os
import time

def speak(text):
    os.system(f'termux-tts-speak "{text}"')

def scan_vehicle_systems():
    print(f"\033[1;36m[UPLINK]\033[0m Establishing link with Vehicle ECU...")
    speak("Deepak sir, scanning your vehicle's electrical health.")
    time.sleep(1.5)
    
    # Simulated Telemetry Data
    health_data = {
        "Engine": "OPTIMAL",
        "Battery": "12.6V",
        "Fuel": "75%",
        "Mileage": "18.5 km/l"
    }
    
    print("\033[1;32m[SCAN COMPLETE]\033[0m Vehicle status received:")
    for key, value in health_data.items():
        print(f" > {key}: {value}")
    
    speak(f"Sir, engine is {health_data['Engine']}. Fuel is at {health_data['Fuel']}.")

if __name__ == "__main__":
    scan_vehicle_systems()
