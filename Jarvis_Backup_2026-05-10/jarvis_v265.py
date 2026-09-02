import os

# UI Colors Dictionary
C = {
    "G": "\033[92m", 
    "R": "\033[91m", 
    "Y": "\033[93m", 
    "B": "\033[96m", 
    "W": "\033[0m", 
    "BOLD": "\033[1m"
}

def color_print(text, color_code):
    print(f"{color_code}{text}{C['W']}")

def create_file():
    filename = input(f"{C['Y']}[JARVIS]: Enter file name (with extension): {C['W']}")
    content = input(f"{C['Y']}[JARVIS]: Enter content for the file: {C['W']}")
    
    try:
        with open(filename, "w") as f:
            f.write(content)
        color_print(f"[SUCCESS]: File '{filename}' has been created.", C['G'])
    except Exception as e:
        color_print(f"[ERROR]: Failed to create file: {e}", C['R'])

def process_command(cmd):
    cmd = cmd.lower()
    if "create" in cmd or "file" in cmd:
        create_file()
    elif "exit" in cmd:
        color_print("Terminating link. Goodbye, Commander.", C['R'])
        return False
    else:
        color_print(f"Executing standard task: {cmd}", C['B'])
    return True

def mission_entry():
    color_print("="*45, C['B'])
    color_print("      OPTIMUS JARVIS SUPER-FRAME", C['BOLD'])
    color_print("      PHASE 265: FILE CREATION ENGINE", C['BOLD'])
    color_print("="*45, C['B'])
    
    active = True
    while active:
        task = input(f"\n{C['Y']}[MISSION-CMD]: {C['W']}")
        active = process_command(task)

if __name__ == "__main__":
    mission_entry()
