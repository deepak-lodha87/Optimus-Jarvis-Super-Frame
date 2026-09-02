import os
import time

def schedule_reminder_protocol():
    print("\n[SYSTEM]: Accessing Task Matrix and Schedule...")
    time.sleep(1)
    
    # यहाँ आप अपनी महत्वपूर्ण डेडलाइन्स लिख सकते हैं
    tasks = {
        "Final Year Project": "2026-04-10",
        "Exam Preparation": "Daily Review",
        "Code Backup": "Every Sunday"
    }
    
    print("\n" + "-"*30)
    print("      PENDING DEADLINES")
    print("-"*30)
    
    for task, deadline in tasks.items():
        print(f" -> {task}: [DEADLINE: {deadline}]")
        time.sleep(0.5)
    
    msg = "Commander Deepak, your schedule is synchronized. Remember to focus on your project deadlines."
    print(f"\n[JARVIS]: {msg}")
    os.system(f"termux-tts-speak '{msg}'")
    print("-"*30)

def jarvis_main():
    print("\n" + "="*50)
    print("|    JARVIS

cat << 'EOF' > jarvis_v202.py
import os
import time

def schedule_reminder_protocol():
    print("\n[SYSTEM]: Accessing Task Matrix and Schedule...")
    time.sleep(1)
    
    # आपकी महत्वपूर्ण डेडलाइन्स
    tasks = {
        "Final Year Project": "2026-04-10",
        "Exam Preparation": "Daily Review",
        "Code Backup": "Every Sunday"
    }
    
    print("\n" + "-"*30)
    print("      PENDING DEADLINES")
    print("-"*30)
    
    for task, deadline in tasks.items():
        print(f" -> {task}: [DEADLINE: {deadline}]")
        time.sleep(0.5)
    
    msg = "Commander Deepak, your schedule is synchronized. Remember to focus on your project deadlines."
    print(f"\n[JARVIS]: {msg}")
    os.system(f"termux-tts-speak '{msg}'")
    print("-"*30)

def jarvis_main():
    print("\n" + "="*50)
    print("|    JARVIS PHASE 202: SCHEDULE REMINDER    |")
    print("="*50)
    
    schedule_reminder_protocol()
    
    print("\n[STATUS]: Task matrix is online.")
    print("="*50)

if __name__ == "__main__":
    jarvis_main()
