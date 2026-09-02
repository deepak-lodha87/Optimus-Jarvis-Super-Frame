import os

class IncomeSource:
    def __init__(self):
        self.master = "Deepak sir"
        self.skill_level = "Advanced Python Implementation"

    def analyze_potential(self):
        os.system('clear')
        print("\033[1;32m[MARKET ANALYSIS]\033[0m Checking Project Worth...")
        
        # Defining the two ways to earn
        print("1. Job Market: Python/Automation Expert")
        print("2. Digital Product: Optimus Jarvis Super-Frame SaaS")
        
        os.system('termux-tts-speak "Deepak sir, this project is an investment in your skills. It will not bring millions tomorrow, but it can build your career for a lifetime."')
        
        print("\n\033[1;33m[DECISION]\033[0m High Effort = High Skill = High Income (In Future)")

if __name__ == "__main__":
    IncomeSource().analyze_potential()
