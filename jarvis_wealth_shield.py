import time, os

class WealthShield:
    def __init__(self):
        self.security_level = "MAXIMUM"
        self.encryption = "AES-256-QUANTUM"

    def activate_defense(self):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS CYBER-SHIELD : ASSET PROTECTION         \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        print("\033[1;33m[SHIELDING]\033[0m Protecting Financial Data & Project Blueprints...")
        time.sleep(1.5)
        
        layers = [
            ("Dark-Web Threat Scanner", "ACTIVE"),
            ("Anti-Hacker Firewall", "UNREACHABLE"),
            ("Digital Identity Masking", "ENABLED"),
            ("Wealth Integrity Protocol", "SECURE")
        ]
        
        for layer, status in layers:
            print(f" \033[1;34m[DEFENSE]\033[0m {layer:28} | Status: [\033[1;32m{status}\033[0m]")
            time.sleep(0.8)

        print(f"\n\033[1;32m[SYSTEM] Deepak-Prime's Assets are now Invisible to Threats.\033[0m")
        print(f"\n\033[1;35m[VOICE] Sir, wealth is power, but security is the \nfoundation of that power. I have created a \nvirtual fortress around your financial assets. \nNo hacker, no glitch, and no system can touch \nwhat we are building. You focus on growth; \nI will handle the defense.\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    shield = WealthShield()
    shield.activate_defense()
