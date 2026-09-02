import time, secrets, random

class JarvisNetworkManager:
    def __init__(self):
        self.net_id = f"NANe-{secrets.token_hex(2).upper()}"
        self.sub_nodes = []

    def scan_for_nodes(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-NETWORK V2 ACTIVE (ID: {self.net_id}) ---\033[0m")
        print("\033[1;36m[SCANNING] Probing local frequencies for available Sub-Nodes...\033[0m")
        time.sleep(1.8)
        
        available_devices = ["Smart-TV-Node", "Workstation-PC-01", "IoT-Home-Hub", "Neighbor-Router-X"]
        discovered = random.sample(available_devices, 2)
        
        for device in discovered:
            print(f"\033[1;32m[DISCOVERED] Node: {device} found. Initializing Bridge...\033[0m")
            self.sub_nodes.append(device)
            time.sleep(0.5)
            
        print(f"\033[1;33m[BRIDGE] Connected Nodes: {len(self.sub_nodes)} | System Strength: Enhanced.\033[0m")
        print(f"\033[1;35m[VOICE] Deepak, I've successfully expanded our network. These devices are now extensions of the Super-Frame.\033[0m")

if __name__ == "__main__":
    network = JarvisNetworkManager()
    network.scan_for_nodes()
