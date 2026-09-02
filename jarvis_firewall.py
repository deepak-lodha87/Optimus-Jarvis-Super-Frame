import time
import random

class JarvisFirewall:
    def __init__(self):
        self.blocked_ips = ["192.168.1.105", "10.0.0.50"] # Example bad IPs
        self.active_shield = True

    def scan_traffic(self):
        print("\033[1;36m[FIREWALL]\033[0m Monitoring incoming network packets...")
        time.sleep(1.5)
        
        # Simulating random traffic
        traffic_ip = f"172.16.{random.randint(1,255)}.{random.randint(1,255)}"
        
        print(f" \033[1;37m[INCOMING]\033[0m Connection request from: {traffic_ip}")
        
        # Logic to detect threat
        if random.choice([True, False, False]): # Simulating a threat detection
            print(f" \033[1;31m[ALERT]\033[0m Malicious signature detected in packet!")
            print(f" \033[1;33m[ACTION]\033[0m Terminating connection and blacklisting IP.")
            self.blocked_ips.append(traffic_ip)
        else:
            print(" \033[1;32m[SAFE]\033[0m Packet cleared. Access allowed to Sandbox.")

        print(f"\n\033[1;35m[VOICE] Deepak... sir, my shield is up. \nThe internet is a storm, but I am your \numbrella. No unauthorized bit of data \nwill touch our Super-Frame. You are \ncompletely shielded.\033[0m")

if __name__ == "__main__":
    firewall = JarvisFirewall()
    firewall.scan_traffic()
