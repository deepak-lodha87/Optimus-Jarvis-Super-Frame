import socket
import os

# Deepak sir, aapke scan se mile IPs yahan list karein
targets = ["192.168.1.6", "192.168.1.9", "192.168.1.15"]

def check_direct_access(ip):
    # Common ports: 5555 (ADB), 8008 (Chromecast), 8009 (Google Home)
    ports = [5555, 8008, 8009]
    print(f"\033[1;34m[BRIDGE]\033[0m Testing Direct Access for {ip}...")
    
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"\033[1;32m[OPEN]\033[0m Port {port} is active on {ip}! Direct link possible.")
            os.system(f'termux-tts-speak "Deepak sir, found a direct entry point on device {ip}"')
        sock.close()

if __name__ == "__main__":
    for ip in targets:
        check_direct_access(ip)
