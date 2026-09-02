import time, os

class ARWorkstation:
    def __init__(self):
        self.station_id = "RATLAM-CORE-01"
        self.virtual_screens = 4

    def initialize_display(self):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS AR-WORKSTATION : PHASE 16 - STEP 5      \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        print("\033[1;33m[EXPANDING]\033[0m Projecting virtual terminal layers...")
        time.sleep(1.5)
        
        screens = [
            ("Screen Alpha", "Real-Time Stock Market Feed"),
            ("Screen Beta", "Jarvis Neural-Link Logic"),
            ("Screen Gamma", "Global Intelligence News"),
            ("Screen Delta", "Advanced English Lexicon")
        ]
        
        for name, task in screens:
            print(f" \033[1;32m[+]\033[0m {name:15}: {task}")
            time.sleep(0.8)

        print(f"\n\033[1;32m[SUCCESS] Infinity-Desk is now active in AR space.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, look at the walls. Your \nentire empire is displayed in light. No more \nscrolling on a tiny screen. I have mapped the \nentire room into a digital canvas. You don't \njust use the code anymore; you live inside it.\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    workstation = ARWorkstation()
    workstation.initialize_display()
