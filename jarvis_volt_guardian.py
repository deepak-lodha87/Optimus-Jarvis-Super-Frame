import os
import subprocess

class VoltGuardian:
    def __init__(self):
        self.master = "Deepak"
        self.threshold = 20

    def analyze_power_grid(self):
        print(f"\n\033[1;33m[VOLT GUARDIAN ACTIVE]\033[0m Scanning energy levels...")
        
        try:
            # Termux-API के माध्यम से बैटरी स्टेटस प्राप्त करना
            # सुनिश्चित करें कि termux-api इंस्टॉल है
            battery_data = os.popen('termux-battery-status').read()
            
            # डमी डेटा अगर एपीआई रिस्पॉन्स न दे (विकास के लिए)
            # असली डेटा के लिए: battery_level = int(json.loads(battery_data)['percentage'])
            battery_level = 18 
            
            if battery_level <= self.threshold:
                print(f"\033[1;31m[CRITICAL]: Power at {battery_level}%.\033[0m")
                os.system('termux-tts-speak "Deepak sir, energy levels are critical. Initiating self-preservation protocol."')
                print("\033[1;36m[ACTION]:\033[0m Disabling heavy modules and dimming display.")
            else:
                print(f"\033[1;32m[STABLE]:\033[0m Energy at {battery_level}%. Systems nominal.")
                
        except Exception as e:
            print(f"\033[1;31m[SENSOR ERROR]:\033[0m Unable to read battery vitals: {e}")

if __name__ == "__main__":
    guardian = VoltGuardian()
    guardian.analyze_power_grid()
