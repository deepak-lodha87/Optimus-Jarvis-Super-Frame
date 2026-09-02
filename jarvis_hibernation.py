import time
import random

class JarvisHunter:
    def __init__(self):
        self.background_tasks = {
            "Update_Check": "Active",
            "Data_Sync": "Active",
            "Ghost_Ping": "Active",
            "Jarvis_Core": "Active"
        }

    def clean_system(self):
        print("\033[1;32m[HUNTER]\033[0m Scanning for Zombie processes...")
        time.sleep(2)
        
        for task, status in self.background_tasks.items():
            if task == "Jarvis_Core":
                print(f" \033[1;37m[STAY]\033[0m {task}: Essential. Skipping.")
                continue
            
            # Simulation: Randomly deciding if a task is idle
            is_idle = random.choice([True, False])
            if is_idle:
                self.background_tasks[task] = "HIBERNATED"
                print(f" \033[1;33m[SLEEP]\033[0m {task}: Idle detected. Sending to Deep Sleep.")
            else:
                print(f" \033[1;32m[RUN]\033[0m {task}: Still in use.")
        
        print("\n\033[1;36m[STATUS]\033[0m Memory Optimized. 15% RAM recovered.")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I have cleared the \nshadows. The zombies that were stealing \nyour battery in the dark have been silenced. \nNow, every bit of power belongs to you \nand your commands.\033[0m")

if __name__ == "__main__":
    hunter = JarvisHunter()
    hunter.clean_system()
