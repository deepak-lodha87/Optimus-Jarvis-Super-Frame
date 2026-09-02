import os

# Professional UI Colors
C = {"G": "\033[92m", "R": "\033[91m", "Y": "\033[93m", "B": "\033[96m", "W": "\033[0m", "BOLD": "\033[1m"}

def color_print(text, color_code):
    print(f"{color_code}{text}{C['W']}")

def inventory_scan():
    color_print("\n[SCANNING PROJECT INVENTORY...]", C['BOLD'])
    files = os.listdir('.')
    color_print(f"{'FILE NAME':<30} | {'SIZE (Bytes)':<10}", C['Y'])
    color_print("-" * 45, C['Y'])
    
    for file in files:
        size = os.path.getsize(file)
        # अगर फाइल बैकअप है तो उसे अलग रंग में दिखाएंगे
        color = C['G'] if file.endswith('.bak') else C['W']
        print(f"{color}{file:<30}{C['W']} | {size:<10}")
    
    color_print("-" * 45, C['Y'])
    color_print(f"Total Assets Detected: {len(files)}", C['B'])

def process_command(cmd):
    cmd = cmd.lower()
    if "inventory" in cmd or "list" in cmd:
        inventory_scan()
    elif "exit" in cmd:
        color_print("Terminating link. System Secure.", C['R'])
        return False
    else:
        color_print(f"Executing logic: {cmd}", C['B'])
    return True

def mission_entry():
    color_print("="*45, C['B'])
    color_print("      OPTIMUS JARVIS SUPER-FRAME", C['BOLD'])
    color_print("      PHASE 269: INVENTORY MANAGEMENT", C['BOLD'])
    color_print("="*45, C['B'])
    
    active = True
    while active:
        task = input(f"\n{C['Y']}[MISSION-CMD]: {C['W']}")
        active = process_command(task)

if __name__ == "__main__":
    mission_entry()
