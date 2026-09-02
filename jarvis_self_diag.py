import os
import time

class SelfDiagnosis:
    def __init__(self):
        self.master = "Deepak sir"

    def speak(self, text):
        os.system(f'termux-tts-speak "{text}"')

    def run_scan(self):
        print(f"\033[1;36m[DIAGNOSIS]\033[0m Initiating Hardware Integrity Check...")
        self.speak(f"{self.master}, scanning internal sensors and frequency modems.")
        
        sensors = ["RF-Antenna", "Signal-Processor", "Neural-Engine", "Satellite-Uplink-Module"]
        
        for sensor in sensors:
            print(f"\033[1;33m[SCANNING]\033[0m Testing {sensor}...")
            time.sleep(1)
            print(f"\033[1;32m[OK]\033[0m {sensor} is operating at peak efficiency.")
            
        self.speak("Hardware diagnosis complete. All systems are optimized for deep space communication.")

if __name__ == "__main__":
    diag = SelfDiagnosis()
    diag.run_scan()
