import os
from datetime import datetime

# UI Colors
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"
BOLD = "\033[1m"

def process_command(cmd):
    cmd = cmd.lower()
    print(f"\n[{YELLOW}ANALYZING{RESET}]: Intent recognition in progress...")
    
    if "backup" in cmd:
        print(f"[{GREEN}ACTION{RESET}]: Initiating redundancy protocol for Jarvis core files.")
    elif "scan" in cmd:
        files = os.listdir('.')
        print(f"[{GREEN}ACTION{RESET}]: Deep scan complete. {len(files)} files verified.")
    elif "exit" in cmd:
        print(f"[{RED}EXIT{RESET}]: Shutting down Optimus Super-Frame. Goodbye, Commander.")
        return False
    else:
        print(f"[{CYAN}INFO{RESET}]: Standard execution for task: '{cmd}'")
    return True

def check_vitals():
    print(f"\n{CYAN}{'='*45}{RESET}")
    print(f"{BOLD}      OPTIMUS JARVIS SUPER-FRAME{RESET}")
    print(f"{BOLD}      PHASE 263: INTENT ANALYZER{RESET}")
    print(f"{CYAN}{'='*45}{RESET}")
    print(f"[{GREEN}STATUS{RESET}]: Neural link active | Bypass mode stable.")

def mission_entry():
    print(f"\n{BOLD}[JARVIS]: System Online, Commander Deepak.{RESET}")
    check_vitals()
    
    active = True
    while active:
        task = input(f"\n[{YELLOW}MISSION-CMD{RESET}]: ")
        active = process_command(task)

if __name__ == "__main__":
    mission_entry()
