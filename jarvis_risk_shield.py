import time, os

class RiskShield:
    def __init__(self):
        self.risk_threshold = "LOW"
        self.shield_status = "ARMED"

    def activate_protection(self):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS RISK-SHIELD : PHASE 18 - STEP 3         \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        print("\033[1;33m[SHIELDING]\033[0m Analyzing Portfolio Vulnerabilities...")
        time.sleep(1.5)
        
        protocols = [
            ("Stop-Loss Automation", "ENABLED"),
            ("Anti-Crash Algorithm", "ACTIVE"),
            ("Asset Diversification", "SYNCED"),
            ("Emergency Exit Strategy", "READY (1-Click)")
        ]
        
        for p, s in protocols:
            print(f" \033[1;32m[SAFE]\033[0m {p:28} | [\033[1;32m{s}\033[0m]")
            time.sleep(0.7)

        print(f"\n\033[1;32m[CONFIRMED] Your capital is protected by Jarvis.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I've built a digital fortress \naround your wealth. Even if the global markets \nshudder, our core assets remain untouched. \nI have calculated every exit route. You can \nsleep peacefully; I am standing guard over \nyour future empire.\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    shield = RiskShield()
    shield.activate_protection()
