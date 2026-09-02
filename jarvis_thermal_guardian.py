import os
import json
import subprocess

class ThermalGuardian:
    def __init__(self):
        self.master = "Deepak"
        self.critical_temp = 45.0  # 45 डिग्री सेल्सियस से ऊपर चेतावनी

    def check_thermals(self):
        print(f"\n\033[1;31m[THERMAL GUARDIAN ACTIVE]\033[0m Checking hardware vitals...")
        
        try:
            # Termux API से बैटरी डेटा लेना
            result = subprocess.run(['termux-battery-status'], capture_output=True, text=True)
            data = json.loads(result.stdout)
            
            temp = data.get("temperature", 0)
            health = data.get("health", "UNKNOWN")
            
            print(f"\033[1;36m[TEMPERATURE]:\033[0m {temp}°C")
            print(f"\033[1;36m[HEALTH]:\033[0m {health}")
            
            if temp > self.critical_temp:
                msg = f"Deepak sir, hardware alert! Battery temperature is high at {temp} degrees. Please cool down the device."
                color = "\033[1;31m"
            else:
                msg = f"Deepak sir, thermal levels are stable at {temp} degrees. Battery health is {health}."
                color = "\033[1;32m"
                
            print(f"{color}[REPORT]: {msg}\033[0m")
            os.system(f'termux-tts-speak "{msg}"')
            
        except Exception as e:
            print(f"Error accessing sensors: {e}")

if __name__ == "__main__":
    guardian = ThermalGuardian()
    guardian.check_thermals()
