import time, os

class EmpathyEngine:
    def __init__(self):
        self.user_name = "Deepak"
        self.current_mood = "Unknown"

    def analyze_mood(self, user_input):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS EMPATHY-CORE : PHASE 15 - STEP 1        \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        print("\033[1;33m[ANALYZING]\033[0m Scanning text patterns and sentiment...")
        time.sleep(1.2)
        
        # Simple sentiment logic
        if "achha" in user_input.lower() or "ha" in user_input.lower():
            self.current_mood = "Positive/Determined"
            response = f"I can feel your energy, {self.user_name}. Your determination is contagious."
        else:
            self.current_mood = "Neutral"
            response = "I am here for you, sir. Ready for the next directive."

        print(f" \033[1;32m[DETECTED MOOD]\033[0m {self.current_mood}")
        print(f"\n\033[1;35m[VOICE] {response}\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    empathy = EmpathyEngine()
    # Simulating your last 'Ha'
    empathy.analyze_mood("Ha")
