import os
import tarfile
import datetime

class BackupMaster:
    def __init__(self):
        self.master = "Deepak"
        self.backup_name = f"Jarvis_Master_Backup_{datetime.datetime.now().strftime('%Y%m%d')}.tar.gz"
        # उन सभी फाइल्स की लिस्ट जो हमने अब तक बनाई हैं
        self.files_to_backup = [f for f in os.listdir('.') if f.endswith('.py') or f.endswith('.json') or f.endswith('.log')]

    def create_full_backup(self):
        print(f"\n\033[1;33m[MASTER BACKUP INITIATED]\033[0m")
        print(f"Scanning millions of protocol cycles...")
        
        try:
            with tarfile.open(self.backup_name, "w:gz") as tar:
                for file in self.files_to_backup:
                    tar.add(file)
            
            print(f"\033[1;32m[SUCCESS]:\033[0m All data consolidated into {self.backup_name}")
            msg = f"Deepak sir, the master backup of your entire project is ready. All protocols are now unified."
            os.system(f'termux-tts-speak "{msg}"')
            
        except Exception as e:
            print(f"\033[1;31m[ERROR]:\033[0m Backup failed. {e}")

    def restore_all(self):
        # भविष्य में एक साथ सब कुछ खोलने के लिए
        print(f"\033[1;34m[RESTORE SYSTEM]:\033[0m Ready to extract all protocols from backup.")

if __name__ == "__main__":
    manager = BackupMaster()
    manager.create_full_backup()
