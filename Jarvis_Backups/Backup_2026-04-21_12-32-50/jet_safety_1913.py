import time
import random

class FighterSafetySystem:
    def __init__(self):
        # कोड के भीतर फेज नंबर सुरक्षित हैं
        self.phase_gforce = 1912
        self.phase_ejection = 1913
        print(f"--- Optimus Jarvis Super-Frame ---")
        print(f"Initializing Pilot Safety: {self.phase_gforce} & {self.phase_ejection}")

    # Phase 1912: G-Force Compensation (गुरुत्वाकर्षण बल संतुलन)
    def compensate_gforce(self, current_g):
        print(f"\n[Code 01: G-Force Compensation - Phase {self.phase_gforce}]")
        print(f"Current Stress: {current_g}G Detected.")
        time.sleep(1.2)
        
        if current_g > 7:
            print("Action: Inflating G-suit and adjusting oxygen pressure...")
            print("Status: Preventing Pilot GLOC (G-induced Loss Of Consciousness).")
            return "G-Status: STABILIZED"
        else:
            print("Status: Normal G-load. Systems monitoring...")
            return "G-Status: OPTIMAL"

    # Phase 1913: Automatic Ejection System (स्वचालित बचाव प्रणाली)
    def check_ejection_criteria(self, altitude, speed, hull_failure):
        print(f"\n[Code 02: Emergency Ejection - Phase {self.phase_ejection}]")
        time.sleep(1.5)
        
        if hull_failure == True and altitude < 500:
            print("CRITICAL: Unrecoverable failure detected at low altitude!")
            print("Action: Initiating Automatic Ejection Sequence...")
            print("Status: Canopy Blown. Rockets Fired. Pilot Safe.")
            return "Ejection: ACTIVATED"
        else:
            print("Status: Aircraft within safe operating parameters.")
            return "Ejection: STANDBY"

if __name__ == "__main__":
    safety_ai = FighterSafetySystem()
    
    # दोनों फेजेस का निष्पादन
    g_report = safety_ai.compensate_gforce(9.2) # High speed turn
    e_report = safety_ai.check_ejection_criteria(300, 1200, True)
    
    print(f"\n--- Pilot Life-Support Summary ---")
    print(f"Report: {g_report} | {e_report}")
