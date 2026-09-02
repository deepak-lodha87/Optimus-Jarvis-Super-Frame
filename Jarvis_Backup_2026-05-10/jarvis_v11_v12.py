# =======================================================
# OPTIMUS JARVIS SUPER-FRAME: PHASE 2011 & 2012
# MODULES: ENV SENSING + TASK AUTOMATION
# =======================================================

import os
import time

def display_dashboard():
    os.system('clear')
    print("\033[1;36m=======================================================")
    print("      OPTIMUS JARVIS SUPER-FRAME: SESSION START        ")
    print("=======================================================\033[0m")
    print("\033[1;33mPHASE STATUS: 2011 & 2012 (ENV & AUTOMATION)\033[0m")
    print("\033[1;32m-------------------------------------------------------\033[0m")

# --- CODE 1: PHASE 2011 ENVIRONMENTAL SENSING ---
def env_sensing():
    print("\033[1;34m[MODULE 1] PHASE 2011: SENSING ENVIRONMENT...\033[0m")
    sensors = {"Temp": "32°C", "Signal": "5G-Full", "Battery": "Optimal"}
    for key, val in sensors.items():
        print(f"  > Reading {key}: {val}")
        time.sleep(0.5)

# --- CODE 2: PHASE 2012 ADVANCED AUTOMATION ---
def auto_scripts():
    print("\n\033[1;35m[MODULE 2] PHASE 2012: AUTOMATION SCRIPTS...\033[0m")
    tasks = ["Cleaning Cache", "Checking GitHub Sync", "Optimizing RAM"]
    for task in tasks:
        print(f"  > Executing: {task}...")
        time.sleep(0.7)
    print("\033[1;32m  [SUCCESS] All routine tasks automated.\033[0m")

if __name__ == "__main__":
    display_dashboard()
    env_sensing()
    auto_scripts()
