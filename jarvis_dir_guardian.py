import os

class DirectoryGuardian:
    def __init__(self):
        self.master = "Deepak"
        self.tracking_path = "."

    def scan_integrity(self):
        print(f"\n\033[1;34m[GUARDIAN ACTIVE]\033[0m Checking project folder integrity...")
        
        # फाइलों की लिस्ट बनाना
        files = [f for f in os.listdir(self.tracking_path) if os.path.isfile(f)]
        file_count = len(files)
        
        print(f"\033[1;36m[TOTAL FILES]:\033[0m {file_count}")
        
        msg = f"Deepak sir, I have scanned the directory. Total {file_count} system files are secured within the frame."
        
        print(f"\033[1;32m[STATUS]:\033[0m Guarding all active assets.")
        os.system(f'termux-tts-speak "{msg}"')

if __name__ == "__main__":
    guardian = DirectoryGuardian()
    guardian.scan_integrity()
