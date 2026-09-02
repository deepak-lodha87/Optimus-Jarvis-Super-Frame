import time, sys, os
from datetime import datetime

C = {"G": "\033[92m", "B": "\033[96m", "Y": "\033[93m", "R": "\033[91m", "W": "\033[0m", "BOLD": "\033[1m"}

def status_check():
    # Simulated system vitals
    print(f"{C['Y']}[SYSTEM]: Running Diagnostic Protocols...", end="\r")
    time.sleep(1.5)
    print(f"{C['G']}[SYSTEM]: Vitals Stable | Neural Link: 100%    {C['W']}")

def mission_entry():
    now = datetime.now().strftime("%H:%M:%S")
    status_check()
    
    # Advanced HUD with Health Bars
    print(f"\n{C['B']}╔" + "═"*44 + "╗")
    print(f"║ {C['BOLD']}{'MARK-V SYSTEM INTERFACE':^42} {C['B']}║")
    print(f"╠" + "═"*44 + "╣")
    print(f"║ {C['W']}CORE TEMP: {C['G']}OPTIMAL{C['W']} | STABILITY: {C['G']}98.4%{C['W']} {C['B']:>4} ║")
    print(f"║ {C['W']}TIME: {now:^12} | PHASE: 275 {C['B']:>13} ║")
    print(f"╠" + "═"*44 + "╣")
    print(f"║ {C['BOLD']}{C['Y']}STATUS: ALL SYSTEMS ARE GOING GREEN{C['B']:>8} ║")
    print(f"╚" + "═"*44 + f"╝{C['W']}")
    
    task = input(f"\n{C['Y']}>> COMMAND: {C['W']}")
    print(f"\n{C['B']}[JARVIS]: Deploying '{task}' sequences...{C['W']}")

if __name__ == "__main__":
    mission_entry()
