import os
import glob

class SystemPurge:
    def __init__(self):
        self.master = "Deepak"

    def execute_purge(self):
        print(f"\n\033[1;31m[SYSTEM PURGE ACTIVE]\033[0m Clearing digital debris...")
        os.system('termux-tts-speak "Deepak sir, initiating system purge to optimize performance."')
        
        # फालतू फाइलों के एक्सटेंशन (जैसे पुरानी लॉग्स या टेम्प फाइल्स)
        junk_extensions = ['*.log', '*.tmp', '__pycache__']
        files_removed = 0
        
        for ext in junk_extensions:
            files = glob.glob(ext)
            for f in files:
                os.remove(f)
                files_removed += 1
                
        print(f"\033[1;32m[SUCCESS]:\033[0m {files_removed} junk files cleared.")
        os.system(f'termux-tts-speak "Purge complete. {files_removed} files removed. System is now lean and fast."')

if __name__ == "__main__":
    purge = SystemPurge()
    purge.execute_purge()
