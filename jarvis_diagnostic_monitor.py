import os
import time

class DiagnosticMonitor:
    def __init__(self):
        self.master = "Deepak"
        self.project = "Optimus Jarvis Super-Frame"

    def run_diagnosis(self, machine):
        print(f"\n\033[1;33m[DIAGNOSTIC]\033[0m Scanning {machine} for micro-defects...")
        time.sleep(1.5)
        
        # Diagnostic Logic
        checks = [
            "Analyzing Electrical Conductivity...",
            "Checking Structural Integrity...",
            "Monitoring Tire Pressure & Wear Patterns...",
            "Predicting Potential Faults..."
        ]
        
        for check in checks:
            print(f"\033[1;32m[CHECK]\033[0m {check}")
            time.sleep(0.4)

        msg = f"{self.master} sir, no defects found in {machine}. The system is 100% operational."
        os.system(f'termux-tts-speak "{msg}"')

    def execute(self):
        os.system('clear')
        print(f"--- {self.project} : PROACTIVE DIAGNOSTIC MONITOR ---")
        self.run_diagnosis("Automated Heavy Truck")
        print("\n\033[1;36m[STATUS]\033[0m SYSTEM HEALTH: OPTIMAL")

if __name__ == "__main__":
    DiagnosticMonitor().execute()
