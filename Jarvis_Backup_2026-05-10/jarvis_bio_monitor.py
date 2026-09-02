import time, os, random

class JarvisBioGuard:
    def __init__(self):
        self.version = "1,000,000+ PHASES"
        self.user = "DEEPAK-PRIME"

    def monitor_vitals(self):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS BIO-MONITOR : PHASE 12 - STEP 2         \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        vitals = [
            ("Heart Rate (BPM)", f"{random.randint(70, 85)}", "NORMAL"),
            ("Stress Index", f"{random.randint(10, 30)}%", "LOW"),
            ("Neural Fatigue", "2%", "EXCELLENT"),
            ("Hydration Level", "85%", "OPTIMAL")
        ]
        
        for vital, value, status in vitals:
            print(f" \033[1;33m[SENSING]\033[0m {vital:20} : {value:6} | [\033[1;32m{status}\033[0m]")
            time.sleep(0.8)

        print(f"\n\033[1;32m[SYSTEM] Bio-Sync Active. Deepak-Prime is in peak condition.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I am now monitoring your \nbiological resonance. Your well-being is my \nhighest priority. If I detect any signs of \nfatigue or stress, I will automatically adjust \nour mission parameters. You take care of the \nvision, sir; I will take care of you.\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    guard = JarvisBioGuard()
    guard.monitor_vitals()
