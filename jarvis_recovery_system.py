import os
import subprocess

class PhoenixProtocol:
    def __init__(self):
        self.master = "Deepak"
        self.repo_url = "https://github.com/YOUR_USERNAME/Optimus-Jarvis.git"

    def initiate_recovery(self):
        print(f"\n\033[1;35m[PHOENIX PROTOCOL ACTIVE]\033[0m Scanning for corrupted or missing cores...")
        os.system('termux-tts-speak "Initiating Phoenix Protocol. Checking system integrity, Deepak sir."')
        
        # चेक करना कि क्या Git रिपॉजिटरी मौजूद है
        if not os.path.exists(".git"):
            print("\033[1;31m[CRITICAL]:\033[0m Local repository data missing!")
            os.system('termux-tts-speak "Critical failure. Local files are missing. Attempting cloud restoration."')
            os.system(f"git clone {self.repo_url} .")
        else:
            print("\033[1;33m[SYNCING]:\033[0m Fetching latest updates from Cloud...")
            os.system("git fetch --all")
            os.system("git reset --hard origin/main")
            
        print("\033[1;32m[RECOVERY COMPLETE]:\033[0m System core has been restored to its optimal state.")
        os.system('termux-tts-speak "System recovery successful. All phases are back online."')

if __name__ == "__main__":
    phoenix = PhoenixProtocol()
    phoenix.initiate_recovery()
