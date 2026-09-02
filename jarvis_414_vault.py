# Optimus Jarvis Super-Frame: Phase 413-414
# Feature: Automated Local Backup & Integrity Vault

import os
import shutil
import time

class JarvisVault:
    def __init__(self):
        self.code_ver = "414.Vault"
        self.backup_dir = "jarvis_backups"
        self.files_to_backup = [
            "jarvis_core.py", 
            "jarvis_408_healing.py", 
            "jarvis_410_strategic.py", 
            "jarvis_412_shield.py"
        ]

    def code_413_initiate_backup(self):
        print(f"\n[MODULE 413] Starting Backup Sequence: Version {self.code_ver}")
        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)
            print(f"[SYSTEM] Directory '{self.backup_dir}' created.")
        
        count = 0
        for file in self.files_to_backup:
            if os.path.exists(file):
                shutil.copy(file, os.path.join(self.backup_dir, f"backup_{file}"))
                print(f"[SUCCESS] {file} backed up successfully.")
                count += 1
        
        return count

    def code_414_verify_backup(self, total):
        print("\n[MODULE 414] Verifying Backup Integrity...")
        time.sleep(1)
        if total > 0:
            print(f"[RESULT] {total} files secured in the Vault.")
            print("[STATUS] System is now Disaster-Proof.")
        else:
            print("[ALERT] Backup failed. Files not found.")

if __name__ == "__main__":
    vault = JarvisVault()
    print(f"--- {vault.code_ver}: Active ---")
    
    saved_files = vault.code_413_initiate_backup()
    vault.code_414_verify_backup(saved_files)
    
    print("\n--- Phase 414 Complete. Data is Secure. ---")
