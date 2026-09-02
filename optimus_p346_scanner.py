import time
import os
import subprocess

def optimus_speak(text):
    print(f"\033[1;34m[OPTIMUS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def neural_scanner():
    os.system('clear')
    print("\033[1;36m" + "="*60)
    print("      OPTIMUS NEURAL SYSTEMS : ADVANCED BLUEPRINT SCANNER")
    print("="*60 + "\033[0m")
    
    optimus_speak("Neural scanner is active. Awaiting hardware identification.")
    
    asset = input("\n\033[1;33m[INPUT]: Enter Asset Name (e.g. Hunter 350, UAV Drone): \033[0m").lower()
    
    print(f"\n\033[1;32m[SYSTEM]: Scanning {asset.upper()} Database...\033[0m")
    time.sleep(1)
    
    # Advanced Data Dictionary
    blueprints = {
        "hunter 350": {
            "Engine": "Single cylinder, 4-stroke, Air-oil cooled",
            "Torque": "27 Nm @ 4000 rpm",
            "Chassis": "Twin Downtube Spine Frame",
            "Compression": "9.5:1",
            "Safety": "Dual Channel ABS Activated"
        },
        "uav drone": {
            "Core": "32-bit ARM Cortex-M4",
            "Propulsion": "850KV Brushless Motors",
            "Telemetry": "Long Range LoRa Link",
            "Voltage": "14.8V Nominal",
            "Guidance": "Optical Flow & LiDAR"
        }
    }

    if asset in blueprints:
        optimus_speak(f"Blueprint for {asset} successfully retrieved.")
        print("-" * 40)
        for key, value in blueprints[asset].items():
            print(f"\033[1;35m| {key}:\033[0m {value}")
            time.sleep(0.4)
        print("-" * 40)
    else:
        optimus_speak("Asset not found in Optimus Neural database.")
        print("\033[1;31m[ERROR]: Data mismatch.\033[0m")

if __name__ == "__main__":
    neural_scanner()
