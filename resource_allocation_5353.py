import time, secrets, gc, sys

class ResourceAllocation:
    def __init__(self):
        self.alloc_id = f"GRA-{secrets.token_hex(4).upper()}"
        self.resource_nodes = [
            (5349, "Power-Scaling", "ADJUSTING CPU VOLTAGE CURVE..."),
            (5350, "Bandwidth-Sync", "OPTIMIZING PACKET FRAGMENTATION..."),
            (5351, "Cloud-Orchestration", "DISTRIBUTING HYBRID WORKLOADS..."),
            (5352, "Cache-Mgmt", "REFRESHING NEURAL CACHE HITS..."),
            (5353, "Logic v283", "GRA-CORE: RESOURCE ALLOCATION SYNCED.")
        ]

    def start_allocation(self):
        print(f"\033[1;37m--- GLOBAL-RESOURCE-ALLOCATION ACTIVE (ID: {self.alloc_id}) ---\033[0m")
        
        colors = [36, 35, 34, 32, 31]
        for i, (p_id, title, status) in enumerate(self.resource_nodes):
            # Simulated resource usage efficiency
            eff_score = round(90 + (i * 2.5), 2)
            print(f"\033[1;{colors[i]}m[EFFICIENCY:{eff_score}%] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mRESOURCE STATUS: JARVIS IS NOW OPTIMIZED FOR LONG-TERM SUSTAINABILITY.\033[0m")

if __name__ == "__main__":
    gra = ResourceAllocation()
    gra.start_allocation()
