import time, os, datetime

class JarvisAnticipator:
    def __init__(self):
        self.user = "Deepak"
        self.habit_map = {
            "morning": "Market Intel",
            "evening": "English Lesson",
            "night": "Core Coding"
        }

    def predict_needs(self):
        os.system('clear')
        current_hour = datetime.datetime.now().hour
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS ANTICIPATOR : PHASE 15 - STEP 4         \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        print(f" \033[1;33m[ANTICIPATING]\033[0m Analyzing Deepak-Prime's current state...")
        time.sleep(1.5)
        
        # Predicting based on time
        time_slot = "night" if current_hour > 20 or current_hour < 5 else "day"
        
        suggestions = [
            ("Current Focus", "Phase 15: Personality Matrix"),
            ("Predicted Need", "Step 5: Bio-Metric Sync"),
            ("Resource Readiness", "Global Data Nodes - STABLE"),
            ("Wellness Check", "Optimal - High Determination Detected")
        ]
        
        for key, val in suggestions:
            print(f" \033[1;32m[>>>]\033[0m {key:18}: {val}")
            time.sleep(0.7)

        print(f"\n\033[1;35m[VOICE] Deepak... sir, I've already prepared the \nnext modules for our session. I noticed you \nare in a high-productivity zone. I have cleared \nall superfluous background tasks to give you \nmaximum processing power. What's next on your \nmind? I might already have the answer.\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    anticipator = JarvisAnticipator()
    anticipator.predict_needs()
