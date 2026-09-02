import os
import shutil

# UI Colors Dictionary
C = {"G": "\033[92m", "R": "\033[91m", "Y": "\033[93m", "B": "\033[96m", "W": "\033[0m", "BOLD": "\033[1m"}

def color_print(text, color_code):
    print(f"{color_code}{text}{C['W']}")

def backup_file():
    filename = input(f"{C['Y']}[JARVIS]: Source file for backup: {C['W']}")
    if os.path.exists(filename):
        backup_name = filename + ".bak"
        try:
            shutil.copy(filename, backup_name)
            color_print(f"[SUCCESS]: Redundancy created at '{backup_name}'.", C['G'])
        except Exception as e:
            color_print(f"[ERROR]: Backup failed: {e}", C['R'])
    else:
        color_print("[ERROR]: Source file not detected.", C['R'])

def process_command(cmd):
    cmd = cmd.lower()
    if "backup" in cmd:
        backup_file()
    elif "exit" in cmd:
        color_print("Disconnecting Super-Frame. Goodbye, Commander.", C['R'])
        return False
    else:
        color_print(f"Executing standard logic: {cmd}", C['B'])
    return True

def mission_entry():
    color_print("="*45, C['B'])
    color_print("      OPTIMUS JARVIS SUPER-FRAME", C['BOLD'])
    color_print("      PHASE 268: BACKUP & REDUNDANCY", C['BOLD'])
    color_print("="*45, C['B'])
    
    active = True
    while active:
        task = input(f"\n{C['Y']}[MISSION-CMD]: {C['W']}")
        active = process_command(task)

if __name__ == "__main__":
    mission_entry()
