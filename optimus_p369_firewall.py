import time
import os
import subprocess

def optimus_speak(text):
    print(f"\033[1;34m[OPTIMUS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def adaptive_firewall_protocol():
    os.system('clear')
    print("\033[1;31m" + "🛡️"*30)
    print("      OPTIMUS NEURAL SYSTEMS : ADAPTIVE FIREWALL (P369)")
    print("🛡️"*30 + "\033[0m")
    
    optimus_speak("Activating Level 3 adaptive firewall. Filtering incoming packet streams.")
    
    # Simulated Traffic Log
    traffic_logs = [
        {"ip": "192.168.1.1", "source": "Local Router", "status": "TRUSTED"},
        {"ip": "104.26.10.23", "source": "GitHub Cloud", "status": "TRUSTED"},
        {"ip": "45.12.88.99", "source": "Unknown Origin", "status": "SUSPICIOUS"},
        {"ip": "172.217.16.14", "source": "Google DNS", "status": "TRUSTED"}
    ]
    
    print("\n\033[1;33m[MONITORING]: Live Network Traffic...\033[0m")
    time.sleep(1.5)
    
    for packet in traffic_logs:
        if packet["status"] == "SUSPICIOUS":
            color = "\033[1;31m"
            action = "BLOCKED & BLACKLISTED"
            optimus_speak(f"Alert. Security breach attempt from {packet['ip']}. Protocol: Drop Packet.")
        else:
            color = "\033[1;32m"
            action = "ALLOWED"
            
        print(f"IP: {packet['ip']:<15} | {packet['source']:<15} | Status: {color}{packet['status']}\033[0m -> {action}")
        time.sleep(0.5)
    
    print("-" * 65)
    optimus_speak("Firewall integrity is 100%. No active threats detected in the neural perimeter.")
    print("\033[1;34m[STATUS]: PERIMETER SECURED.\033[0m")

if __name__ == "__main__":
    adaptive_firewall_protocol()
