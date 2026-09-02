import os
import time

def memory_bank_protocol():
    print("\n[SYSTEM]: Accessing Neural Memory Bank...")
    
    action = input("\n[JARVIS]: Would you like to (S)ave a note or (V)iew saved notes? ").lower()
    
    if action == 's':
        note = input("[JARVIS]: What should I remember, Commander? ")
        timestamp = time.strftime("%Y-%m-%d %H:%M")
        with open("jarvis_memory.txt", "a") as mem:
            mem.write(f"[{timestamp}] - {note}\n")
        print("[STATUS]: Note secured in memory bank.")
        os.system("termux-tts-speak 'Note secured in memory bank.'")
        
    elif action == 'v':
        print("\n" + "-"*30)
        print("      SAVED MEMORIES")
        print("-"*30)
        if os.path.exists("jarvis_memory.txt"):
            with open("jarvis_memory.txt", "r") as mem:
                print(mem.read())
        else:
            print("[EMPTY]: No memories found.")
        print("-"*30)
    else:
        print("[ERROR]: Invalid protocol selection.")

def jarvis_main():
    print("\n" + "="*50)
    print("|    JARVIS PHASE 203: QUICK NOTES & MEMORY    |")
    print("="*50)
    
    memory_bank_protocol()
    
    print("\n[STATUS]: Memory cycle standby.")
    print("="*50)

if __name__ == "__main__":
    jarvis_main()
