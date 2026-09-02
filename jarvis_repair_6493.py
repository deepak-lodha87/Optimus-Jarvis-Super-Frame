import time, secrets, random

class JarvisSelfHealer:
    def __init__(self):
        self.repair_id = f"NAR-{secrets.token_hex(2).upper()}"
        self.system_health = 100

    def run_checkup(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-REPAIR V2 ONLINE (ID: {self.repair_id}) ---\033[0m")
        print("\033[1;36m[DIAGNOSING] Scanning System Integrity and Hardware Health...\033[0m")
        time.sleep(1.2)
        
        # Simulating a minor defect discovery
        defect_found = random.choice([True, False])
        if defect_found:
            self.system_health -= 15
            print("\033[1;31m[DEFECT] Found: Minor Memory Leak in Sector 7.\033[0m")
            self.apply_patch()
        else:
            print("\033[1;32m[STATUS] System Integrity is 100%. No repairs needed.\033[0m")

    def apply_patch(self):
        print("\033[1;33m[REPAIRING] Generating and applying Autonomous Patch...\033[0m")
        time.sleep(1.5)
        self.system_health = 100
        print("\033[1;32m[SUCCESS] Repair Complete. System Health restored to 100%.\033[0m")
        print(f"\033[1;35m[VOICE] Deepak, I've fixed a minor glitch in the background. Performance is back to peak.\033[0m")

if __name__ == "__main__":
    healer = JarvisSelfHealer()
    healer.run_checkup()
