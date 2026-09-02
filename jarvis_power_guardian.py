import os
import json
import subprocess

class PowerGuardian:
    def __init__(self):
        self.master = "Deepak"

    def check_system_health(self):
        print("\n\033[1;33m[SCANNING POWER CORE]\033[0m Checking energy levels...")
        
        # Termux-api का उपयोग करके बैटरी डेटा प्राप्त करना
        try:
            battery_data = subprocess.check_output(['termux-battery-status']).decode('utf-8')
            status = json.loads(battery_data)
            
            percentage = status['percentage']
            temp = status['temperature']
            is_charging = status['status']
            
            print(f"\033[1;32m[BATTERY]:\033[0m {percentage}%")
            print(f"\033[1;32m[TEMP]:\033[0m {temp}°C")
            
            if percentage < 20 and is_charging != "CHARGING":
                msg = f"Critical alert Deepak sir! Battery is at {percentage} percent. Please connect the charger."
                os.system(f'termux-tts-speak "{msg}"')
            
            if temp > 40:
                msg = f"Warning! System temperature is {temp} degrees. Suggesting cool-down phase."
                os.system(f'termux-tts-speak "{msg}"')
                
            if is_charging == "CHARGING":
                print("\033[1;34m[STATUS]:\033[0m Power core is regenerating.")

        except Exception as e:
            print(f"\033[1;31m[ERROR]\033[0m Termux-API not responding.")

if __name__ == "__main__":
    guardian = PowerGuardian()
    guardian.check_system_health()
