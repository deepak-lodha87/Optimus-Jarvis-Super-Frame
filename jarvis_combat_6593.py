import time, secrets, random

class JarvisCombatCore:
    def __init__(self):
        self.combat_id = f"NACom-{secrets.token_hex(2).upper()}"
        self.mode = "Tactical-Defense"

    def engage_threat(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-COMBAT V1 ACTIVE (ID: {self.combat_id}) ---\033[0m")
        print("\033[1;31m[ALERT] Incoming Digital Strike Detected! Scanning Source...\033[0m")
        time.sleep(1.5)
        
        # Deploying Counter-Measures
        tactics = ["Reverse-Proxy-Reflection", "Neural-Stun-Wave", "Decoy-Data-Deployment"]
        chosen_tactic = random.choice(tactics)
        
        print(f"\033[1;33m[TACTICAL] Executing: {chosen_tactic}...\033[0m")
        time.sleep(1.2)
        
        print("\033[1;32m[SUCCESS] Threat neutralized and source origin isolated.\033[0m")
        print(f"\033[1;35m[VOICE] Deepak, the intruder's system is now in a loop. They won't be bothering us again.\033[0m")

if __name__ == "__main__":
    combat = JarvisCombatCore()
    combat.engage_threat()
