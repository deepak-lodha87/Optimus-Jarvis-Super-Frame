import os
import shutil
import time
from datetime import datetime

class JarvisBackupSystem:
    def __init__(self):
        self.backup_name = f"Jarvis_Master_Archive_{datetime.now().strftime('%Y%m%d_%H%M')}"
        # Sirf files ko select karna, folders ko nahi
        self.items = [f for f in os.listdir('.') if f.startswith('jarvis_')]

    def execute_backup(self):
        print(f"\033[1;36m[BACKUP-CORE]\033[0m Initializing Secure Backup...")
        time.sleep(1)
        
        if not os.path.exists(self.backup_name):
            os.makedirs(self.backup_name)
            
        print(f"\033[1;34m[SYNC]\033[0m Filtering modules for backup...")
        
        for item in self.items:
            # Ye line check karegi ki 'item' file hai ya folder
            if os.path.isfile(item):
                shutil.copy(item, self.backup_name)
                print(f" > Backing up: {item} [\033[1;32mDONE\033[0m]")
            else:
                # Agar folder hai toh use skip kar dega
                print(f" > Skipping directory: {item} [\033[1;33mSKIP\033[0m]")
            
        # Zipping the final backup
        shutil.make_archive(self.backup_name, 'zip', self.backup_name)
        
        # Safai (Original backup folder delete karna, sirf zip rakhna)
        shutil.rmtree(self.backup_name)
        
        print(f"\n\033[1;32m[SUCCESS]\033[0m Data secured in: {self.backup_name}.zip")
        print(f"\033[1;35m[VOICE] Deepak sir, I have filtered out the directories. \nYour core files are now perfectly archived.\033[0m")

if __name__ == "__main__":
    backup = JarvisBackupSystem()
    backup.execute_backup()
