import time
import os
import sys

def self_destruct_sequence():
    print("\n" + "!"*50)
    alert = "Commander Deepak, Self-Destruct Sequence Initiated."
    print(f"[CRITICAL]: {alert}")
    os.system(f"termux-tts-speak '{alert}'")
    
    for i in range(5, 0, -1):
        print(f"[SYSTEM]: Core destabilizing in {i}...")
        time.sleep(1)
    
    # Final Visual Effect
    print("\n[BOOM]: System Core Purged.")
    print("!"*50 + "\n")
    os.system("termux-tts-speak 'System purged. Goodbye, Commander.'")

def jarvis_main():
    print("\n--- OPTIMUS JARVIS PHASE 184 ---")
    time.sleep(1)
    print("[STATUS]: All systems operational.")
    
    confirm = input("\nEnter Authorization Code or 'SD' for Self-Destruct: ")
    
    if confirm.upper() == 'SD':
        self_destruct_sequence()
    else:
        print("[JARVIS]: Access Granted. Welcome back, Commander.")

if __name__ == "__main__":
    jarvis_main()
