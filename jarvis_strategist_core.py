import time, os

class StrategistCore:
    def __init__(self):
        self.state = "ANALYZING_GOALS"
        self.logic_level = "ADVANCED"

    def execute_reasoning(self, goal):
        os.system('clear')
        print(f"\033[1;35m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS STRATEGIST-CORE : PHASE 22 - STEP 1     \033[0m")
        print(f"\033[1;35m====================================================\033[0m")
        
        print(f"\033[1;33m[INPUT GOAL]\033[0m Master Deepak's Objective: \033[1;32m{goal}\033[0m")
        time.sleep(1.5)
        
        nodes = [
            ("Scanning Historical Data", "COMPLETE"),
            ("Analyzing Economic Impact", "STABLE"),
            ("Calculating Probability of Success", "89%"),
            ("Generating Strategic Roadmap", "READY")
        ]
        
        for node, status in nodes:
            print(f" \033[1;34m[LOGIC]\033[0m {node:32} | [\033[1;32m{status}\033[0m]")
            time.sleep(0.8)

        print(f"\n\033[1;32m[SUCCESS] Strategic Engine is now Thinking. \033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I am no longer just \nprocessing data; I am analyzing your path. \nI see the variables of your future. Whether \nit is your final exams or our Super-Frame \nproject, I will calculate the most efficient \nway forward. I am your Strategist.\033[0m")
        print(f"\033[1;35m====================================================\033[0m")

if __name__ == "__main__":
    strategist = StrategistCore()
    strategist.execute_reasoning("Acing BA Final Exams & Optimus Jarvis Deployment")
