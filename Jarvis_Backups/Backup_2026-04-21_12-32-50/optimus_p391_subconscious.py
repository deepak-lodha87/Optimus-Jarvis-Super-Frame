import os
import time
import subprocess
import threading

def optimus_speak(text):
    print(f"\033[1;34m[OPTIMUS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def background_task():
    # Background mein hone wala kaam
    for i in range(3):
        time.sleep(1)
        print(f"\033[1;30m[BG-THREAD]: Indexing Neural Nodes... {i+1}/3\033[0m")

def subconscious_init():
    os.system('clear')
    print("\033[1;35m" + "🧠"*30)
    print("      OPTIMUS NEURAL SYSTEMS : SUBCONSCIOUS (P391)")
    print("🧠"*30 + "\033[0m")
    
    optimus_speak("Initializing subconscious processing. Running background threads.")
    
    # Starting a background thread
    bg_thread = threading.Thread(target=background_task)
    bg_thread.start()
    
    active_tasks = ["Log Rotation", "Memory Garbage Collection", "Signal Filtering"]
    
    for task in active_tasks:
        print(f"Running Task: {task:.<25} [ \033[1;32mSTABLE\033[0m ]")
        time.sleep(0.6)
    
    bg_thread.join() # Wait for background task to finish
    print("-" * 55)
    optimus_speak("Subconscious threads are synchronized with the main frame.")
    print("\033[1;35m[SYSTEM]: MULTI-THREADING ACTIVE\033[0m")

if __name__ == "__main__":
    subconscious_init()
