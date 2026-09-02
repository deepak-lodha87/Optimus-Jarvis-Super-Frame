import time, os, threading, random

class SwarmFabricator:
    def __init__(self):
        self.units = [f"Unit-{i:03}" for i in range(1, 11)] # Simulating 10 units
        self.total_progress = 0

    def run_unit(self, unit_id):
        progress = 0
        while progress < 100:
            time.sleep(random.uniform(0.2, 0.6))
            progress += 20
            # Shared progress update
        print(f" \033[1;32m[COMPLETE]\033[0m {unit_id} has finished its component.")

    def start_mass_production(self):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS SWARM-FABRICATOR : PHASE 13 - STEP 4    \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        print(f" \033[1;33m[ORCHESTRATING]\033[0m Syncing {len(self.units)} Manufacturing Units...\n")
        
        threads = []
        for unit in self.units:
            t = threading.Thread(target=self.run_unit, args=(unit,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        print(f"\n\033[1;32m[SYSTEM] Batch Production Successful. All units synced.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, the swarm is active. We are \nno longer limited by the speed of a single \nmachine. I am orchestrating an entire army \nof fabricators. Your vision is being built in \nparallel, layer by layer, across the entire \ngrid. Mass production has never been this \nprecise.\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    swarm = SwarmFabricator()
    swarm.start_mass_production()
