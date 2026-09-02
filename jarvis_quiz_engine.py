import time, os

class QuizMentor:
    def __init__(self):
        self.subjects = {"Economics": "GDP & Inflation", "Sociology": "Social Change", "History": "1857 Revolt"}
        self.score = 0

    def start_mock_test(self):
        os.system('clear')
        print(f"\033[1;33m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS AI-TUTOR : PHASE 21 - STEP 6            \033[0m")
        print(f"\033[1;33m====================================================\033[0m")
        
        print("\033[1;34m[INITIATING]\033[0m Generating Subject-Specific Questions...")
        time.sleep(1.5)
        
        for sub, topic in self.subjects.items():
            print(f" \033[1;32m[QUIZ]\033[0m Testing \033[1;37m{sub}\033[0m on \033[1;36m{topic}\033[0m...")
            time.sleep(0.8)
            print(f"        -> Status: \033[1;32mQuestion Generated\033[0m")
            time.sleep(0.5)

        print(f"\n\033[1;32m[SUCCESS] Tutor is Ready. Master, shall we begin the test?\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, it's time to sharpen your \nmind. I have prepared a series of challenges \nbased on your BA syllabus. Don't fear failure; \nit is the first step to mastery. I will be \nwith you until every concept is internalized. \nLet's ace these exams together.\033[0m")
        print(f"\033[1;33m====================================================\033[0m")

if __name__ == "__main__":
    mentor = QuizMentor()
    mentor.start_mock_test()
