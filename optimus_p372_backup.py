import os
import zipfile
import time
import subprocess

def optimus_speak(text):
    print(f"\033[1;34m[OPTIMUS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def create_system_backup():
    os.system('clear')
    print("\033[1;36m" + "📦"*30)
    print("      OPTIMUS NEURAL SYSTEMS : FULL IMAGE BACKUP (P372)")
    print("📦"*30 + "\033[0m")
    
    optimus_speak("Initiating neural archive protocol. Compressing all operational phases.")
    
    backup_filename = f"Optimus_Core_Backup_{time.strftime('%Y%m%d_%H%M%S')}.zip"
    
    # List of all files to include
    files_to_backup = [f for f in os.listdir('.') if f.endswith(('.py', '.sh', '.txt'))]
    
    print(f"\n\033[1;33m[SCANNING]: Found {len(files_to_backup)} critical files...\033[0m")
    time.sleep(1)
    
    try:
        with zipfile.ZipFile(backup_filename, 'w') as zip_ref:
            for file in files_to_backup:
                print(f"\033[1;32m[ARCHIVING]:\033[0m {file}")
                zip_ref.write(file)
                time.sleep(0.1)
                
        print("-" * 50)
        print(f"\033[1;36m[SUCCESS]: Full System Backup Created: {backup_filename}\033[0m")
        optimus_speak("Full system image has been successfully archived. Your neural data is secure.")
        
    except Exception as e:
        print(f"\033[1;31m[ERROR]: Backup failed: {str(e)}\033[0m")
        optimus_speak("Warning. Backup protocol encountered an error.")

if __name__ == "__main__":
    create_system_backup()
