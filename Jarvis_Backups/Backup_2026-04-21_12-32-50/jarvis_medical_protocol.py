import time

class MedicalProtocol:
    def __init__(self):
        self.user = "Deepak"
        self.phase = "3045"
        self.emergency_contact = "Emergency Services / Trusted Contact"

    def analyze_trauma_levels(self):
        print(f"\033[1;35m>> PHASE {self.phase}: MONITORING TRAUMA & STRESS LEVELS <<\033[0m")
        time.sleep(1)
        # Simulation of emergency logic
        stress_level = 45 # Normal range 0-100
        print(f"\033[1;34m[BIO-DATA] Current Stress Level: {stress_level}%\033[0m")
        
        if stress_level > 85:
            self.trigger_emergency()
        else:
            print("\033[1;32m[STATUS] Biological state stable. No emergency protocol required.\033[0m")

    def trigger_emergency(self):
        print("\033[1;31m[ALERT] EXTREME BIOLOGICAL DISTRESS DETECTED! <<\033[0m")
        print(f"\033[1;33m[ACTION] Sending location to {self.emergency_contact}...\033[0m")
        print("\033[1;33m[ACTION] Activating First-Aid HUD Instructions for nearby personnel.\033[0m")

    def run(self):
        print(f"\033[1;32m>> MEDICAL PROTOCOL STANDBY: ARCHITECT DEEPAK IS UNDER WATCH. <<\033[0m")
        self.analyze_trauma_levels()

if __name__ == "__main__":
    emp = MedicalProtocol()
    emp.run()
