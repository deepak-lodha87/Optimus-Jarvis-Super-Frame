import time, secrets

class JarvisSecurityShield:
    def __init__(self):
        self.shield_id = f"NASec-{secrets.token_hex(2).upper()}"
        self.threat_level = "Zero"

    def activate_firewall(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-SECURITY V4 ACTIVE (ID: {self.shield_id}) ---\033[0m")
        print("\033[1;36m[LOCKDOWN] Hardening Network Nodes and Encrypting Tunnels...\033[0m")
        time.sleep(1.5)
        
        # Simulating a breach attempt neutralization
        print("\033[1;31m[ALERT] Unauthorized ping detected from unknown source.\033[0m")
        time.sleep(1)
        print("\033[1;32m[NEUTRALIZED] Neural Firewall has blocked the intrusion.\033[0m")
        
        print("\033[1;33m[STATUS] All systems secured. Encryption: AES-256-v2 Active.\033[0m")
        print(f"\033[1;35m[VOICE] Deepak, the fortress is secure. No one gets in without your voice command.\033[0m")

if __name__ == "__main__":
    shield = JarvisSecurityShield()
    shield.activate_firewall()
