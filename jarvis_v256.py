import os
import time
from datetime import datetime

def mission_summary():
    print("\n" + "="*45)
    print("      OPTIMUS JARVIS: MISSION LOG")
    print("      PHASE 102: ANALYTICS")
    print("="*45)

    tasks = []
    total_minutes = 0

    while True:
        name = input("[INPUT]: Task Name (or 'DONE'): ")
        if name.upper() == 'DONE': break
        
        mins = input(f"Time spent on '{name}' (minutes): ")
        tasks.append({"name": name, "time": int(mins)})
        total_minutes += int(mins)

    print("\n" + "-"*30)
    print(f"COMMANDER, MISSION REPORT:")
    print(f"Total Tasks Completed: {len(tasks)}")
    print(f"Total Active Time: {total_minutes} minutes")
    
    if total_minutes > 120:
        print("Status: Highly Productive Day.")
    else:
        print("Status: Baseline Objectives Met.")
    print("-"*30)

if __name__ == "__main__":
    mission_summary()
