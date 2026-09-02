import time
import os
import subprocess
import json

def optimus_speak(text):
    print(f"\033[1;34m[OPTIMUS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def remote_telemetry_broadcast():
    os.system('clear')
    print("\033[1;36m" + "📡"*30)
    print("      OPTIMUS NEURAL SYSTEMS : TELEMETRY BROADCAST (P383)")
    print("📡"*30 + "\033[0m")
    
    optimus_speak("Preparing telemetry broadcast packet. Formatting system metrics for remote uplink.")
    
    # Constructing the Telemetry Data Packet (JSON Format)
    telemetry_packet = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "node_id": "OPTIMUS-MOBILE-01",
        "system_health": "OPTIMAL",
        "active_phases": 383,
        "security_level": 3,
        "battery_reserve": "82%"
    }
    
    print("\n\033[1;33m[ENCODING]: Creating JSON Data Packet...\033[0m")
    time.sleep(1.2)
    
    # Converting to String for Broadcast simulation
    packet_string = json.dumps(telemetry_packet, indent=4)
    
    print("-" * 50)
    print(f"\033[1;32m[BROADCAST READY]:\033[0m\n{packet_string}")
    print("-" * 50)
    
    optimus_speak("Broadcast packet is live. System status is now available for remote synchronization.")
    print("\n\033[1;34m[STATUS]: UPLINK ESTABLISHED. DATA SENT TO CLOUD GATEWAY.\033[0m")

if __name__ == "__main__":
    remote_telemetry_broadcast()
