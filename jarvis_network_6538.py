import time, secrets, random

class JarvisNetworkHub:
    def __init__(self):
        self.net_id = f"NAN-{secrets.token_hex(2).upper()}"
        self.connected_nodes = []

    def scan_for_devices(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-NETWORK V3 ACTIVE (ID: {self.net_id}) ---\033[0m")
        print("\033[1;36m[SCANNING] Pinging nearby smart devices via Bluetooth/Wi-Fi...\033[0m")
        time.sleep(1.5)
        
        available = ["Smart-TV", "Brother's-Phone", "Smart-Bulb", "Laptop-Node"]
        found = random.sample(available, 2)
        
        for device in found:
            print(f"\033[1;32m[FOUND] Device detected: {device} | Signal Strength: Strong\033[0m")
            self.connected_nodes.append(device)
            time.sleep(0.5)
            
        print(f"\033[1;33m[SYNC] Establishing Secure Bridge with {len(self.connected_nodes)} nodes...\033[0m")
        time.sleep(1)
        print(f"\033[1;35m[VOICE] Deepak, the network is expanding. I can now interface with the {found[0]} if required.\033[0m")

if __name__ == "__main__":
    hub = JarvisNetworkHub()
    hub.scan_for_devices()
