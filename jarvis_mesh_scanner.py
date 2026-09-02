import os
import socket

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def scan_network():
    base_ip = ".".join(get_local_ip().split(".")[:-1]) + "."
    print(f"\033[1;36m[SCANNING]\033[0m Searching for devices on {base_ip}0/24...")
    
    for i in range(1, 255):
        ip = base_ip + str(i)
        # Mobile hardware level ping
        response = os.system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1")
        if response == 0:
            print(f"\033[1;32m[FOUND]\033[0m Active Device at: {ip}")

if __name__ == "__main__":
    scan_network()
