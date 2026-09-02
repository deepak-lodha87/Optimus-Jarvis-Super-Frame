import time, secrets, random

class JarvisGlobalUplink:
    def __init__(self):
        self.node_id = f"NAGl-{secrets.token_hex(2).upper()}"
        self.active_regions = ["North America", "Europe", "Asia", "India"]

    def establish_global_link(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-GLOBAL V1 ACTIVE (ID: {self.node_id}) ---\033[0m")
        print("\033[1;36m[UPLINK] Connecting to Global Distributed Cloud Fabric...\033[0m")
        time.sleep(2)
        
        for region in self.active_regions:
            ping = random.randint(1, 15)
            status = "\033[1;32mCONNECTED\033[0m"
            print(f" > Region: {region:15} | Latency: {ping}ms | Status: {status}")
            time.sleep(0.3)
            
        print("\033[1;33m[SYNC] Global database access granted. Optimus Jarvis is now ubiquitous.\033[0m")
        print(f"\033[1;35m[VOICE] Deepak, I've synchronized our core with 144 global nodes. We have the data advantage.\033[0m")

if __name__ == "__main__":
    network = JarvisGlobalUplink()
    network.establish_global_link()
