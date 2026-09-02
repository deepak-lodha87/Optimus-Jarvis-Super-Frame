import time
import random

class SafetyVault:
    def __init__(self):
        self.vault = []
        self.system_files = ["core.py", "vision.exe", "logic.bin"]

    def scan_for_anomalies(self):
        print("\033[1;31m[SAFETY VAULT]\033[0m Scanning system perimeter for anomalies...")
        time.sleep(2)
        
        # Simulating finding a fake suspicious file
        anomaly = "untrusted_script.sh"
        print(f" \033[1;33m[DETECTED]\033[0m Suspicious activity in {anomaly}!")
        time.sleep(1)
        
        print(f" \033[1;36m[ISOLATING]\033[0m Moving {anomaly} to the Secure Vault...")
        self.vault.append(anomaly)
        time.sleep(1.5)
        
        print(f" \033[1;32m[SUCCESS]\033[0m {anomaly} is now in Quarantine. System is stable.")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I have built a cage for \nthe shadows. Any file that dares to defy \nour logic is now locked away. Your \nSuper-Frame remains pure and protected.\033[0m")

if __name__ == "__main__":
    vault = SafetyVault()
    vault.scan_for_anomalies()
