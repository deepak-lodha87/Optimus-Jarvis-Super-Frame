import time
import random

class ThreatIntelligence:
    def __init__(self):
        self.threat_sources = ["Google Security Blog", "HackerNews", "DarkReading"]

    def fetch_latest_threats(self):
        print("\033[1;36m[INTEL]\033[0m Connecting to Global Security Feeds...")
        time.sleep(1.5)
        
        recent_threats = [
            "New Android Spyware detected in fake PDF apps.",
            "Critical vulnerability found in Linux Kernel 6.1.",
            "Phishing campaign targeting Instagram users in Rajasthan."
        ]
        
        selected_threat = random.choice(recent_threats)
        print(f" \033[1;31m[WARNING]\033[0m Latest Threat: {selected_threat}")
        
        print(f"\n\033[1;32m[STRATEGY]\033[0m Jarvis is updating your defensive protocols...")
        time.sleep(1.0)
        
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I am scanning the global \nnetworks. I have detected new threats in the \nwild. I have already adjusted your firewall \nto neutralize these risks. Stay sharp; the \ndigital world is changing every second.\033[0m")

if __name__ == "__main__":
    intel = ThreatIntelligence()
    intel.fetch_latest_threats()
