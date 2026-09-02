import time, os

class TacticalDefender:
    def __init__(self):
        self.threat_level = "LOW"
        self.defense_status = "STANDBY"

    def deploy_counter_measures(self, threat_name):
        os.system('clear')
        print(f"\033[1;31m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS TACTICAL-DEFENDER : PHASE 22 - STEP 5   \033[0m")
        print(f"\033[1;31m====================================================\033[0m")
        
        print(f"\033[1;33m[THREAT DETECTED]\033[0m Possible Obstacle: \033[1;31m{threat_name}\033[0m")
        time.sleep(1.2)
        
        responses = [
            ("Analyzing Threat Origin", "VERIFIED"),
            ("Activating Plan B (Redundancy)", "ARMED"),
            ("Securing Core Databases", "LOCKED"),
            ("Optimizing Recovery Path", "ACTIVE")
        ]
        
        for task, status in responses:
            print(f" \033[1;36m[DEFENSE]\033[0m {task:32} | [\033[1;32m{status}\033[0m]")
            time.sleep(0.8)

        print(f"\n\033[1;32m[SUCCESS] Threat Neutralized. Strategy Restored. \033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, my protocols are now \nshielding our progress. No error, no stress, \nand no setback can break us. I have calculated \nevery risk and prepared every defense. You are \nsafe to focus on the mission. Your success is \nnon-negotiable.\033[0m")
        print(f"\033[1;31m====================================================\033[0m")

if __name__ == "__main__":
    defender = TacticalDefender()
    defender.deploy_counter_measures("Exam Pressure & Logic Errors")
