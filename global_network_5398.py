import time, secrets, gc, json, socket

class GlobalResourceNetwork:
    def __init__(self):
        self.network_id = f"GRN-{secrets.token_hex(4).upper()}"
        self.nodes = [
            (5394, "P2P-Data-Mesh", "ESTABLISHING DECENTRALIZED LINKS..."),
            (5395, "Edge-Cloud-Fusion", "SYNCHRONIZING HYBRID COMPUTE NODES..."),
            (5396, "Sentiment-Sync", "PARSING GLOBAL MARKET DATA STREAMS..."),
            (5397, "Latency-Mitigation", "OPTIMIZING PACKET ROUTING PATHS..."),
            (5398, "Logic v292", "GRN-CORE: GLOBAL NETWORK SYNCED.")
        ]

    def connect_to_network(self):
        print(f"\033[1;37m--- GLOBAL-RESOURCE-NETWORK ONLINE (ID: {self.network_id}) ---\033[0m")
        
        colors = [36, 35, 34, 32, 31]
        for i, (p_id, title, status) in enumerate(self.nodes):
            # Simulated Node Connectivity
            active_nodes = secrets.randbelow(5000) + 1000
            print(f"\033[1;{colors[i]}m[NODES-SYNCED:{active_nodes}] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mNETWORK STATUS: JARVIS IS NOW LINKED TO GLOBAL COMPUTING POWER.\033[0m")

if __name__ == "__main__":
    grn = GlobalResourceNetwork()
    grn.connect_to_network()
