import os
from datetime import datetime

# ANSI Color Codes
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"
BOLD = "\033[1m"

def scan_directory():
    try:
        files = os.listdir('.')
        file_count = len(files)
        print(f"[{CYAN}SCANNER{RESET}]: {file_count} items detected in root directory.")
    except Exception as e:
        print(f"[{RED}ERROR{RESET}]: Scanning failed: {e}")

def log_access():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("access_log.txt", "a") as f:
        f.write(f"Phase 262 accessed at: {now}\n")
    print(f"[{GREEN}SECURE{RESET}]: Access Log Synchronized.")

def check_system_vitals():
    # Android restrictions की वजह से psutil को bypass करना
    print(f"\n{CYAN}{'='*45}{RESET}")
    print(f"{BOLD}      OPTIMUS JARVIS SUPER-FRAME{RESET}")
    print(f"{BOLD}      PHASE 262: BYPASS PROTOCOL{RESET}")
    print(f"{CYAN}{'='*45}{RESET}")
    print(f"[{YELLOW}SYSTEM{RESET}]: Hardware monitoring is restricted by OS.")
    print(f"[{GREEN}STATUS{RESET}]: Core logic is still functional.")

def mission_entry():
    print(f"\n{BOLD}[JARVIS]: Initializing Phase 262...{RESET}")
    log_access()
    check_system_vitals()
    scan_directory()

    task = input(f"\n[{YELLOW}MISSION-CMD{RESET}]: ")
    print(f"{GREEN}[JARVIS]: '{task}' processed via Bypass Mode.{RESET}")

if __name__ == "__main__":
    mission_entry()
