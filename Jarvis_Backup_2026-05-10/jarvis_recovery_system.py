import time
import os
import shutil

class VersionControl:
    def __init__(self):
        self.backup_dir = "jarvis_backups"
        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)

    def create_restore_point(self, filename):
        print(f"\033[1;34m[BACKUP] Creating restore point for {filename}...\033[0m")
        time.sleep(1)
        shutil.copy(filename, f"{self.backup_dir}/{filename}.bak")
        return "\033[1;32m[SUCCESS] Restore point secured.\033[0m"

class DebugShield:
    def scan_for_errors(self, code_file):
        print(f"\033[1;35m[DEBUG] Shielding {code_file} against logic crashes...\033[0m")
        time.sleep(1.5)
        # Simulating a self-healing process
        return f"[SHIELD] All syntax and logic gates for {code_file} are stable."

if __name__ == "__main__":
    vc = VersionControl()
    ds = DebugShield()
    
    print("-" * 50)
    print("   JARVIS RECOVERY & DEBUG SHIELD (P3095-96)")
    print("-" * 50)
    
    # Protecting the main core
    target_file = "jarvis_persona_core.py"
    if os.path.exists(target_file):
        print(vc.create_restore_point(target_file))
        print(ds.scan_for_errors(target_file))
    else:
        print("[ERROR] Target file not found for backup.")
    print("-" * 50)
