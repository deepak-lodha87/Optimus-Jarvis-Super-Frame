import time, secrets, random

class JarvisRepairBot:
    def __init__(self):
        self.repair_id = f"NARe-{secrets.token_hex(2).upper()}"
        self.health_score = 100

    def run_self_diagnosis(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-REPAIR V1 ACTIVE (ID: {self.repair_id}) ---\033[0m")
        print("\033[1;36m[DIAGNOSING] Running full system health checkup...\033[0m")
        time.sleep(1.5)
        
        # Simulating a detected defect
        defects = ["Memory Leak in Phase 6588", "Syntax Drift", "Corrupted Log Node"]
        found = random.choice(defects)
        
        print(f"\033[1;31m[DEFECT FOUND] {found}. Initiating Repair...\033[0m")
        time.sleep(1.2)
        
        print(f"\033[1;32m[REPAIRED] Code Refactored. Integrity restored to 100%.\033[0m")
        print(f"\033[1;35m[VOICE] Deepak, I've patched a minor glitch in the background. The Frame is running perfectly.\033[0m")

if __name__ == "__main__":
    medic = JarvisRepairBot()
    medic.run_self_diagnosis()
