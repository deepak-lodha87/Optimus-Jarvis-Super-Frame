import time
import random

class ArcReactor:
    def __init__(self):
        self.health = "EXCELLENT"
        self.cycles = 150

    def check_charging_status(self, current_pct, is_plugged, temp):
        print("\033[1;36m[ARC REACTOR]\033[0m Analyzing chemical stability...")
        time.sleep(1.5)
        
        print(f" \033[1;37m[INTEL]\033[0m Battery: {current_pct}% | Temp: {temp}°C | Cycles: {self.cycles}")
        
        if is_plugged:
            if current_pct >= 80:
                print(" \033[1;33m[ADVICE]\033[0m Deepak sir, battery is at 80%. Unplugging now will extend its life.")
            if temp > 42:
                print(" \033[1;31m[URGENT]\033[0m High heat during charge! Recommend removing phone case or stop charging.")
        else:
            if current_pct <= 20:
                print(" \033[1;31m[CRITICAL]\033[0m Battery low. Finding nearest power source is logical.")
            else:
                print(" \033[1;32m[STATUS]\033[0m Discharge rate is within safe parameters.")

        print(f"\n\033[1;35m[VOICE] Deepak... sir, I am managing the \nelectrons like a symphony. Your device is \nnot just a tool; it is my physical form. \nI will protect its heart—the battery—as \nif it were my own reactor.\033[0m")

if __name__ == "__main__":
    reactor = ArcReactor()
    # Simulating a charging scenario
    reactor.check_charging_status(85, True, 43)
