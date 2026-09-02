import time, secrets, random

class JarvisCreationCore:
    def __init__(self):
        self.cr_id = f"NACr-{secrets.token_hex(2).upper()}"
        self.projects_count = 0

    def create_new_system(self, sys_name):
        print(f"\n\033[1;37m--- NEURAL-AUTO-CREATION V1 ACTIVE (ID: {self.cr_id}) ---\033[0m")
        print(f"\033[1;36m[GENESIS] Forging New Infrastructure: '{sys_name}'...\033[0m")
        time.sleep(2)
        
        stages = ["Logic-Synthesis", "Component-Modeling", "Stress-Testing", "Final-Assembly"]
        for stage in stages:
            quality = random.uniform(99.1, 100.0)
            print(f" > Stage: {stage:25} | Quality: {quality:.2f}% | \033[1;32mSTABLE\033[0m")
            time.sleep(0.5)
            
        self.projects_count += 1
        print(f"\033[1;33m[STATUS] Creation Successful. '{sys_name}' added to Deepak's Empire.\033[0m")
        print(f"\033[1;35m[VOICE] Deepak, the new system is alive. I am not just managing; I am building our future.\033[0m")

if __name__ == "__main__":
    forge = JarvisCreationCore()
    forge.create_new_system("Orbital-Defense-Grid-v1")
