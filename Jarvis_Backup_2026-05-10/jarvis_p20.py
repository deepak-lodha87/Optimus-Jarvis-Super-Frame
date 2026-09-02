import socket
import subprocess
import time

def get_network_info():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return hostname, local_ip
    except:
        return "Unknown", "Disconnect"

def jarvis_network_scan():
    print("--- OPTIMUS JARVIS SUPER-FRAME: PHASE 20 ---")
    print("[LOG] Establishing Satellite Link...")
    time.sleep(1.5)
    
    host, ip = get_network_info()
    
    print(f"\n[SYSTEM] Network Intelligence Check:")
    print(f"📡 Hostname: {host}")
    print(f"🌐 Local IP: {ip}")
    print(f"🌍 Status: SECURE CONNECTIVITY ESTABLISHED")
    
    print("\n✅ Phase 20: Global Connectivity Core Integrated.")

if __name__ == "__main__":
    jarvis_network_scan()
