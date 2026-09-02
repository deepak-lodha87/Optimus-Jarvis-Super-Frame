import os
import shutil
from datetime import datetime

class BackupSystem:
    def __init__(self):
        self.source_dir = os.getcwd()
        self.backup_dir = os.path.join(self.source_dir, "Jarvis_Backups")
        
        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)

    def create_snapshot(self):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        backup_folder = os.path.join(self.backup_dir, f"Backup_{timestamp}")
        os.makedirs(backup_folder)
        
        print(f"\033[1;34m[BACKUP] Initiating Memory Snapshot: {timestamp}...\033[0m")
        
        # Files to backup
        files_to_save = [f for f in os.listdir(self.source_dir) if f.endswith('.py')]
        
        for file in files_to_save:
            shutil.copy(file, backup_folder)
            print(f"  • {file} --> Secured.")
            
        print(f"\033[1;32m[SUCCESS] Project 'Optimus Jarvis Super-Frame' is now safe.\033[0m")

if __name__ == "__main__":
    vault = BackupSystem()
    print("-" * 50)
    print("   JARVIS INTEGRATED BACKUP PROTOCOL")
    print("-" * 50)
    vault.create_snapshot()
