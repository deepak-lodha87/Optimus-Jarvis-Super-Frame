import time, sys
from datetime import datetime

C = {"G": "\033[92m", "B": "\033[96m", "Y": "\033[93m", "W": "\033[0m", "BOLD": "\033[1m"}

def loading_effect():
    print(f"{C['G']}[JARVIS]: Initializing", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="")
        sys.stdout.flush()
    print(f" ONLINE{C['W']}\n")

def mission_entry():
    now = datetime.now().strftime("%H:%M:%S")
    loading_effect()
    
    # HUD Interface
    print(f"{C['B']}╔" + "═"*40 + "╗")
    print(f"║ {C['BOLD']}{'SYSTEM INTERFACE ACTIVE':^38} {C['B']}║")
    print(f"╠" + "═"*40 + "╣")
    print(f"║ {C['W']}TIME: {now:^33} {C['B']}║")
    print(f"║ {C['G']}PHASE: 274 (ANIMATION CORE){C['B']:^26} ║")
    print(f"╚" + "═"*40 + f"╝{C['W']}")
    
    task = input(f"\n{C['Y']}>> COMMAND: {C['W']}")
    print(f"\n{C['B']}[JARVIS]: Executing '{task}' protocol...{C['W']}")

if __name__ == "__main__":
    mission_entry()
