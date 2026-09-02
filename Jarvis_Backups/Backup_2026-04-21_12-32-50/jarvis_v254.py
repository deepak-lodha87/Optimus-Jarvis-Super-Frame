import os
import time

def task_prioritizer():
    print("\n" + "="*45)
    print("      JARVIS TASK PRIORITIZER")
    print("="*45)
    
    tasks = []
    print("[INPUT]: Enter your tasks for today (Type 'DONE' to finish)")
    
    while True:
        task_name = input("Task Name: ")
        if task_name.upper() == 'DONE': break
        
        priority = input("Priority (1: Critical, 2: High, 3: Normal): ")
        tasks.append({"name": task_name, "level": priority})

    # प्राथमिकता के आधार पर सॉर्ट करना
    tasks.sort(key=lambda x: x['level'])

    msg_init = f"Commander Deepak, I have organized your schedule. You have {len(tasks)} tasks prioritized."
    print(f"\n[JARVIS]: {msg_init}")
    os.system(f"termux-tts-speak '{msg_init}'")

    print("\n[PRIORITIZED SCHEDULE]:")
    for t in tasks:
        level_name = "CRITICAL" if t['level'] == '1' else "HIGH" if t['level'] == '2' else "NORMAL"
        print(f"  [{level_name}] --> {t['name']}")
        
    final_rem = "Focus on the Critical tasks first to ensure mission success."
    os.system(f"termux-tts-speak '{final_rem}'")
    print("\n" + "="*45)

if __name__ ==

cat << 'EOF' > jarvis_v254.py
import os
import time

def task_prioritizer():
    print("\n" + "="*45)
    print("      JARVIS TASK PRIORITIZER")
    print("="*45)
    
    tasks = []
    print("[INPUT]: Enter your tasks for today (Type 'DONE' to finish)")
    
    while True:
        task_name = input("Task Name: ")
        if task_name.upper() == 'DONE': break
        
        priority = input("Priority (1: Critical, 2: High, 3: Normal): ")
        tasks.append({"name": task_name, "level": priority})

    # प्राथमिकता के आधार पर सॉर्ट करना
    tasks.sort(key=lambda x: x['level'])

    msg_init = f"Commander Deepak, I have organized your schedule. You have {len(tasks)} tasks prioritized."
    print(f"\n[JARVIS]: {msg_init}")
    os.system(f"termux-tts-speak '{msg_init}'")

    print("\n[PRIORITIZED SCHEDULE]:")
    for t in tasks:
        level_name = "CRITICAL" if t['level'] == '1' else "HIGH" if t['level'] == '2' else "NORMAL"
        print(f"  [{level_name}] --> {t['name']}")
        
    final_rem = "Focus on the Critical tasks first to ensure mission success."
    os.system(f"termux-tts-speak '{final_rem}'")
    print("\n" + "="*45)

if __name__ == "__main__":
    task_prioritizer()
