import time
import os

class EvidenceScrubber:
    def __init__(self):
        self.temp_logs = ["session_46.log", "cache_data.tmp", "trace_route.txt"]

    def scrub_system(self):
        print("\033[1;31m[CLEANER]\033[0m Session ending. Initiating Anti-Forensic Scrubbing...")
        time.sleep(1.5)
        
        for file in self.temp_logs:
            print(f" \033[1;37m[WIPING]\033[0m Overwriting {file} with random bits...")
            # Overwriting simulation
            time.sleep(0.5)
            print(f" \033[1;32m[DELETED]\033[0m {file} has been purged.")
        
        # Clearing Terminal Command History (Simulated)
        print(" \033[1;37m[SHREDDING]\033[0m Clearing Terminal Bash History...")
        time.sleep(1)
        
        print("\n\033[1;32m[STATUS]\033[0m Zero-Footprint achieved. System is clean.")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I have burned the map \nbehind us. No one can follow where we \nhave been or what we have done. Our \nsecrets are safe in the void. Mission \naccomplished.\033[0m")

if __name__ == "__main__":
    scrubber = EvidenceScrubber()
    scrubber.scrub_system()
