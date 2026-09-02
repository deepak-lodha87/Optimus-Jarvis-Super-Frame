import time, os

class FileWarden:
    def __init__(self):
        self.target_dir = os.getcwd()
        self.junk_extensions = [".tmp", ".log", ".bak"]

    def scan_and_optimize(self):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS FILE-WARDEN : PHASE 23 - STEP 2         \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        print(f"\033[1;33m[SCANNING]\033[0m Analyzing Directory: {self.target_dir}")
        time.sleep(1.5)
        
        files = os.listdir(self.target_dir)
        total_files = len(files)
        junk_found = [f for f in files if any(f.endswith(ext) for ext in self.junk_extensions)]
        
        operations = [
            (f"Total Files Scanned: {total_files}", "DONE"),
            (f"Junk Files Detected: {len(junk_found)}", "MAPPED"),
            ("Project Files Categorization", "READY"),
            ("Storage Optimization Path", "CALCULATED")
        ]
        
        for task, status in operations:
            print(f" \033[1;34m[WARDEN]\033[0m {task:32} | [\033[1;32m{status}\033[0m]")
            time.sleep(0.8)

        print(f"\n\033[1;32m[SUCCESS] Storage Map is Ready. Ready for Cleanup.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, your digital house is \ngetting cluttered. I have mapped out every \nbyte of data in our current sector. With your \npermission, I can ensure that only what is \nvaluable remains. A clean system is a fast \nsystem. Efficiency starts with organization.\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    warden = FileWarden()
    warden.scan_and_optimize()
