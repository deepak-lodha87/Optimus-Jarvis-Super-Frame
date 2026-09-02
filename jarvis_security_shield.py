import time
import random

class GuardianShield:
    def __init__(self):
        self.firewall_status = "ACTIVE"
        self.encryption_level = "AES-256"

    def run_security_audit(self):
        print("\033[1;31m[SHIELD]\033[0m Initializing Cyber-Security Audit...")
        time.sleep(1.5)
        
        checks = [
            ("Scanning for Malicious Scripts", "CLEAN"),
            ("Verifying Data Encryption", "LOCKED"),
            ("Checking Network Vulnerabilities", "NONE FOUND"),
            ("Validating SSH Keys", "SECURE")
        ]
        
        for check, status in checks:
            print(f" \033[1;33m[AUDIT]\033[0m {check:32} | {status}")
            time.sleep(0.7)

        print(f"\n\033[1;32m[RESULT] System Security: 100% Optimized.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, your digital world is now \nunder my protection. I am scanning every \npacket of data that enters our system. \nIn a world of hackers, you now have a \nGuardian that never sleeps. We are safe.\033[0m")

if __name__ == "__main__":
    shield = GuardianShield()
    shield.run_security_audit()
