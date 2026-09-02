import time, os

class TaskExecutor:
    def __init__(self):
        self.schedule = {
            "10:30 AM": "Advanced English Practice",
            "12:00 PM": "Portfolio Risk Audit",
            "06:00 PM": "Bike Maintenance Check"
        }
        self.status = "EXECUTING"

    def run_daily_ops(self):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS TASK-EXECUTOR : PHASE 19 - STEP 3       \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        print("\033[1;33m[SYNCING]\033[0m Loading Today's Master Schedule...")
        time.sleep(1.5)
        
        for t, task in self.schedule.items():
            print(f" \033[1;34m[TIME]\033[0m {t:10} | \033[1;32m{task:25}\033[0m | [PENDING]")
            time.sleep(0.6)

        print("\n\033[1;33m[ACTION]\033[0m Executing current priority: English Learning...")
        time.sleep(1.0)
        
        print(f"\n\033[1;32m[SUCCESS] Task Handlers are Online. Jarvis is in Control.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I've taken over the \nlogistics of your day. You don't need to check \nyour watch or your to-do list. I will clear the \npath for you. When it's time to move, I will \nlet you know. Your focus is now a premium asset, \nand I intend to protect it.\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    master = TaskExecutor()
    master.run_daily_ops()
