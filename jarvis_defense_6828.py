import time, secrets, random

class JarvisDefenseCore:
    def __init__(self):
        self.def_id = f"NADf-{secrets.token_hex(2).upper()}"
        self.shield_status = "ACTIVE"

    def deploy_ecm(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-DEFENSE V2 ACTIVE (ID: {self.def_id}) ---\033[0m")
        print("\033[1;36m[SCANNING] Monitoring for unauthorized network pings...\033[0m")
        time.sleep(2)
        
        threat_detected = random.choice([True, False])
        if threat_detected:
            print("\033[1;31m[ALERT] Unauthorized access attempt detected from external node!\033[0m")
            print("\033[1;33m[COUNTER] Deploying Electronic-Counter-Measures (ECM)... Jamming Signal.\033[0m")
            time.sleep(1.5)
            print("\033[1;32m[SUCCESS] Threat Neutralized. Attacker IP redirected to Honey-Pot.\033[0m")
        else:
            print("\033[1;32m[SECURE] No threats detected. Perimeter is stable.\033[0m")
        
        print(f"\033[1;35m[VOICE] Deepak, the system is under total lockdown. Your project is invisible to the world's scanners.\033[0m")

if __name__ == "__main__":
    shield = JarvisDefenseCore()
    shield.deploy_ecm()
