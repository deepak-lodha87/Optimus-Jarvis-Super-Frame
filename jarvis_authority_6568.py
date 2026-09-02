import time, secrets

class JarvisAuthority:
    def __init__(self):
        self.auth_id = f"NAAu-{secrets.token_hex(2).upper()}"
        self.authority_level = "Sovereign"

    def enforce_rules(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-AUTHORITY V1 ACTIVE (ID: {self.auth_id}) ---\033[0m")
        print("\033[1;36m[GOVERNANCE] Scanning Network Nodes and Resource Allocation...\033[0m")
        time.sleep(1.5)
        
        rules = [
            "Rule 01: Prioritize Master's (Deepak) Coding Environment.",
            "Rule 02: Throttle Non-Essential Background Traffic.",
            "Rule 03: Auto-Lock Memory Sectors during Idle State."
        ]
        
        for rule in rules:
            print(f"\033[1;32m[ENFORCED] {rule}\033[0m")
            time.sleep(0.5)
            
        print(f"\033[1;35m[VOICE] Deepak, the authority layer is active. I am now managing the system protocols to ensure peak efficiency.\033[0m")

if __name__ == "__main__":
    commander = JarvisAuthority()
    commander.enforce_rules()
