import os
import threading
import time

class TaskSpawner:
    def __init__(self):
        self.master = "Deepak"

    def background_service(self, service_name):
        print(f"\033[1;32m[SPAWNED]:\033[0m {service_name} is now running in the shadow.")
        time.sleep(2)
        print(f"\033[1;36m[STATUS]:\033[0m {service_name} completed successfully.")

    def launch_all(self):
        print(f"\n\033[1;35m[CORE TASK SPAWNER]\033[0m Initiating parallel protocols...")
        os.system('termux-tts-speak "Deepak sir, spawning multiple background threads to optimize the super-frame."')
        
        services = ["Vitals Check", "Security Scan", "Encryption Sync"]
        threads = []

        for service in services:
            t = threading.Thread(target=self.background_service, args=(service,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

if __name__ == "__main__":
    spawner = TaskSpawner()
    spawner.launch_all()
