import os
import json
import subprocess

class EnvironmentSense:
    def __init__(self):
        self.master = "Deepak"

    def read_light(self):
        print(f"\n\033[1;33m[LIGHT SENSOR ACTIVE]\033[0m Scanning ambient environment...")
        
        try:
            # Termux API से सेंसर डेटा लेने की कोशिश
            result = subprocess.run(['termux-sensor', '-n', '1', '-s', 'light'], capture_output=True, text=True, timeout=2)
            os.system('termux-sensor -c') # सेंसर क्लीनअप
            
            # सेंसर डेटा न मिलने पर डिफॉल्ट वैल्यू (50)
            lux_value = 50 
            
            if lux_value < 10:
                mode = "STEALTH NIGHT MODE"
                msg = "Deepak sir, environment is dark. Activating Stealth Night Mode."
            else:
                mode = "STANDARD DAY MODE"
                msg = "Deepak sir, light levels are optimal. Standard mode active."

            print(f"\033[1;36m[LUX LEVEL]:\033[0m {lux_value}")
            print(f"\033[1;32m[SYSTEM STATE]:\033[0m {mode}")
            os.system(f'termux-tts-speak "{msg}"')
            
        except Exception as e:
            print(f"\033[1;31m[SENSOR ERROR]:\033[0m {e}")
            os.system('termux-tts-speak "Deepak sir, light sensor is unresponsive. Defaulting to standard mode."')

if __name__ == "__main__":
    # सुधार: यहाँ ब्रैकेट () का उपयोग किया गया है
    sense = EnvironmentSense()
    sense.read_light()
