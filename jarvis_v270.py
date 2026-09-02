import os

# Ultra-UI Colors
C = {"G": "\033[92m", "R": "\033[91m", "Y": "\033[93m", "B": "\033[96m", "W": "\033[0m", "BOLD": "\033[1m"}

def color_print(text, color_code):
    print(f"{color_code}{text}{C['W']}")

def search_files():
    keyword = input(f"{C['Y']}[JARVIS]: Enter file name or keyword to find: {C['W']}").lower()
    files = os.listdir('.')
    found_files = [f for f in files if keyword in f.lower()]
    
    if found_files:
        color_print(f"\n[SCAN COMPLETE]: {len(found_files)} matches found.", C['G'])
        for f in found_files:
            size = os.path.getsize(f)
            print(f"{C['B']}-> {f}{C['W']} ({size} bytes)")
    else:
        color_print(f"[ALERT]: No files matching '{keyword}' were detected.", C['R'])

def process_command(cmd):
    cmd = cmd.lower()
    if "search" in cmd or "find" in cmd:
        search_files()
    elif "exit" in cmd:
        color_print("Offline. Security protocols engaged.", C['R'])
        return False
    else:
        color_print(f"Executing command: {cmd}", C['B'])
    return True

def mission_entry():
    color_print("="*45, C['B'])
    color_print("      OPTIMUS JARVIS SUPER-FRAME", C['BOLD'])
    color_print("      PHASE 270: SEARCH & ACQUISITION", C['BOLD'])
    color_print("="*45, C['B'])
    
    active = True
    while active:
        task = input(f"\n{C['Y']}[MISSION-CMD]: {C['W']}")
        active = process_command(task)

if __name__ == "__main__":
    mission_entry()
