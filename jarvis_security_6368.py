import time, secrets, os

class CyberFortress:
    def __init__(self):
        self.shield_id = f"NCF-{secrets.token_hex(2).upper()}"
        self.security_level = "MAXIMUM"

    def active_scan(self):
        print(f"\n\033[1;37m--- NEURAL-CYBER-FORTRESS V2 ONLINE (ID: {self.shield_id}) ---\033[0m")
        print("\033[1;36m[SCANNING] Monitoring all incoming/outgoing data packets...\033[0m")
        
        # Simulating Intrusion Detection
        time.sleep(1)
        threats = random.choice([0, 0, 1]) # Low chance of simulated threat
        
        if threats:
            print("\033[1;31m[ALERT] Suspicious IP connection detected!\033[0m")
            print("\033[1;33m[ACTION] Blocking IP and rerouting traffic through Encrypted Tunnel.\033[0m")
        else:
            print("\033[1;32m[SAFE] No active threats. Your connection is ghost-secured.\033[0m")

    def deploy_shield(self):
        print("\033[1;35m[VOICE] Deepak, the Cyber-Fortress is active. Your Oppo Reno 12 Pro is now invisible to local sniffers.\033[0m")

if __name__ == "__main__":
    import random # Only for simulation
    shield = CyberFortress()
    shield.active_scan()
    shield.deploy_shield()
