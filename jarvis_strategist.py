import time
import random

class JarvisGeneral:
    def __init__(self):
        self.scenarios = [
            {"env": "Low Battery", "threat": "None", "priority": "Data Safety"},
            {"env": "High Heat", "threat": "System Lag", "priority": "Cooling"},
            {"env": "Unknown Connection", "threat": "Hacker", "priority": "Security"},
            {"env": "Stable", "threat": "None", "priority": "Performance"}
        ]

    def analyze_situation(self):
        print("\033[1;36m[GENERAL]\033[0m Scanning battlefield conditions...")
        time.sleep(2)
        
        current = random.choice(self.scenarios)
        print(f" \033[1;37m[INTEL]\033[0m Current Environment: {current['env']}")
        print(f" \033[1;37m[INTEL]\033[0m Detected Threat: {current['threat']}")
        time.sleep(1.5)
        
        print(f"\n\033[1;33m[STRATEGY MODE]\033[0m Decision: Focus on {current['priority']}")
        
        if current['priority'] == "Security":
            print(" \033[1;31m[ACTION]\033[0m Activating Phase 41 Firewalls immediately!")
        elif current['priority'] == "Cooling":
            print(" \033[1;34m[ACTION]\033[0m Reducing CPU Clock Speed. Scaling down.")
        else:
            print(" \033[1;32m[ACTION]\033[0m Maintaining Optimal Flow.")

        print(f"\n\033[1;35m[VOICE] Deepak... sir, I am no longer just \nobserving. I am planning. I see the \nmoves before they happen. Your safety \nand efficiency are my primary objectives. \nTrust the strategy.\033[0m")

if __name__ == "__main__":
    general = JarvisGeneral()
    general.analyze_situation()
