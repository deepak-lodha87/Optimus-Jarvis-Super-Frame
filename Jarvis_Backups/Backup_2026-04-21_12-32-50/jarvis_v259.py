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

def log_access():
    # एक्सेस लॉग फाइल में एंट्री दर्ज करना
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("access_log.txt", "a") as f:
        f.write(f"Access granted to Commander Deepak at: {now}\n")
    print(f"[{GREEN}SECURE{RESET}]: Access Log Updated.")

def check_system_vitals():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()

    print(f"\n{CYAN}{'='*45}{RESET}")
    print(f"{BOLD}      OPTIMUS JARVIS SUPER-FRAME{RESET}")
    print(f"{BOLD}      PHASE 259: SECURITY & VITALS{RESET}")
    print(f"{CYAN}{'='*45}{RESET}")

    print(f"[{YELLOW}STATUS{RESET}]: Scanning Hardware...")
    print(f"CPU: {cpu_usage}% | RAM: {memory_info.percent}%")

    if cpu_usage > 85 or memory_info.percent > 85:
        print(f"[{RED}ALERT{RESET}]: System strain detected!")
    else:
        print(f"[{GREEN}STABLE{RESET}]: Core temperature normal.")

def mission_entry():
    now = datetime.now().strftime("%H:%M")
    print(f"\n{BOLD}[JARVIS]: System Online, Commander Deepak. Time: {now}{RESET}")
    
    log_access()
    check_system_vitals()

    task = input(f"\n[{YELLOW}MISSION-CMD{RESET}]: ")
    print(f"{GREEN}[JARVIS]: Process '{task}' initiated... Successfully.{RESET}")

if __name__ == "__main__":
    mission_entry()
