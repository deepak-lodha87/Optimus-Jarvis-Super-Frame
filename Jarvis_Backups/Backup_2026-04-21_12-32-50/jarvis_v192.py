import os
import time
import shutil

def auto_backup_protocol():
    print("\n[SYSTEM]: Initializing Auto-Backup Sequence...")
    time.sleep(1)
    
    source_file = "jarvis_v192.py"
    backup_file = "jarvis_v192_backup.py"
    
    try:
        if os.path.exists(source_file):
            shutil.copy(source_file, backup_file)
            print(f"[SUCCESS]: Backup created: {backup_file}")
            msg = "Commander Deepak, system core files have been backed up successfully."
            os.system(f"termux-tts-speak '{msg}'")
        else:
            print("[ERROR]: Source file not found for backup.")
    except Exception as e:
        print(f"[ERROR]: Backup failed. Reason: {str(e)}")

def jarvis_main():
    print("\n" + "="*50)
    print("|    JARVIS PHASE 192: AUTO-BACKUP & PROTECTION    |")
    print("="*50)
    
    auto_backup_protocol()
    
    print("\n[SYSTEM]: Optimus Jarvis Super-Frame is fortified.")
    print("="*50)

if __name__ == "__main__":
    jarvis_main()
