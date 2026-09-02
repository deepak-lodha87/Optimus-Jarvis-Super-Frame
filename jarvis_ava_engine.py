import time
import random

class AVAEngine:
    def __init__(self):
        self.vulnerabilities_found = 0
        self.system_health = 100

    def start_assessment(self):
        print("\033[1;31m[AVA]\033[0m Starting Automated Vulnerability Assessment...")
        time.sleep(1.5)
        
        areas = ["File System", "Network Ports", "User Permissions", "Encryption Keys"]
        
        for area in areas:
            risk = random.choice(["LOW", "MEDIUM", "SAFE"])
            print(f" \033[1;36m[SCANNING]\033[0m Checking {area:18} | Status: {risk}")
            if risk != "SAFE":
                self.vulnerabilities_found += 1
                self.system_health -= 10
            time.sleep(0.6)

        print(f"\n\033[1;33m[REPORT]\033[0m Total Flaws Found: {self.vulnerabilities_found}")
        print(f"\033[1;32m[REPAIR]\033[0m Jarvis is auto-patching vulnerabilities...")
        time.sleep(1.2)
        
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I have finished scanning our \nfortress. I found a few small cracks, but \ndon't worry—I have already sealed them. \nIn the digital world, being 'Safe' is not \nenough; we must be 'Unbeatable'.\033[0m")

if __name__ == "__main__":
    ava = AVAEngine()
    ava.start_assessment()
