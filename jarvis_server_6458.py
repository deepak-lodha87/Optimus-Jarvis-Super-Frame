import secrets, time

class JarvisNetwork:
    def __init__(self):
        self.server_id = f"NAN-{secrets.token_hex(2).upper()}"
        self.local_ip = "192.168.1.100 (Simulated)"

    def start_private_server(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-NETWORK V2 ACTIVE (ID: {self.server_id}) ---\033[0m")
        print(f"\033[1;36m[HOSTING] Creating Private Command Tunnel on {self.local_ip}...\033[0m")
        time.sleep(1.5)
        
        print("\033[1;32m[STATUS] Private Server is LIVE. Devices in Ratlam Mesh can now connect.\033[0m")
        self.broadcast_signal()

    def broadcast_signal(self):
        print("\033[1;33m[SIGNAL] Sending Encrypted Handshake to Trusted Nodes...\033[0m")
        time.sleep(1)
        print("\033[1;35m[VOICE] Deepak, the command server is ready. You can now control me from any local device.\033[0m")

if __name__ == "__main__":
    nan = JarvisNetwork()
    nan.start_private_server()
