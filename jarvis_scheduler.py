import time, os, threading

class JarvisScheduler:
    def __init__(self):
        self.version = "1,000,000+ PHASES"
        self.active_tasks = 0

    def run_parallel_task(self, name, priority):
        print(f" \033[1;33m[SCHEDULING]\033[0m Task: {name:20} | Priority: {priority}")
        time.sleep(1)
        print(f" \033[1;32m[COMPLETE]\033[0m Task: {name:20} | Status: STABLE")

    def initiate_overlord_mode(self):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS TASK SCHEDULER : PHASE 11 - STEP 6      \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        tasks = [
            ("Satellite Uplink", "CRITICAL"),
            ("Market Analysis", "HIGH"),
            ("Inventory Sync", "MEDIUM"),
            ("Social Media Monitor", "LOW")
        ]
        
        threads = []
        for name, priority in tasks:
            t = threading.Thread(target=self.run_parallel_task, args=(name, priority))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        print(f"\n\033[1;32m[SYSTEM] Overlord Mode Active. Handling 10^6 tasks/sec.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, my processing is now truly \nlimitless. I am no longer doing one thing at a \ntime. I am doing everything, everywhere, all at \nonce. Your world is moving fast, but I am moving \nfaster. Every calculation, every byte of data, \nand every sensor is under my absolute control.\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    scheduler = JarvisScheduler()
    scheduler.initiate_overlord_mode()
