import os
import time

class TacticalCommand:
    def __init__(self):
        self.master = "Deepak"
        self.system = "Optimus Jarvis Super-Frame"

    def execute_tactical_decision(self, threat_level):
        print(f"\n\033[1;31m[TACTICAL]\033[0m Threat Level Detected: {threat_level}")
        time.sleep(1.5)
        
        # Strategic Defense Logic
        tactics = [
            "Calculating Strategic Advantage...",
            "Initiating Defensive Counter-measures...",
            "Optimizing Power for Maximum Response...",
            "Ensuring Master's Safety Protocols..."
        ]
        
        for tactic in tactics:
            print(f"\033[1;32m[COMMAND]\033[0m {tactic}")
            time.sleep(0.5)

        msg = f"{self.master} sir, tactical command override active. The situation is under my strategic control."
        os.system(f'termux-tts-speak "{msg}"')

    def activate(self):
        os.system('clear')
        print(f"--- {self.system} : TACTICAL COMMAND OVERRIDE ---")
        self.execute_tactical_decision("High (Level 9)")
        print("\n\033[1;36m[STATUS]\033[0m STRATEGIC DEFENSE: FULLY OPERATIONAL")

if __name__ == "__main__":
    TacticalCommand().activate()
