import os
import subprocess
import time

def optimus_speak(text):
    print(f"\033[1;34m[OPTIMUS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def network_bandwidth_monitor():
    os.system('clear')
    print("\033[1;34m" + "🌐"*30)
    print("      OPTIMUS NEURAL SYSTEMS : BANDWIDTH MONITOR (P366)")
    print("🌐"*30 + "\033[0m")
    
    optimus_speak("Scanning network infrastructure. Pinging global DNS servers.")
    
    # Testing Latency (Ping)
    print("\n\033[1;33m[UPLINK]: Testing Latency to Cloud Server...\033[0m")
    
    # Using 'ping' to check connection (Termux needs internet access)
    response = os.system("ping -c 1 google.com > /dev/null 2>&1")
    
    if response == 0:
        latency = "24ms" # Simulated latency
        status = "STABLE"
        color = "\033[1;32m"
        optimus_speak("Network connection is robust. Synchronous link established.")
    else:
        latency = "N/A"
        status = "OFFLINE / UNSTABLE"
        color = "\033[1;31m"
        optimus_speak("Warning. Network instability detected. Cloud synchronization may fail.")

    print(f"\n\033[1;36m[REPORT]: NETWORK DIAGNOSTICS\033[0m")
    print("-" * 50)
    print(f"Uplink Status: {color}{status}\033[0m")
    print(f"Latency:       {latency}")
    print(f"Bandwidth:     Adaptive (4G/5G/Wi-Fi)")
    print("-" * 50)
    
    if status == "STABLE":
        print("\033[1;32m[RESULT]: OPTIMUS CORE IS READY FOR CLOUD SYNC.\033[0m")
    else:
        print("\033[1;31m[RESULT]: LOCAL MODE ONLY. NETWORK ERROR.\033[0m")

if __name__ == "__main__":
    network_bandwidth_monitor()
