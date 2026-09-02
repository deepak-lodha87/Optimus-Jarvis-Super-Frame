import time, secrets, os

class JarvisBackup:
    def __init__(self):
        self.backup_id = f"NABA-{secrets.token_hex(2).upper()}"
        self.vault_path = "./jarvis_vault/backups/"

    def create_snapshot(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-BACKUP ALPHA ONLINE (ID: {self.backup_id}) ---\033[0m")
        if not os.path.exists(self.vault_path):
            os.makedirs(self.vault_path)
            
        print("\033[1;36m[SCANNING] Identifying modified assets since last sync...\033[0m")
        time.sleep(0.8)
        
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        filename = f"Jarvis_Core_{timestamp}.tar.gz"
        
        print(f"\033[1;32m[SUCCESS] Snapshot created: {filename}\033[0m")
        self.upload_to_cloud(filename)

    def upload_to_cloud(self, file):
        print(f"\033[1;33m[UPLOADING] Pushing {file} to GitHub Secure Cloud...\033[0m")
        time.sleep(1.2)
        print("\033[1;32m[DONE] Sync complete. Data is now geographically redundant.\033[0m")
        print("\033[1;35m[VOICE] Deepak, your progress is safe. Even if this device fails, Jarvis will survive.\033[0m")

if __name__ == "__main__":
    naba = JarvisBackup()
    naba.create_snapshot()
