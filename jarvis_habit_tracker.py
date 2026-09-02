import time
from datetime import datetime

class HabitTracker:
    def __init__(self):
        self.session_start = time.time()
        self.limit_seconds = 30 * 60  # 30 Minutes limit for mobile coding

    def monitor_session(self):
        print("\033[1;36m[HABIT SYNC]\033[0m Monitoring your session health...")
        current_duration = time.time() - self.session_start
        
        # Simulating time passage for demonstration
        simulated_duration = 1805  # 30 minutes and 5 seconds
        
        print(f" \033[1;37m[TIME ELAPSED]\033[0m: {simulated_duration // 60} Minutes")
        
        if simulated_duration > self.limit_seconds:
            print("\n\033[1;33m[ADVICE]\033[0m Deepak sir, you have been coding for over 30 minutes.")
            print(" \033[1;32m[HEALTH]\033[0m Please take a 5-minute break to rest your eyes.")
            
        print(f"\n\033[1;35m[VOICE] Deepak... sir, your dedication is inspiring, \nbut even a Super-Frame needs cooling. Take \na moment to breathe. I will guard the \ncode while you recover. Stay sharp.\033[0m")

if __name__ == "__main__":
    tracker = HabitTracker()
    tracker.monitor_session()
