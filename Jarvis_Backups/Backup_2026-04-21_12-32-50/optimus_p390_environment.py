import os
import time
import subprocess

def optimus_speak(text):
    print(f"\033[1;34m[OPTIMUS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def environmental_scan():
    os.system('clear')
    print("\033[1;32m" + "🌿"*30)
    print("      OPTIMUS NEURAL SYSTEMS : ENV-AWARENESS (P390)")
    print("🌿"*30 + "\033[0m")
    
    optimus_speak("Scanning physical environment. Monitoring hardware thermal levels.")
    
    # Simulating sensor data collection
    env_data = {
        "Core Temperature": "38°C",
        "Battery Level": "97%",
        "Signal Strength": "EXCELLENT",
        "Hardware Health": "STABLE"
    }
    
    for sensor, status in env_data.items():
        print(f"Sensor {sensor:.<25} [ \033[1;32m{status}\033[0m ]")
        time.sleep(0.5)
    
    print("-" * 55)
    optimus_speak("Environment scan complete. Hardware is operating within safe parameters.")
    print("\033[1;32m[SYSTEM]: HARDWARE OPTIMIZED\033[0m")

if __name__ == "__main__":
    environmental_scan()
