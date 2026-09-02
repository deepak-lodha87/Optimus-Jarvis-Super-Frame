import time
import os

class JarvisCommander:
    def __init__(self):
        self.threat_levels = {"LOW": 0, "MEDIUM": 1, "HIGH": 2, "CRITICAL": 3}
        self.current_threat = "CRITICAL" # Simulating a sudden threat

    def execute_defense(self):
        print(f"\033[1;31m[COMMANDER]\033[0m Threat Detected: {self.current_threat}")
        print("\033[1;33m[DECISION]\033[0m No time for manual confirmation. Initiating Auto-Defense.")
        time.sleep(1)

        if self.threat_levels[self.current_threat] >= 2:
            print(" \033[1;37m[ACTION 1]\033[0m Locking Gatekeeper Protocol...")
            time.sleep(0.8)
            print(" \033[1;37m[ACTION 2]\033[0m Encrypting User Directory...")
            time.sleep(0.8)
            print(" \033[1;37m[ACTION 3]\033[0m Cutting External Network Access...")
            time.sleep(1.2)
            
            print("\n\033[1;32m[STATUS]\033[0m Perimeter Secured. System is now in Black-Out Mode.")
        
        print(f"\n\033[1;35m[VOICE] Deepak... sir, the enemy was at the \ngate, but I have already locked the doors \nand armed the traps. I didn't wait for \nyour order because every second counts in \nwar. You are safe. The threat is \nneutralized.\033[0m")

if __name__ == "__main__":
    commander = JarvisCommander()
    commander.execute_defense()
