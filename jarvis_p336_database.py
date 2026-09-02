import json
import time
import subprocess

def jarvis_speak(text):
    print(f"\033[1;34m[JARVIS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

# Advanced Asset Database
asset_registry = {
    "hunter 350": {
        "category": "Motorcycle",
        "engine_type": "J-Series 349cc",
        "fuel_system": "Fuel Injection",
        "compression_ratio": "9.5:1",
        "tire_pressure": "Front: 29 psi, Rear: 32 psi",
        "blueprint_status": "Verified"
    },
    "uav drone": {
        "category": "Aerial Vehicle",
        "flight_controller": "Pixhawk 4 / ArduPilot",
        "motor_type": "920KV Brushless",
        "propeller": "10x4.5 inch",
        "payload_capacity": "1.5 kg",
        "frequency": "2.4 GHz"
    },
    "power_train": {
        "category": "Electrical",
        "voltage": "48V - 72V",
        "motor": "BLDC Hub Motor",
        "cooling": "Air Cooled",
        "efficiency": "92%"
    }
}

def search_asset():
    os.system('clear')
    print("\033[1;36m" + "="*50)
    print("      OPTIMUS JARVIS : ASSET REGISTRY (P336)")
    print("="*50 + "\033[0m")
    
    jarvis_speak("Asset registry is online. Which blueprint should I load?")
    query = input("\033[1;33m[INPUT]: Enter Asset Name: \033[0m").lower()

    if query in asset_registry:
        data = asset_registry[query]
        jarvis_speak(f"Loading specifications for {query}.")
        print(f"\n\033[1;32m[MATCH FOUND]: {query.upper()}\033[0m")
        print("-" * 30)
        for key, value in data.items():
            print(f"| {key.replace('_', ' ').title()}: {value}")
            time.sleep(0.3) # Scanning effect
        print("-" * 30)
    else:
        jarvis_speak("Specified asset not found in the current database.")
        print("\033[1;31m[ERROR]: Asset not indexed.\033[0m")

if __name__ == "__main__":
    import os
    search_asset()
