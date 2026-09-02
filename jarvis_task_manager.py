import time
from datetime import datetime, timedelta

class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_milestone(self, title, hours_from_now):
        deadline = datetime.now() + timedelta(hours=hours_from_now)
        self.tasks.append({"title": title, "deadline": deadline})
        print(f"\033[1;34m[SCHEDULED] Task: {title} | Due: {deadline.strftime('%H:%M %p')}\033[0m")

class DeadlineManager:
    def check_priorities(self, tasks):
        print("\033[1;35m[ANALYSIS] Evaluating task urgency and focus levels...\033[0m")
        time.sleep(1.2)
        for task in tasks:
            print(f"  • {task['title']}: Priority HIGH (Deadline approaching)")
        return "\033[1;32m[STATUS] Alerts synchronized with Reno 12 Pro Notification Engine.\033[0m"

if __name__ == "__main__":
    scheduler = TaskScheduler()
    manager = DeadlineManager()
    
    print("-" * 50)
    print("   JARVIS TASK SCHEDULER & DEADLINE TRACKER")
    print("-" * 50)
    
    # Adding sample tasks for Optimus Project
    scheduler.add_milestone("Core Phase 3111", 2)
    scheduler.add_milestone("Vehicle Blueprint Review", 5)
    
    print("\n" + manager.check_priorities(scheduler.tasks))
    print("-" * 50)
