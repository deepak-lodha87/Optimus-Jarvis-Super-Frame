import os
import time
import shutil

def system_backup_protocol():
    print("\n" + "="*40)
    print("      JARVIS AUTOMATIC BACKUP SYSTEM")
    print("="*40)
    
    # बैकअप फोल्डर का नाम
    backup_dir = f"jarvis_backup_{time.strftime('%Y%m%d')}"
    
    msg_start = "Commander Deepak, initiating core backup sequence..."
    print(f"\n[JARVIS]: {msg_start}")
    os.system(f"termux-tts-speak '{msg_start}'")
    
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    # सभी .py फाइलों को कॉपी करना
    files = [f for f in os.listdir('.') if f.endswith('.py')]
    count = 0
    
    for file in files:
        shutil.copy(file, backup_dir)
        count += 1
        print(f"[PROCESS]: Backing up {file}...")
    
    msg_end = f"Backup complete. {count} files secured in {backup_dir} folder."
    print(f"\n[JARVIS]: {msg_end}")
    os.system(f"termux-tts-speak '{msg_end}'")
    print("="*40)

if __name__ == "__main__":
    system_backup_protocol()
