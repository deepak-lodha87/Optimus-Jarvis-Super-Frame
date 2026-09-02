import os
import psutil
from datetime import datetime

# ANSI Color Codes
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"
BOLD = "\033[1m"

def check_system_vitals():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()

    print(f"\n{CYAN}{'='*45}{RESET}")
    print(f"{BOLD}      OPTIMUS JARVIS SUPER-FRAME{RESET}")
    print(f"{BOLD}      PHASE 258: SYSTEM VITALS MONITOR{RESET}")
    print(f"{CYAN}{'='*45}{RESET}")

    print(f"[{YELLOW}STATUS{RESET}]: Scanning Hardware...")
    print(f"CPU Usage: {cpu_usage}%")
    print(f"RAM Usage: {memory_info.percent}%")

    if cpu_usage > 80 or memory_info.percent > 80:
        print(f"[{RED}WARNING{RESET}]: System load is {RED}CRITICAL{RESET}, Commander.")
    else:
        print(f"[{GREEN}REPORT{RESET}]: All systems {GREEN}OPERATIONAL{RESET} and within limits.")
    print(f"{CYAN}{'='*45}{RESET}")

def mission_entry():
    now = datetime.now().strftime("%H:%M")
    print(f"\n{BOLD}[JARVIS]: Welcome back, Commander Deepak. Time: {now}{RESET}")
    
    check_system_vitals()

    task = input(f"\n[{YELLOW}INPUT{RESET}]: Direct command for Phase 258: ")
    print(f"{GREEN}[JARVIS]: Executing '{task}'... Done.{RESET}")

if __name__ == "__main__":
    mission_entry()
