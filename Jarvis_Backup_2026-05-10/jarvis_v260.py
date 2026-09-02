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

def scan_directory():
    # करंट फोल्डर की फाइलों को गिनना
    files = os.listdir('.')
    file_count = len(files)
    print(f"[{CYAN}SCANNER{RESET}]: {file_count} items detected in root directory.")
    return file_count

def log_access():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("access_log.txt", "a") as f:
        f.write(f"Phase 260 accessed by Commander Deepak at: {now}\n")

def check_system_vitals():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    print(f"\n{CYAN}{'='*45}{RESET}")
    print(f"{BOLD}      OPTIMUS JARVIS SUPER-FRAME{RESET}")
    print(f"{BOLD}      PHASE 260: DIRECTORY ANALYZER{RESET}")
    print(f"{CYAN}{'='*45}{RESET}")
    print(f"[{YELLOW}HARDWARE{RESET}]: CPU {cpu}% | RAM {ram}%")

def mission_entry():
    print(f"\n{BOLD}[JARVIS]: Initializing Phase 260...{RESET}")
    log_access()
    check_system_vitals()
    scan_directory()

    task = input(f"\n[{YELLOW}MISSION-CMD{RESET}]: ")
    print(f"{GREEN}[JARVIS]: '{task}' has been processed.{RESET}")

if __name__ == "__main__":
    mission_entry()
