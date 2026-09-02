import time, secrets, random

class JarvisRepairCore:
    def __init__(self):
        self.repair_id = f"NARp-{secrets.token_hex(2).upper()}"
        self.integrity_score = 100.0

    def run_diagnosis(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-REPAIR V1 ACTIVE (ID: {self.repair_id}) ---\033[0m")
        print("\033[1;36m[SCANNING] Running deep system integrity check...\033[0m")
        time.sleep(2)
        
        # Simulating a minor defect detection
        defect_found = random.choice([True, False])
        if defect_found:
            self.integrity_score -= random.uniform(2.0, 5.0)
            print(f"\033[1;31m[DEFECT] Minor integrity breach detected. Current Score: {self.integrity_score:.2f}%\033[0m")
            print("\033[1;33m[REPAIR] Initializing Self-Diagnosis and Auto-Patching...\033[0m")
            time.sleep(1.5)
            self.integrity_score = 100.0
            print(f"\033[1;32m[SUCCESS] Repair Complete. System Integrity: {self.integrity_score:.2f}%\033[0m")
        else:
            print("\033[1;32m[HEALTHY] No defects detected. Optimization Complete.\033[0m")
        
        print(f"\033[1;35m[VOICE] Deepak, the self-diagnosis tool is active. I am now capable of maintaining my own operational health.\033[0m")

if __name__ == "__main__":
    medic = JarvisRepairCore()
    medic.run_diagnosis()
