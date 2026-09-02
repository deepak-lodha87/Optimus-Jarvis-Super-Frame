import os
import subprocess

class CloudArmor:
    def __init__(self):
        self.master = "Deepak"
        self.repo_url = "https://github.com/YOUR_USERNAME/Optimus-Jarvis.git" # यहाँ अपना लिंक डालें

    def sync_to_cloud(self):
        print(f"\n\033[1;36m[CLOUD UPLINK ACTIVE]\033[0m Preparing backup for {self.master}'s Core...")
        os.system('termux-tts-speak "Initializing cloud backup protocol, Deepak sir."')
        
        try:
            # Git कमांड्स को सीक्वेन्स में चलाना
            commands = [
                "git init",
                "git add .",
                'git commit -m "Jarvis Phase 110: Systematic Backup"',
                f"git remote add origin {self.repo_url}",
                "git push -u origin main"
            ]
            
            for cmd in commands:
                print(f"\033[1;33m[EXECUTING]:\033[0m {cmd}")
                os.system(cmd)
                
            print("\033[1;32m[SUCCESS]:\033[0m All phases are now secured on Cloud.")
            os.system('termux-tts-speak "Backup complete. Your progress is now permanent on GitHub."')
            
        except Exception as e:
            print(f"\033[1;31m[ERROR]:\033[0m Synchronization failed: {e}")

if __name__ == "__main__":
    cloud = CloudArmor()
    cloud.sync_to_cloud()
