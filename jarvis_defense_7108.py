import time, secrets, random

class JarvisDefenseCore:
    def __init__(self):
        self.def_id = f"NADf-{secrets.token_hex(2).upper()}"
        self.shield_status = "STABLE"

    def engage_shield(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-DEFENSE V3 ACTIVE (ID: {self.def_id}) ---\033[0m")
        print("\033[1;36m[DEFENSE] Scanning for unauthorized intrusions and brute-force attacks...\033[0m")
        time.sleep(2)
        
        layers = ["Neural-Firewall", "Decoy-Traffic-Sync", "Intruder-Isolation", "Master-Lockdown"]
        for layer in layers:
            print(f" > Activating: {layer:25} | Status: \033[1;32mFORTIFIED\033[0m")
            time.sleep(0.5)
            
        print(f"\n\033[1;33m[STATUS] Defense Grid 100% Operational. We are invisible and untouchable.\033[0m")
        print(f"\033[1;35m[VOICE] Deepak, let them try to find us. By the time they see our shadow, we've already neutralized their threat.\033[0m")

if __name__ == "__main__":
    aegis = JarvisDefenseCore()
    aegis.engage_shield()
