import os
import time
import random

def firewall_guardian_protocol():
    print("\n" + "="*40)
    print("      JARVIS VIRTUAL FIREWALL GUARD")
    print("="*40)
    
    msg_init = "Commander Deepak, activating neural firewall layers..."
    print(f"\n[JARVIS]: {msg_init}")
    os.system(f"termux-tts-speak '{msg_init}'")
    
    time.sleep(1.5)
    
    # संदिग्ध गतिविधि का सिमुलेशन
    threat_ips = ["192.168.1.50", "10.0.0.99", "Unknown_External_Source"]
    detected_threat = random.choice(threat_ips)
    
    alert_msg = f"Alert! Unauthorized access attempt detected from source: {detected_threat}"
    print(f"\n[!!! WARNING !!!]: {alert_msg}")
    os.system(f"termux-tts-speak '{alert_msg}'")
    
    # काउंटर-मेजर (Counter-measure)
    print("\n[PROCESS]: Initiating protocol: Blacklist & Isolate.")
    time.sleep(2)
    
    success_msg = f"Threat neutralized. Source {detected_threat} has been permanently blocked by the Super-Frame."
    print(f"\n[SUCCESS]: {success_msg}")
    os.system(f"termux-tts-speak '{success_msg}'")
    
    print("\n" + "="*40)

if __name__ == "__main__":
    firewall_guardian_protocol()
