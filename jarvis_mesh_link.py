import time

class MeshNetwork:
    def __init__(self):
        self.connected_devices = []
        self.host_device = "Oppo Reno 12 Pro"

    def deploy_to_node(self, device_name):
        print(f"\033[1;36m[MESH-LINK]\033[0m Pinging {device_name}...")
        time.sleep(1.5)
        
        print(f" \033[1;32m[CONNECTED]\033[0m Handshake successful with {device_name}.")
        self.connected_devices.append(device_name)
        
        print(f" \033[1;34m[SYNC]\033[0m Transferring Jarvis Core v101.1 to {device_name}...")
        time.sleep(1)
        
    def show_status(self):
        print(f"\n\033[1;33m[NETWORK STATUS]\033[0m Active Nodes: {len(self.connected_devices)}")
        for device in self.connected_devices:
            print(f"  - {device}: ONLINE")
            
        print(f"\n\033[1;35m[VOICE] Deepak sir, I have expanded my presence. \nI am no longer confined to one device. I am \neverywhere you are, ready to assist you on \nany platform instantly.\033[0m")

if __name__ == "__main__":
    mesh = MeshNetwork()
    mesh.deploy_to_node("Smart Bike Interface")
    mesh.deploy_to_node("Work Station Laptop")
    mesh.show_status()
