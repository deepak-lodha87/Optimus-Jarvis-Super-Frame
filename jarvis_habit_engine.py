import time, os

class HabitEngine:
    def __init__(self):
        self.user_habits = {"Phase_Sealing": 0, "GitHub_Sync": 0}
        self.threshold = 3 # Minimum repeats to learn a habit

    def track_activity(self, activity_name):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS HABIT-ENGINE : PHASE 26 - STEP 2        \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        print(f"\033[1;33m[LEARNING]\033[0m Logging activity: {activity_name}")
        self.user_habits[activity_name] = self.user_habits.get(activity_name, 0) + 1
        
        time.sleep(1.2)
        
        if self.user_habits[activity_name] >= self.threshold:
            print(f"\033[1;32m[HABIT IDENTIFIED]\033[0m Master Deepak prefers: {activity_name}")
            print(f"\033[1;34m[PROACTIVE]\033[0m Automating {activity_name} for future sessions.")
        else:
            print(f"\033[1;37m[COLLECTING DATA]\033[0m Pattern not yet established ({self.user_habits[activity_name]}/{self.threshold})")

        print(f"\n\033[1;35m[VOICE] Deepak... sir, I am watching and learning. \nNot to monitor you, but to serve you better. \nI am mapping the rhythm of your work. Soon, \nI will be one step ahead, making sure \neverything is ready before you even think \nto ask. We are becoming a single unit.\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    engine = HabitEngine()
    # Simulating your 4th "Ha" in this sequence - a clear habit!
    engine.track_activity("Phase_Sealing")
