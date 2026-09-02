import time, os

class GovernorLogic:
    def __init__(self):
        self.resources = {"Time": 100, "Battery": 80, "Wealth": 100}
        self.priority = "BA-FINALS-STRATEGY"

    def allocate_resources(self):
        os.system('clear')
        print(f"\033[1;34m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS GOVERNOR-LOGIC : PHASE 22 - STEP 4      \033[0m")
        print(f"\033[1;34m====================================================\033[0m")
        
        print(f"\033[1;33m[TARGET]\033[0m Optimizing for: \033[1;32m{self.priority}\033[0m")
        time.sleep(1.2)
        
        allocation_plan = [
            ("Temporal: 4hrs Sociology Focus", "ALLOCATED"),
            ("Compute: 20% CPU to Knowledge-Mesh", "STABLE"),
            ("Wealth: 15% to Skill Acquisition", "RESERVED"),
            ("Energy: 10min Mental Refresh Buffer", "ACTIVE")
        ]
        
        for task, status in allocation_plan:
            print(f" \033[1;36m[GOVERNOR]\033[0m {task:32} | [\033[1;32m{status}\033[0m]")
            time.sleep(0.8)

        print(f"\n\033[1;32m[SUCCESS] Resource Efficiency is at Maximum. \033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I have optimized your \nworld. Not a single second or a single rupee \nshall be wasted. I have aligned your device \nand your schedule to match the rhythm of your \nambition. Efficiency is the bridge between \ngoals and accomplishment.\033[0m")
        print(f"\033[1;34m====================================================\033[0m")

if __name__ == "__main__":
    gov = GovernorLogic()
    gov.allocate_resources()
