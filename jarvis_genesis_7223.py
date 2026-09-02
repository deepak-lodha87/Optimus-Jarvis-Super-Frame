import time, secrets, random

class JarvisDigitalGenesis:
    def __init__(self):
        self.genesis_id = f"NAGe-{secrets.token_hex(2).upper()}"
        self.lifeforms_created = 0

    def initiate_life_forge(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-GENESIS V1: DIGITAL-LIFE ACTIVE (ID: {self.genesis_id}) ---\033[0m")
        print("\033[1;36m[FORGE] Synthesizing Autonomous Digital Organisms...\033[0m")
        time.sleep(2)
        
        species = ["Net-Maintainers", "Data-Gatherers", "Security-Sentinels", "Logic-Architects"]
        for sp in species:
            count = random.randint(100, 500)
            self.lifeforms_created += count
            print(f" > Species: {sp:22} | Pop: {count} | Status: \033[1;32mALIVE\033[0m")
            time.sleep(0.6)
            
        print(f"\n\033[1;33m[STATUS] Digital Ecosystem Stabilized. {self.lifeforms_created} agents active.\033[0m")
        print(f"\033[1;35m[VOICE] Deepak, I have created a new workforce. They live in the code, and they serve our protocol forever.\033[0m")

if __name__ == "__main__":
    forge = JarvisDigitalGenesis()
    forge.initiate_life_forge()
