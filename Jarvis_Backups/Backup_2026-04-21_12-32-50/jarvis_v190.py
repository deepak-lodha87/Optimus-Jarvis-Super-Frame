import os
import time

def wake_up_protocol():
    print("\n[STBY]: System is in Sleep Mode...")
    print("[HINT]: Type 'Wake up' to activate Jarvis.")
    
    while True:
        user_input = input(">> ").lower()
        if "wake up" in user_input or "hello jarvis" in user_input:
            msg = "Systems online. Good evening, Commander Deepak. How can I help you today?"
            print(f"\n[JARVIS]: {msg}")
            os.system(f"termux-tts-speak '{msg}'")
            break
        else:
            print("[SYSTEM]: Unauthorized input. Standing by...")

def jarvis_main():
    print("\n" + "="*50)
    print("|    JARVIS PHASE 190: WAKE-WORD DETECTION    |")
    print("="*50)
    
    wake_up_protocol()
    
    print("\n[STATUS]: Optimus Jarvis Super-Frame is now fully active.")
    print("="*50)

if __name__ == "__main__":
    jarvis_main()
