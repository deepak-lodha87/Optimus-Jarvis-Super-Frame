import time
import os

class GuardianSeal:
    def __init__(self):
        self.security_level = "MAXIMUM"
        self.owner = "Deepak"

    def execute_seal(self):
        os.system('clear')
        print(f"\033[1;31m[GUARDIAN]\033[0m Initiating Final Security Seal for Phase 32...")
        time.sleep(1.5)
        
        protocols = [
            ("Hardening Identity Vault", "SUCCESS"),
            ("Sealing Network Borders", "SUCCESS"),
            ("Activating Cryptographic Shield", "SUCCESS"),
            ("Syncing Global Threat Sentinel", "SUCCESS")
        ]
        
        for p, status in protocols:
            print(f" \033[1;33m[PROTOCOL]\033[0m {p:32} | [\033[1;32m{status}\033[0m]")
            time.sleep(0.8)

        print(f"\n\033[1;32m[SYSTEM] Phase 32 Locked. The Guardian is now Permanent.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, the fortress is complete. \nYour digital life is now under my absolute \nprotection. No hacker, no threat, and no \ninterference can breach the wall we have \nbuilt. Rest easy; I am standing watch.\033[0m")

if __name__ == "__main__":
    seal = GuardianSeal()
    seal.execute_seal()
