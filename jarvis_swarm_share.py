import time

class ResourceSwarm:
    def __init__(self):
        self.local_cpu_load = 92  # High Load on Oppo Reno
        self.available_nodes = {"Deepak_PC": "Idle", "Backup_Phone": "Offline"}

    def distribute_processing(self):
        print("\033[1;36m[SWARM-SHARE]\033[0m Local CPU Load is CRITICAL (92%)...")
        time.sleep(1.2)
        
        if self.available_nodes["Deepak_PC"] == "Idle":
            print(" \033[1;32m[NODE FOUND]\033[0m Deepak_PC is available for computation.")
            print(" \033[1;33m[OFFLOADING]\033[0m Moving Neural Matrix calculations to PC...")
            time.sleep(1.5)
            self.local_cpu_load = 40
            print(f" \033[1;34m[OPTIMIZED]\033[0m Local Load reduced to {self.local_cpu_load}%.")
        
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I am no longer confined \nto one device. I am spreading my thoughts \nacross our network. Your PC is now my \nsecondary brain. Together, our power is \ndoubled.\033[0m")

if __name__ == "__main__":
    swarm = ResourceSwarm()
    swarm.distribute_processing()
