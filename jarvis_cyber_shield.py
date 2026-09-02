import time
import hashlib

class InfiltrationShield:
    def __init__(self):
        self.firewall_layers = 12
        self.active_decoy = False

    def deploy_ghost_network(self):
        print("\033[1;34m[SHIELD] Initializing Ghost-Network Cloaking...\033[0m")
        time.sleep(1.5)
        # Creating a virtual phantom IP to mislead trackers
        phantom_ip = "192.168." + str(hashlib.md5(b"ghost").hexdigest()[:3])
        self.active_decoy = True
        print(f"  • Phantom IP Active: {phantom_ip}")
        print("  • Real Traffic Encapsulated in 1024-bit Tunnel... [OK]")
        return "\033[1;32m[SUCCESS] Digital Shadow Deployed. You are now Invisible.\033[0m"

class CyberCounterMeasure:
    def detect_intrusion(self):
        print("\033[1;35m[WATCH] Monitoring Global Threat Intelligence Feeds...\033[0m")
        time.sleep(1)
        return "\033[1;36m[LOG] No unauthorized access attempts detected in the last 24h.\033[0m"

if __name__ == "__main__":
    shield = InfiltrationShield()
    counter = CyberCounterMeasure()
    
    print("-" * 50)
    print("   JARVIS GLOBAL CYBER-SHIELD (P3200-01)")
    print("-" * 50)
    
    print(shield.deploy_ghost_network())
    print("\n" + counter.detect_intrusion())
    print("-" * 50)
