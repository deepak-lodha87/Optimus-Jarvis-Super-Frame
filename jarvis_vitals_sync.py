import time, os, random

class BioMetricSync:
    def __init__(self):
        self.user = "Deepak-Prime"
        self.vitals = {"Focus": 85, "Energy": 70, "Stress": 20}

    def monitor_vitals(self):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS BIO-SYNC : PHASE 15 - STEP 5            \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        print("\033[1;33m[SYNCING]\033[0m Accessing device bio-sensors...")
        time.sleep(1.5)
        
        for metric, value in self.vitals.items():
            bar = "█" * (value // 10)
            print(f" \033[1;37m{metric:10}\033[0m: [{bar:10}] {value}%")
            time.sleep(0.5)

        print(f"\n\033[1;32m[ANALYSIS] Physical state is Optimal for Phase 16.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I am monitoring your vitals \nin real-time. Your focus levels are peaking, \nmaking this the perfect time for complex \nintegration. However, I noticed a slight rise \nin eye-strain patterns. I've adjusted the \nscreen's color temperature. Your health is the \nfoundation of our empire.\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    sync = BioMetricSync()
    sync.monitor_vitals()
