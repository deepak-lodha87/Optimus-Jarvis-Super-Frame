import os
from datetime import datetime

C = {"G": "\033[92m", "B": "\033[96m", "W": "\033[0m", "BOLD": "\033[1m"}

def mission_entry():
    now = datetime.now().strftime("%H:%M:%S")
    print(f"{C['B']}╔" + "═"*40 + "╗")
    print(f"║ {C['BOLD']}{'JARVIS DASHBOARD':^38} {C['B']}║")
    print(f"╠" + "═"*40 + "╣")
    print(f"║ {C['W']}TIME: {now:^33} {C['B']}║")
    print(f"║ {C['G']}PHASE: 273 (ACTIVE){C['B']:^29} ║")
    print(f"╚" + "═"*40 + f"╝{C['W']}")
    
    task = input(f"\n>> COMMAND: ")
    print(f"[JARVIS]: Processed '{task}'.")

if __name__ == "__main__":
    mission_entry()
