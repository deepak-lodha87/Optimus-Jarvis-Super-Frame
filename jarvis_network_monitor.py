import time
import random

class NetSentry:
    def __init__(self):
        self.blocked_ips = ["192.168.1.105", "45.77.12.33"] # Simulated bad IPs
        self.active_connections = 5

    def scan_traffic(self):
        print("\033[1;36m[SCANNING]\033[0m Monitoring active network packets...")
        time.sleep(1.5)
        
        # Simulating a packet check
        incoming_ip = f"104.21.14.{random.randint(1, 255)}"
        print(f" \033[1;37m[INCOMING]\033[0m Packet from: {incoming_ip}")
        
        if incoming_ip in self.blocked_ips:
            print(f" \033[1;31m[ALERT]\033[0m Malicious IP detected! Blocking connection...")
        else:
            print(f" \033[1;32m[SECURE]\033[0m Traffic verified. Connection is safe.")

        print(f"\n\033[1;35m[VOICE] Deepak... sir, I am now watching the \ndigital borders of your device. No packet \nmoves without my permission. Your network \nis no longer a playground for others; it's \na fortress. We are invisible to the noise.\033[0m")

if __name__ == "__main__":
    sentry = NetSentry()
    sentry.scan_traffic()
