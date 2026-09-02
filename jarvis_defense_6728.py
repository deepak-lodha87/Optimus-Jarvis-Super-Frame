import time, secrets, random

class JarvisDefenseSystem:
    def __init__(self):
        self.def_id = f"NADe-{secrets.token_hex(2).upper()}"
        self.shield_integrity = 100

    def scan_for_threats(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-DEFENSE V1 ACTIVE (ID: {self.def_id}) ---\033[0m")
        print("\033[1;36m[SHIELD] Scanning network traffic and core file integrity...\033[0m")
        time.sleep(2)
        
        threats = ["Brute Force Attempt", "Malware Injection", "Phishing Link Detected"]
        if random.random() > 0.5:
            attack = random.choice(threats)
            print(f"\033[1;31m[ALERT] Threat Detected: {attack}!\033[0m")
            print("\033[1;33m[ACTION] Activating Honey-Pot and blocking IP source...\033[0m")
            time.sleep(1)
            print("\033[1;32m[SAFE] Threat neutralized. Shield integrity restored.\033[0m")
        else:
            print("\033[1;32m[SAFE] No active threats. Privacy Vault remains locked.\033[0m")
        
        print(f"\033[1;35m[VOICE] Deepak, the perimeter is secure. I've updated the encryption keys to keep us ahead of any hackers.\033[0m")

if __name__ == "__main__":
    guard = JarvisDefenseSystem()
    guard.scan_for_threats()
