import time
import random

class JarvisAdvancedDiagnostics:
    def __init__(self):
        self.phase_503 = "503.Self-Diagnosis-Core"
        self.phase_504 = "504.Strategic-Defense-Alert"
        self.system_health = 100
        self.offline_mode = False

    def run_self_diagnosis(self):
        print(f"\n--- [SYSTEM] Initializing {self.phase_503} ---")
        time.sleep(1)
        print("[JARVIS]: Running Full System Scan...")
        time.sleep(2)
        
        # Simulating a potential defect (Electrical or Offline)
        defects = ["Electrical-Short", "Offline-Logic-Error", "None"]
        current_defect = random.choice(defects)
        
        if current_defect == "Electrical-Short":
            print("[CRITICAL]: Defect detected! Source: ELECTRICAL.")
            print("[SOLUTION]: Reroute power to secondary capacitors. Check physical wiring.")
            self.system_health = 75
        elif current_defect == "Offline-Logic-Error":
            print("[ALERT]: Defect detected! Source: OFFLINE LOGIC.")
            print("[SOLUTION]: Mirroring local database. Re-syncing encryption keys.")
            self.offline_mode = True
        else:
            print("[STATUS]: No defects found. System is fully stable.")
            self.system_health = 100

    def run_strategic_defense(self):
        print(f"\n--- [SYSTEM] Initializing {self.phase_504} ---")
        time.sleep(1)
        print("[JARVIS]: Activating Captain America Strategic Protocol...")
        
        # Strategic analysis for defense
        threat_level = "Medium"
        if self.system_health < 80 or self.offline_mode:
            print(f"[STRATEGY]: Shield deployed. Shifting to Stealth-Mode due to health drop.")
        else:
            print(f"[STRATEGY]: All systems optimal. Perimeter scanning active.")
        
        time.sleep(1.2)
        print(f"[FINAL REPORT]: Health {self.system_health}% | Offline Mode: {self.offline_mode}")
        print("[STATUS]: Phases 503 & 504 Consolidated Successfully.")

if __name__ == "__main__":
    jarvis = JarvisAdvancedDiagnostics()
    jarvis.run_self_diagnosis()
    jarvis.run_strategic_defense()
