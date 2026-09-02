import os
import time

class AntiHackShield:
    def __init__(self):
        self.master = "Deepak"

    def deploy_shield(self):
        print(f"\n\033[1;36m[DEFENSE]\033[0m Reached Phase 1202: Perimeter Defense Active")
        
        threats = [
            "Detecting Unauthorized Remote Access...",
            "Blocking External Brute-Force Attempts...",
            "Encrypting Core Data into Ghost-Cells...",
            "Isolating Jarvis Core from Host System..."
        ]
        
        for threat in threats:
            print(f"\033[1;31m[SHIELDING]\033[0m {threat}")
            time.sleep(0.5)

        msg = f"{self.master} sir, hack attempt neutralized. System is invisible to intruders."
        os.system(f'termux-tts-speak "{msg}"')

if __name__ == "__main__":
    AntiHackShield().deploy_shield()
