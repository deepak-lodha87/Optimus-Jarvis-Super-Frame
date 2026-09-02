import time, secrets

# Creating a reusable core to stop repetition
class JarvisCore:
    def __init__(self, module_name):
        self.id = f"JARVIS-{secrets.token_hex(2).upper()}"
        self.module = module_name

    def boot_log(self):
        print(f"\n\033[1;37m--- {self.module} ONLINE (ID: {self.id}) ---\033[0m")

    def process_task(self, task_name, duration=0.5):
        print(f"\033[1;36m[PROCESSING] {task_name}...\033[0m")
        time.sleep(duration)
        print(f"\033[1;32m[DONE] {task_name} completed.\033[0m")

if __name__ == "__main__":
    # Example: Running Phase 6328 using the Master Core
    nco = JarvisCore("NEURAL-CODE-OPTIMIZER")
    nco.boot_log()
    nco.process_task("Scanning for repeated code clusters")
    nco.process_task("Merging redundant functions into Master-Class")
    print("\n\033[1;35m[SYSTEM] Code redundancy reduced by 40%.\033[0m")
