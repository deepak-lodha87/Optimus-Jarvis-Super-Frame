import os
import time

def global_threat_monitor():
    print("\n" + "="*45)
    print("      JARVIS GLOBAL THREAT MONITOR")
    print("="*45)
    
    msg_init = "Commander Deepak, scanning global digital perimeter for risk factors."
    print(f"\n[JARVIS]: {msg_init}")
    os.system(f"termux-tts-speak '{msg_init}'")
    
    # संवेदनशील कीवर्ड्स की सूची
    risk_keywords = ["unauthorized", "data_leak", "vulnerability", "breach"]
    simulated_traffic = ["system_stable", "data_leak_detected", "update_available"]
    
    time.sleep(1.5)
    found_threats = []

    for packet in simulated_traffic:
        print(f"[SCANNING]: Analyzing packet data: {packet}...")
        time.sleep(0.8)
        if any(key in packet for key in risk_keywords):
            found_threats.append(packet)

    if found_threats:
        alert = f"Commander, {len(found_threats)} potential threat indicators identified!"
        print(f"\n[CRITICAL]: {alert}")
        os.system(f"termux-tts-speak '{alert}'")
        for threat in found_threats:
            print(f"  --> ALERT: Keyword match found in '{threat}'")
    else:
        success = "Digital perimeter is secure. No threat indicators found."
        print(f"\n[STATUS]: {success}")
        os.system(f"termux-tts-speak '{success}'")

    print("\n" + "="*45)

if __name__ == "__main__":
    global_threat_monitor()
