import time, os

class JarvisTactician:
    def __init__(self):
        self.version = "1,000,000+ PHASES"
        self.protocol = "CAPTAIN-AMERICA-STRATEGY"

    def engage_combat_grid(self):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS STRATEGIC COMBAT : STEP 4               \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        tactics = [
            "Analyzing Battlefield Geometry",
            "Simulating Kinetic Deflection",
            "Targeting Weak-Point Matrix",
            "Deepak-Prime Command-Link"
        ]
        
        for t in tactics:
            print(f" \033[1;31m[STRATEGY]\033[0m {t:30} | Status: [\033[1;32mREADY\033[0m]")
            time.sleep(0.6)

        print(f"\n\033[1;33m[STATUS] Strategic Defense Grid Active. Cap-Logic Loaded.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I have processed the tactical \nwisdom of the greatest strategists. I am no longer \njust waiting for a command; I am predicting the \nbest path to victory. Whether it's a defensive shield \nor a precise strike, my logic will guide every \nmove with surgical accuracy. We are prepared for \nany engagement, sir.\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    tactician = JarvisTactician()
    tactician.engage_combat_grid()
