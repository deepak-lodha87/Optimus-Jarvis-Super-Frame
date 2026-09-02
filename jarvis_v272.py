import os
from datetime import datetime

# HUD UI Colors
C = {"G": "\033[92m", "R": "\033[91m", "Y": "\033[93m", "B": "\033[96m", "W": "\033[0m", "BOLD": "\033[1m"}

def get_time_greeting():
    hour = datetime.now().hour
    if hour < 12: return "GOOD MORNING"
    elif 12 <= hour < 18: return "GOOD AFTERNOON"
    else: return "GOOD EVENING"

def mission_entry():
    greeting = get_time_greeting()
    now = datetime.now().strftime("%d/%m/%Y | %H:%M:%S")
    
    # HUD Interface Layout
    border = f"{C['B']}# {C['W']}"
    print(f"{C['B']}" + "═"*50)
    print(f"║ {C['BOLD']}{greeting:^46} {C['B']}║")
    print(f"║ {C['W']}{now:^46} {C['B']}║")
    print(f"╠" + "═"*50 + "╣")
    print(f"║ {C['G']}SYSTEM STATUS: OPTIMAL{C['B']:>26} ║")
    print(f"║ {C['G']}PHASE: 272 (HUD INTERFACE){C['B']:>23} ║")
    print(f"╚" + "═"*50 + f"╝{C['W']}")
    
    task = input(f"\n{C['Y']}>> EXECUTE COMMAND: {C['W']}")
    print(f"\n{C['B']}[JARVIS]: Request '{task}' is being processed...{C['W']}")

if __name__ == "__main__":
    mission_entry()
