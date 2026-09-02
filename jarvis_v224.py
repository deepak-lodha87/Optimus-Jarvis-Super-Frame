import os
import time

def task_reminder_protocol():
    print("\n" + "="*40)
    print("      JARVIS TASK REMINDER SYSTEM")
    print("="*40)
    
    msg_ask = "Commander Deepak, what is the task and in how many minutes should I remind you?"
    print(f"\n[JARVIS]: {msg_ask}")
    os.system(f"termux-tts-speak '{msg_ask}'")
    
    task_name = input("\n[INPUT]: Enter Task: ")
    try:
        reminder_time = int(input("[INPUT]: Minutes from now: "))
        
        start_msg = f"Reminder set for '{task_name}' in {reminder_time} minutes, Commander."
        print(f"\n[JARVIS]: {start_msg}")
        os.system(f"termux-tts-speak '{start_msg}'")
        
        # बैकग्राउंड में प्रतीक्षा करने के लिए सिमुलेशन
        time.sleep(reminder_time * 60)
        
        alert_msg = f"Commander Deepak, ALERT! It is time for: {task_name}. Please check your schedule."
        print(f"\n[!!! ALERT !!!]: {alert_msg}")
        os.system(f"termux-tts-speak '{alert_msg}'")
        
    except ValueError:
        error = "Commander, please provide a valid number for minutes."
        print(f"\n[ERROR]: {error}")
        os.system(f"termux-tts-speak '{error}'")

    print("\n" + "="*40)

if __name__ == "__main__":
    task_reminder_protocol()
