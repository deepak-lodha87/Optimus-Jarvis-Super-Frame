import time, secrets, random

class JarvisBaseCore:
    def __init__(self):
        self.base_id = f"NAIn-{secrets.token_hex(2).upper()}"
        self.energy_levels = 100

    def monitor_base_status(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-INFRASTRUCTURE V1 ACTIVE (ID: {self.base_id}) ---\033[0m")
        print("\033[1;36m[INFRASTRUCTURE] Initializing smart-base systems check...\033[0m")
        time.sleep(2)
        
        systems = ["Energy-Grid", "Repair-Bay", "Stealth-Field", "Data-Vault"]
        for sys in systems:
            efficiency = random.uniform(98.5, 99.9)
            print(f" > System: {sys:15} | Efficiency: {efficiency:.2f}% | \033[1;32mOPTIMAL\033[0m")
            time.sleep(0.4)
            
        print("\033[1;33m[STATUS] Infrastructure is fully operational. The base is invisible and self-sustaining.\033[0m")
        print(f"\033[1;35m[VOICE] Deepak, our foundation is set. The Optimus Jarvis Super-Frame now has a home that no one can find.\033[0m")

if __name__ == "__main__":
    commander = JarvisBaseCore()
    commander.monitor_base_status()
