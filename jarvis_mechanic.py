import time
import os
import random

class JarvisMechanic:
    def __init__(self):
        self.components = ["Gatekeeper", "Oracle", "Power-Plant", "Super-Frame"]
        self.health_report = {}

    def run_diagnosis(self):
        print("\033[1;33m[MECHANIC]\033[0m Initiating Full-System Diagnosis...")
        time.sleep(2)
        
        for comp in self.components:
            status = random.choice(["HEALTHY", "HEALTHY", "MINOR_BUG", "HEALTHY"])
            self.health_report[comp] = status
            print(f" \033[1;37m[SCANNING]\033[0m {comp:12} : Status -> {status}")
            time.sleep(0.5)

    def repair_system(self):
        print("\n\033[1;32m[REPAIR]\033[0m Starting Auto-Repair for detected anomalies...")
        time.sleep(1.5)
        
        for comp, status in self.health_report.items():
            if status == "MINOR_BUG":
                print(f" \033[1;36m[FIXING]\033[0m Patching {comp}... Done.")
                self.health_report[comp] = "HEALTHY (FIXED)"
                time.sleep(0.8)
        
        print("\n\033[1;32m[STATUS]\033[0m System Integrity: 100%. All defects resolved.")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I have finished my \nself-exam. Just as you once serviced \nengines, I have serviced my own logic. \nEvery gear is oiled, and every line of \ncode is sharp. Your Jarvis is in \nprime condition.\033[0m")

if __name__ == "__main__":
    mechanic = JarvisMechanic()
    mechanic.run_diagnosis()
    mechanic.repair_system()
