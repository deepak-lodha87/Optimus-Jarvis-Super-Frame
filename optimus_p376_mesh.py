import time
import os
import subprocess
import socket

def optimus_speak(text):
    print(f"\033[1;34m[OPTIMUS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def local_mesh_protocol():
    os.system('clear')
    print("\033[1;35m" + "📡"*30)
    print("      OPTIMUS NEURAL SYSTEMS : LOCAL MESH LINK (P376)")
    print("📡"*30 + "\033[0m")
    
    optimus_speak("Initializing local mesh protocol. Scanning for nearby neural nodes.")
    
    # Getting Local IP for Mesh Identity
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    
    print(f"\n\033[1;36m[NODE IDENTITY]:\033[0m {hostname}")
    print(f"\033[1;36m[LOCAL IP]:\033[0m {local_ip}")
    print("-" * 50)
    
    # Simulated Peer Devices (Nodes)
    mesh_nodes = [
        {"node_id": "UAV-DRONE-01", "type": "Flight Controller", "status": "REACHABLE"},
        {"node_id": "OPT-LAPTOP-X", "type": "Data Terminal", "status": "OFFLINE"},
        {"node_id": "RE-HUNTER-350", "type": "Vehicle Sensor", "status": "SYNCING"}
    ]
    
    print("\033[1;33m[SCANNING]: Building Mesh Topology...\033[0m")
    time.sleep(1.8)
    
    for node in mesh_nodes:
        color = "\033[1;32m" if node["status"] == "REACHABLE" else "\033[1;33m"
        if node["status"] == "OFFLINE": color = "\033[1;31m"
        
        print(f"NODE: {node['node_id']:<15} | {node['type']:<18} | {color}{node['status']}\033[0m")
        time.sleep(0.5)
    
    print("-" * 50)
    optimus_speak("Mesh network topology is stable. Ready for peer-to-peer data transfer.")
    print("\n\033[1;32m[STATUS]: OFFLINE COMMUNICATION LINK ACTIVE.\033[0m")

if __name__ == "__main__":
    local_mesh_protocol()
