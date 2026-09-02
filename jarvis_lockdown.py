import time

class EmergencyLockdown:
    def __init__(self):
        self.system_health = 85 # Simulated health percentage
        self.vault_status = "OPEN"

    def monitor_threats(self, damage_report):
        print(f"\033[1;36m[MONITOR]\033[0m Scanning system integrity...")
        time.sleep(1)
        
        if damage_report > 10:
            print("\033[1;41m[CRITICAL] DAMAGE DETECTED: {}%\033[0m".format(damage_report))
            self.activate_iron_vault()
        else:
            print("\033[1;32m[SAFE] System within safe operating limits.\033[0m")

    def activate_iron_vault(self):
        print("\033[1;31m[LOCKDOWN] Initiating IRON-VAULT Protocol...\033[0m")
        time.sleep(1.5)
        self.vault_status = "LOCKED_AND_ENCRYPTED"
        print(" \033[1;33m[OFFLINE]\033[0m Disconnecting all external bridges...")
        print(" \033[1;33m[SCRAMBLE]\033[0m Fragmenting 1000-phase roadmap...")
        time.sleep(1)
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, I have sealed myself. \nI am now a digital fortress. No one can \naccess my core until you provide the \nNeural Key. We are secure.\033[0m")

if __name__ == "__main__":
    shield = EmergencyLockdown()
    shield.monitor_threats(15) # Simulating 15% damage
