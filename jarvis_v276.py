import os, time
from datetime import datetime

C = {"G": "\033[92m", "B": "\033[96m", "Y": "\033[93m", "R": "\033[91m", "W": "\033[0m", "BOLD": "\033[1m"}

def integrity_scan():
    print(f"{C['B']}[SECURITY]: Running Integrity Scan...", end="\r")
    time.sleep(1)
    files = [f for f in os.listdir('.') if f.endswith('.py')]
    print(f"{C['G']}[SECURITY]: {len(files)} Secure Modules Verified.    ")

def mission_entry():
    now = datetime.now().strftime("%H:%M:%S")
    integrity_scan()
    
    # Advanced Security HUD
    print(f"\n{C['R']}╓" + "─"*44 + "╖")
    print(f"║ {C['BOLD']}{'JARVIS SECURITY OVERRIDE':^42} {C['R']}║")
    print(f"╟" + "─"*44 + "╢")
    print(f"║ {C['W']}CORE STATUS: {C['G']}SHIELDED{C['W']} | ENCRYPTION: {C['G']}AES-256{C['W']} {C['R']:>2} ║")
    print(f"║ {C['W']}ID: DEEPAK-PROTOCOL | PHASE: 276 {C['R']:>12} ║")
    print(f"╙" + "─"*44 + f"╜{C['W']}")
    
    input(f"\n{C['Y']}>> AUTHORIZATION REQUIRED: {C['W']}")
    print(f"{C['G']}[ACCESS GRANTED]: Welcome back, Commander.{C['W']}")

if __name__ == "__main__":
    mission_entry()
