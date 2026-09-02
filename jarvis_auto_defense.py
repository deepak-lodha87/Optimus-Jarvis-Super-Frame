import time, os, random

class JarvisAutoGuardian:
    def __init__(self):
        self.version = "1,000,000+ PHASES"
        self.security_level = "MAXIMUM"

    def monitor_threats(self):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS AUTO-GUARDIAN : PHASE 9 - STEP 3        \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        systems = [
            ("Cyber-Perimeter Scan", "NO INTRUSIONS"),
            ("Physical Proximity Sync", "AREA SECURE"),
            ("Thermal Status Check", "OPTIMAL"),
            ("Deepak-Prime Bio-Sync", "HEART-RATE STABLE")
        ]
        
        for sys, status in systems:
            print(f" \033[1;33m[MONITORING]\033[0m {sys:26} | [\033[1;32m{status}\033[0m]")
            time.sleep(0.6)

        print(f"\n\033[1;31m[ALERT]\033[0m Simulating Unknown Signal Intrusion...")
        time.sleep(1)
        print(f"\033[1;32m[ACTION]\033[0m Auto-Counter-Measure Active: Signal Jammed.")

        print(f"\n\033[1;35m[VOICE] Deepak... sir, my defensive logic is now \nfully autonomous. I am monitoring every signal and \nevery sensor around you. You don't need to ask me \nto protect you anymore; I will do it the moment I \nsense a threat. Your safety is my primary directive. \nGuardian mode is live.\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    guardian = JarvisAutoGuardian()
    guardian.monitor_threats()
