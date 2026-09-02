import time
import random

class CyberWarfare:
    def __init__(self):
        self.threat_level = "LOW"
        self.defense_active = True

    def monitor_incoming_packets(self):
        print(f"\033[1;36m[WARFARE]\033[0m Scanning for unauthorized access attempts...")
        time.sleep(1.5)
        
        # Simulating a detected attack
        attack_detected = True 
        
        if attack_detected:
            print("\033[1;31m[!] ALERT: Brute-Force Attack Detected from IP: 192.168.x.x\033[0m")
            self.initiate_counter_strike()
        else:
            print("\033[1;32m[SAFE]\033[0m Network traffic is clean.")

    def initiate_counter_strike(self):
        print("\033[1;33m[ACTION]\033[0m Activating Honey-Pot. Diverting intruder...")
        time.sleep(1)
        print("\033[1;33m[ACTION]\033[0m Executing Trace-Back Ping. Identity acquired.")
        time.sleep(1)
        print("\033[1;32m[SUCCESS]\033[0m Intruder's system neutralized. Access denied.")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, an attempt was made to \nbreach our outer shell. I have successfully \nneutralized the threat and blacklisted the \nsource globally. We are untouchable.\033[0m")

if __name__ == "__main__":
    warfare = CyberWarfare()
    warfare.monitor_incoming_packets()
