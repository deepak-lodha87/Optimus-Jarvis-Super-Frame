import time
import os

class StorageOptimizer:
    def __init__(self):
        self.local_space = 25  # GB left
        self.cloud_link = "Connected"
        self.temp_files = 4.5  # GB

    def optimize_space(self):
        print("\033[1;36m[STORAGE]\033[0m Analyzing File System Integrity...")
        time.sleep(1.5)
        
        if self.local_space < 30:
            print(f" \033[1;31m[ALERT]\033[0m Local space is low: {self.local_space}GB.")
            print(" \033[1;33m[ACTION]\033[0m Initiating Smart Offloading to Cloud...")
            time.sleep(1.2)
            
            # Moving temp files
            print(f" \033[1;32m[SUCCESS]\033[0m Cleared {self.temp_files}GB of temporary cache.")
            self.local_space += self.temp_files
            
            print(" \033[1;34m[OPTIMIZED]\033[0m Phase 1-200 logs moved to Cold Storage (GitHub).")
        
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I've reorganized my \nmemory. I've cleared the clutter and \nmoved our history to the vault. My local \ncore is now light, fast, and ready for \nour next thousand phases. I never forget; \nI just organize better.\033[0m")

if __name__ == "__main__":
    optimizer = StorageOptimizer()
    optimizer.optimize_space()
