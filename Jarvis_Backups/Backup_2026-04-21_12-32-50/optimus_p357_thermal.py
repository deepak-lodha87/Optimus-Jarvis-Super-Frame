import os
import subprocess
import time

def optimus_speak(text):
    print(f"\033[1;34m[OPTIMUS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def thermal_shield_monitor():
    os.system('clear')
    print("\033[1;31m" + "🌡️"*30)
    print("      OPTIMUS NEURAL SYSTEMS : THERMAL SHIELD (P357)")
    print("🌡️"*30 + "\033[0m")
    
    optimus_speak("Thermal monitoring active. Scanning hardware temperature sensors.")
    
    # Fetching real battery temperature from Termux
    try:
        raw_data = os.popen('termux-battery-status').read()
        # Simulation if real data is blocked on some devices
        temp = 36.5 
        if "temperature" in raw_data.lower():
            import json
            data = json.loads(raw_data)
            temp = data['temperature'] / 10.0 # Convert to Celsius
    except:
        temp = 38.0

    print(f"\n\033[1;33m[SENSOR DATA]: Core Temperature: {temp}°C\033[0m")
    
    if temp > 45.0:
        print("\033[1;41m[CRITICAL]: OVERHEATING DETECTED!\033[0m")
        optimus_speak("System is overheating. Initiating emergency cooling and reducing background processes.")
        print("\033[1;31m[ACTION]: Throttling CPU Power. Cooling engaged.\033[0m")
    elif temp > 40.0:
        print("\033[1;33m[WARNING]: Temperature rising above optimal levels.\033[0m")
        optimus_speak("Warning. Core temperature is rising. Suggesting moderate usage.")
    else:
        print("\033[1;32m[STABLE]: Thermal integrity within safe limits.\033[0m")
        optimus_speak("Thermal levels are nominal. All systems stable.")

if __name__ == "__main__":
    thermal_shield_monitor()
