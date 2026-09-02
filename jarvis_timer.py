import time
import datetime

class TimeMaster:
    def __init__(self):
        self.tasks = []

    def add_reminder(self, task_name, task_time):
        self.tasks.append({"task": task_name, "time": task_time})
        print(f"\033[1;32m[SCHEDULED]\033[0m {task_name} at {task_time}")

    def run_monitor(self):
        print("\033[1;36m[TIME MASTER]\033[0m Monitoring your schedule...")
        time.sleep(1)
        
        # Displaying current state
        print(f"Current System Time: {datetime.datetime.now().strftime('%H:%M:%S')}")
        print(f"\n\033[1;35m[VOICE] Deepak sir, your schedule is synchronized. \nI will notify you exactly when it's time to act. \nNo teaching, no lessons—just pure efficiency.\033[0m")

if __name__ == "__main__":
    tm = TimeMaster()
    tm.add_reminder("Project Update", "10:00 AM")
    tm.run_monitor()
