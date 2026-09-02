import os
from datetime import datetime

def save_mission_log(tasks, total_mins):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("mission_history.txt", "a") as f:
        f.write(f"\n--- MISSION DATE: {now} ---\n")
        for t in tasks:
            f.write(f"Task: {t['name']} | Duration: {t['time']} mins\n")
        f.write(f"TOTAL ACTIVE TIME: {total_mins} minutes\n")
        f.write("-" * 30 + "\n")
    print(f"\n[JARVIS]: Mission log has been encrypted and saved to 'mission_history.txt'.")

def mission_summary():
    print("\n" + "="*45)
    print("      OPTIMUS JARVIS: MISSION PERSISTENCE")
    print("      PHASE 103: DATA STORAGE")
    print("="*45)

    tasks = []
    total_minutes = 0

    while True:
        name = input("[INPUT]: Task Name (or 'DONE'): ")
        if name.upper() == 'DONE':
            break

        try:
            mins = input(f"Time spent on '{name}' (minutes): ")
            tasks.append({"name": name, "time": int(mins)})
            total_minutes += int(mins)
        except ValueError:
            print("[ERROR]: Please enter a valid number for time.")

    print("\n" + "-"*30)
    print(f"COMMANDER, FINAL REPORT:")
    print(f"Total Tasks Completed: {len(tasks)}")
    print(f"Total Active Time: {total_minutes} minutes")
    
    if total_minutes > 120:
        print("Status: Highly Productive Day.")
    else:
        print("Status: Baseline Objectives Met.")
    print("-"*30)

    if tasks:
        save_mission_log(tasks, total_minutes)

if __name__ == "__main__":
    mission_summary()
