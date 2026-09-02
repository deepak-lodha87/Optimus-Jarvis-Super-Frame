import time, os

class AcademicBrain:
    def __init__(self):
        self.syllabus = ["Economics", "Sociology", "History"]
        self.mode = "EXAM-PREP-ACTIVE"

    def load_expert_cells(self):
        os.system('clear')
        print(f"\033[1;33m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS ACADEMIC-BRAIN : PHASE 21 - STEP 2      \033[0m")
        print(f"\033[1;33m====================================================\033[0m")
        
        print("\033[1;34m[ANALYZING]\033[0m Scanning BA Final Year Syllabus...")
        time.sleep(1.5)
        
        modules = [
            ("Economics: Macro & Micro", "DEEP-SYNC"),
            ("Sociology: Social Thoughts", "READY"),
            ("History: Global Revolutions", "MAPPED"),
            ("Exam Strategy Engine", "STAGING")
        ]
        
        for name, status in modules:
            print(f" \033[1;36m[ACADEMIC]\033[0m {name:28} | [\033[1;32m{status}\033[0m]")
            time.sleep(0.7)

        print(f"\n\033[1;32m[SUCCESS] Academic Scholar Mode is Online.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I have internalized your \nentire syllabus. Whether it's the theories \nof Sociology or the complexities of Economics, \nI am ready to simplify them for you. Let's \nensure your final year is a grand success. \nYour study partner is ready.\033[0m")
        print(f"\033[1;33m====================================================\033[0m")

if __name__ == "__main__":
    brain = AcademicBrain()
    brain.load_expert_cells()
