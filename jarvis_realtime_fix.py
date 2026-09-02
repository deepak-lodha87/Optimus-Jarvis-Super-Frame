import os
import time

class RealTimeMechanic:
    def __init__(self):
        self.master = "Deepak"

    def analyze_fault_nature(self, fault_type):
        print(f"\n\033[1;36m[JARVIS DIAGNOSIS]\033[0m Analyzing fault: {fault_type}")
        time.sleep(1)
        
        if fault_type == "Electrical":
            print("\033[1;32m[ACTION]\033[0m Executing Digital Bypass...")
            time.sleep(1.5)
            print("\033[1;32m[SUCCESS]\033[0m System Rebooted. Engine Authorized to Start.")
        else:
            print("\033[1;33m[ALERT]\033[0m Mechanical Failure Detected. Activating 'Limp Mode'...")
            time.sleep(1)
            print("\033[1;34m[INFO]\033[0m Sending GPS & Fault Report to nearest Service Hub.")

    def final_instruction(self):
        msg = "Deepak sir, for electrical issues, I have full control. For mechanical, I am managing the logistics to get you to safety."
        os.system(f'termux-tts-speak "{msg}"')

if __name__ == "__main__":
    jarvis = RealTimeMechanic()
    # उदाहरण के तौर पर इलेक्ट्रिकल इशू चेक करना
    jarvis.analyze_fault_nature("Electrical")
    jarvis.final_instruction()
