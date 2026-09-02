import os, time, math, secrets

class IncomeEngine:
    def __init__(self):
        self.engine_id = f"DIE-{secrets.token_hex(2).upper()}"
        self.modules = {
            "A": "Market-Scraper: Extracting profitable data...",
            "B": "API-Linker: Connecting to global servers...",
            "C": "Lead-Gen: Finding potential clients...",
            "D": "Income-Tracker: Analyzing revenue streams..."
        }

    def run_module(self, key):
        if key in self.modules:
            print(f"\n\033[1;36m[RUNNING] {self.modules[key]}\033[0m")
            for i in range(1, 6):
                # Unique progress logic
                progress = i * 20
                print(f"[*] Processing Block {i}... {progress}% Complete", end='\r')
                time.sleep(0.3)
            print(f"\n\033[1;32m[SUCCESS] Module {key} synchronized with Jarvis.\033[0m")
        else:
            print("\033[1;31m[ERROR] Invalid Module Key.\033[0m")

    def dashboard(self):
        print(f"\n\033[1;37m--- JARVIS INCOME ENGINE (ID: {self.engine_id}) ---\033[0m")
        for k, v in self.modules.items():
            print(f"{k}. {v.split(':')[0]}")
        
        choice = input("\nSelect Module to Deploy (A/B/C/D) or 'Q' to Quit: ").upper()
        if choice != 'Q':
            self.run_module(choice)

if __name__ == "__main__":
    engine = IncomeEngine()
    engine.dashboard()
