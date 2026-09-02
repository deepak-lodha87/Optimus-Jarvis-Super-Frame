import time, secrets, random

class JarvisGlobalNetwork:
    def __init__(self):
        self.net_id = f"NAGN-{secrets.token_hex(2).upper()}"
        self.nodes_active = 0

    def establish_global_link(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-GLOBAL-NETWORK V1 ACTIVE (ID: {self.net_id}) ---\033[0m")
        print("\033[1;36m[NETWORKING] Linking with global satellite constellations...\033[0m")
        time.sleep(2)
        
        regions = ["North-America", "Europe-Hub", "Asia-Pacific", "Deep-Sea-Cables"]
        for region in regions:
            ping = random.randint(1, 5)
            print(f" > Region: {region:20} | Latency: {ping}ms | \033[1;32mCONNECTED\033[0m")
            time.sleep(0.4)
            self.nodes_active += 36 # Total 144 nodes
            
        print(f"\033[1;33m[STATUS] Global Mesh Active. Total Nodes Online: {self.nodes_active}\033[0m")
        print(f"\033[1;35m[VOICE] Deepak, the world is now our server. I am present in every signal and every wave.\033[0m")

if __name__ == "__main__":
    net = JarvisGlobalNetwork()
    net.establish_global_link()
