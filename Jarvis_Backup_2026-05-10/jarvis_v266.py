import os

# UI Colors
C = {"G": "\033[92m", "R": "\033[91m", "Y": "\033[93m", "B": "\033[96m", "W": "\033[0m", "BOLD": "\033[1m"}

def color_print(text, color_code):
    print(f"{color_code}{text}{C['W']}")

def delete_file():
    filename = input(f"{C['Y']}[JARVIS]: Enter file name to delete: {C['W']}")
    if os.path.exists(filename):
        confirm = input(f"{C['R']}[WARNING]: Are you sure you want to delete '{filename}'? (y/n): {C['W']}").lower()
        if confirm == 'y':
            os.remove(filename)
            color_print(f"[SUCCESS]: '{filename}' has been permanently removed.", C['G'])
        else:
            color_print("[CANCELLED]: Deletion aborted by Commander.", C['B'])
    else:
        color_print(f"[ERROR]: File '{filename}' not found.", C['R'])

def process_command(cmd):
    cmd = cmd.lower()
    if "delete" in cmd or "remove" in cmd:
        delete_file()
    elif "exit" in cmd:
        color_print("Terminating link. Goodbye, Commander.", C['R'])
        return False
    else:
        color_print(f"Standard operation: {cmd}", C['B'])
    return True

def mission_entry():
    color_print("="*45, C['B'])
    color_print("      OPTIMUS JARVIS SUPER-FRAME", C['BOLD'])
    color_print("      PHASE 266: DELETION PROTOCOL", C['BOLD'])
    color_print("="*45, C['B'])
    
    active = True
    while active:
        task = input(f"\n{C['Y']}[MISSION-CMD]: {C['W']}")
        active = process_command(task)

if __name__ == "__main__":
    mission_entry()
