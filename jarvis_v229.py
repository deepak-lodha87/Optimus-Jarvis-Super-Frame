import os
import time
import shutil

def emergency_lockdown():
    print("\n" + "="*40)
    print("      JARVIS EMERGENCY LOCKDOWN MODE")
    print("="*40)
    
    msg_warn = "Commander Deepak, priority alert! Confirm lockdown activation?"
    print(f"\n[ALERT]: {msg_warn}")
    os.system(f"termux-tts-speak '{msg_warn}'")
    
    confirm = input("\n[INPUT]: Type 'ACTIVATE' to secure data: ")
    
    if confirm == 'ACTIVATE':
        lock_dir = "SECRET_VAULT_LOCKED"
        if not os.path.exists(lock_dir):
            os.makedirs(lock_dir)
            
        # संवेदनशील फाइलों की लिस्ट
        sensitive_files = ["vault_data.txt", "expense_log.txt", "command_log.txt", "academic_vault.txt"]
        
        msg_process = "Initiating data isolation protocol..."
        print(f"\n[JARVIS]: {msg_process}")
        os.system(f"termux-tts-speak '{msg_process}'")
        
        count = 0
        for file in sensitive_files:
            if os.path.exists(file):
                shutil.move(file, os.path.join(lock_dir, file))
                count += 1
                print(f"[SECURED]: {file} moved to encrypted vault.")
        
        success = f"Lockdown complete. {count} sensitive files have been isolated."
        print(f"\n[STATUS]: {success}")
        os.system(f"termux-tts-speak '{success}'")
    else:
        print("\n[CANCELLED]: Lockdown aborted. System remains in normal state.")

    print("\n" + "="*40)

if __name__ == "__main__":
    emergency_lockdown()
