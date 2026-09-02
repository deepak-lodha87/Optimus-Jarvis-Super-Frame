import os
import time
from datetime import datetime

def task_manager():
    print("\n" + "="*45)
    print("      OPTIMUS JARVIS SUPER-FRAME")
    print("      PHASE 101: TASK EXECUTION")
    print("="*45)

    tasks = []
    print("[INPUT]: Commander Deepak, define your mission objectives (Type 'DONE' to finish)")

    while True:
        task_name = input("Objective: ")
        if task_name.upper() == 'DONE':
            break
        
        priority = input("Priority Level (1: Critical, 2: High, 3: Normal): ")
        duration = input("Estimated Time (minutes): ")
        tasks.append({"name": task_name, "level": priority, "time": duration})

    # प्राथमिकता के आधार पर व्यवस्थित करना
    tasks.sort(key=lambda x: x['level'])

    print(f"\n[JARVIS]: Mission strategy updated. Starting execution sequence...")
    
    for t in tasks:
        print(f"\n>>> CURRENT TASK: {t['name']} [Level {t['level']}]")
        confirm = input("Press ENTER to start the timer or 'S' to skip: ")
        
        if confirm.upper() != 'S':
            minutes = int(t['time'])
            print(f"Timer set for {minutes} minutes. Stay focused, Commander.")
            # समय की बचत के लिए यहाँ हम सिर्फ सेकंड्स में दिखा रहे हैं, 
            # असली इस्तेमाल में (minutes * 60) करें।
            time.sleep(2) 
            print(f"[ALERT]: Time's up for '{t['name']}'. Task completed?")
            input("Press ENTER to proceed to the next objective.")

    print("\n" + "="*45)
    print("      ALL OBJECTIVES CLEARED. STANDBY.")
    print("="*45)

if __name__ == "__main__":
    task_manager()
