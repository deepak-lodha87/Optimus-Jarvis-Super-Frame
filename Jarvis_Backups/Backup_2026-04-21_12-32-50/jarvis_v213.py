import os
import time

def command_history_logger():
    print("\n" + "="*40)
    print("      JARVIS COMMAND HISTORY PROTOCOL")
    print("="*40)
    
    msg_ask = "Commander Deepak, please enter the command to be logged."
    print(f"\n[JARVIS]: {msg_ask}")
    os.system(f"termux-tts-speak '{msg_ask}'")
    
    user_cmd = input("\n[INPUT]: Command/Instruction: ")
    
    # टाइमस्टैम्प के साथ लॉग फाइल में सेव करना
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] COMMAND: {user_cmd}\n"
    
    try:
        with open("command_log.txt", "a") as log_file:
            log_file.write(log_entry)
        
        success_msg = "Instruction has been synchronized with the history core."
        print(f"\n[JARVIS]: {success_msg}")
        os.system(f"termux-tts-speak '{success_msg}'")
        
    except Exception as e:
        print(f"[ERROR]: Could not update log. {e}")

    # हिस्ट्री देखने का विकल्प
    view = input("\n[JARVIS]: Would you like to view recent history? (y/n): ").lower()
    if view == 'y':
        print("\n" + "-"*30)
        print("      RECENT COMMAND LOGS")
        print("-"*30)
        if os.path.exists("command_log.txt"):
            with open("command_log.txt", "r") as f:
                lines = f.readlines()
                for line in lines[-5:]: # आखिरी 5 कमांड्स दिखाना
                    print(line.strip())
        else:
            print("[EMPTY]: No history found.")
        print("-"*30)

if __name__ == "__main__":
    command_history_logger()
