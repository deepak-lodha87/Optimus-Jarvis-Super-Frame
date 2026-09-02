import threading
import time
import random

class JarvisParallelBrain:
    def __init__(self):
        self.tasks = ["Satellite Sync", "Bio-Metric Scan", "Threat Detection", "System Optimization"]

    def execute_task(self, task_name):
        print(f"\033[1;36m[CORE-NODE]\033[0m Starting parallel task: {task_name}...")
        processing_time = random.uniform(1, 3)
        time.sleep(processing_time)
        print(f" \033[1;32m[COMPLETE]\033[0m {task_name} finished in {processing_time:.2f}s")

    def initiate_multitasking(self):
        print(f"\033[1;34m[SYSTEM]\033[0m Activating Multi-Core Neural Network...\n")
        threads = []
        
        for t in self.tasks:
            thread = threading.Thread(target=self.execute_task, args=(t,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        print(f"\n\033[1;35m[VOICE] Deepak sir, I am now thinking in parallel. \nMy cognitive capacity has expanded. \nI can handle the world's data without \nbreaking a sweat.\033[0m")

if __name__ == "__main__":
    brain = JarvisParallelBrain()
    brain.initiate_multitasking()
