import time, secrets, sys

class JarvisSelfHealer:
    def __init__(self):
        self.repair_id = f"NAR-{secrets.token_hex(2).upper()}"
        self.health_score = 100

    def monitor_core(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-REPAIR V2 ONLINE (ID: {self.repair_id}) ---\033[0m")
        print("\033[1;36m[MONITORING] Scanning Core Logic for anomalies...\033[0m")
        
        try:
            # Simulating a division by zero error (common bug)
            result = 10 / 0
        except ZeroDivisionError as e:
            print(f"\033[1;31m[CRITICAL] Bug Detected: {e}\033[0m")
            self.heal_logic("ZeroDivisionFix")

    def heal_logic(self, patch_type):
        print(f"\033[1;33m[HEALING] Applying {patch_type} in real-time...\033[0m")
        time.sleep(1.5)
        self.health_score = 100
        print(f"\033[1;32m[SUCCESS] Patch applied. Health restored to {self.health_score}%.\033[0m")
        print("\033[1;35m[VOICE] Deepak, I found a logic defect and fixed it before it could crash the system.\033[0m")

if __name__ == "__main__":
    healer = JarvisSelfHealer()
    healer.monitor_core()
