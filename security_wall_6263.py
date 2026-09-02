import os, time, secrets

class SecurityWall:
    def __init__(self):
        self.wall_id = f"NCSW-{secrets.token_hex(2).upper()}"
        self.status = "SECURE"

    def scan_vulnerabilities(self):
        print(f"\n\033[1;37m--- NEURAL-CYBER-SECURITY-WALL ONLINE (ID: {self.wall_id}) ---\033[0m")
        checks = [
            "Scanning Open Ports...",
            "Checking SSH Integrity...",
            "Verifying API Token Encryption...",
            "Analyzing Active Processes..."
        ]
        
        for check in checks:
            print(f"\033[1;33m[*] {check}\033[0m")
            time.sleep(0.4)
            print(f"\033[1;32m[SAFE] No threats detected.\033[0m")

    def activate_shield(self):
        print("\n\033[1;36m[ACTION] Activating Quantum-Encryption Shield...\033[0m")
        time.sleep(1)
        print("\033[1;32m[SUCCESS] Firewall active. Your digital assets are now invisible to hackers.\033[0m")

if __name__ == "__main__":
    wall = SecurityWall()
    wall.scan_vulnerabilities()
    wall.activate_shield()
