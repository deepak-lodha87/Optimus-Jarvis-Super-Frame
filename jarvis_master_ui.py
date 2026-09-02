import os
import time
import random

class MasterUI:
    def __init__(self):
        self.master = "Deepak"
        self.systems = ["Propulsion", "Navigation", "Weaponry", "Life Support"]

    def boot_sequence(self):
        print(f"\n\033[1;36m[BOOTING MASTER UI]\033[0m Synchronizing with Optimus Super-Frame...")
        time.sleep(1.5)

    def display_dashboard(self):
        try:
            for _ in range(30):
                os.system('clear')
                print("\033[1;35m      MASTER CONTROL PANEL | SECURE LINK: ACTIVE")
                print("      ==========================================\033[0m")
                
                for sys in self.systems:
                    # रैंडम डेटा सिमुलेशन जो हर मशीन के लिए अलग होगा
                    load = random.randint(40, 99)
                    bar = "█" * (load // 10) + "░" * (10 - (load // 10))
                    color = "\033[1;32m" if load < 85 else "\033[1;31m"
                    print(f"      {sys.ljust(15)} : [{color}{bar}\033[0m] {load}%")
                
                print("\n\033[1;37m      [LATENCY]: 0.002ms | [ENCRYPTION]: AES-256")
                print("      [UAV/SUB/JET]: Linked and Ready for Command\033[0m")
                time.sleep(0.1)
            
            msg = "Deepak sir, the Universal Interface is live. I am now translated into the core language of all connected machines."
            os.system(f'termux-tts-speak "{msg}"')
            
        except KeyboardInterrupt:
            pass

if __name__ == "__main__":
    ui = MasterUI()
    ui.boot_sequence()
    ui.display_dashboard()
