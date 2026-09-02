import os

# Optimized UI Colors
C = {"G": "\033[92m", "R": "\033[91m", "Y": "\033[93m", "B": "\033[96m", "W": "\033[0m", "BOLD": "\033[1m"}

def color_print(text, color_code):
    print(f"{color_code}{text}{C['W']}")

def read_file():
    filename = input(f"{C['Y']}[JARVIS]: File name to scan: {C['W']}")
    if os.path.exists(filename):
        size = os.path.getsize(filename)
        color_print(f"[INFO]: Data size: {size} bytes.", C['B'])
        with open(filename, "r") as f:
            content = f.read()
            color_print("--- START OF DATA ---", C['Y'])
            print(content)
            color_print("--- END OF DATA ---", C['Y'])
    else:
        color_print("[ERROR]: Target file not found.", C['R'])

def process_command(cmd):
    cmd = cmd.lower()
    if "read" in cmd or "scan" in cmd:
        read_file()
    elif "exit" in cmd:
        color_print("System offline. Goodbye, Commander.", C['R'])
        return False
    else:
        color_print(f"Executing standard logic: {cmd}", C['B'])
    return True

def mission_entry():
    color_print("="*45, C['B'])
    color_print("      OPTIMUS JARVIS SUPER-FRAME", C['BOLD'])
    color_print("      PHASE 267: DATA ANALYZER CORE", C['BOLD'])
    color_print("="*45, C['B'])
    
    active = True
    while active:
        task = input(f"\n{C['Y']}[MISSION-CMD]: {C['W']}")
        active = process_command(task)

if __name__ == "__main__":
    mission_entry()
