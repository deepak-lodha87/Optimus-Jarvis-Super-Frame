import json
import os
import subprocess
import datetime

MEMORY_FILE = "jarvis_memory.json"

def jarvis_speak(text):
    print(f"\033[1;34m[JARVIS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, 'r') as f:
            return json.load(f)
    return {"user_name": "Deepak", "projects": {}, "last_interaction": ""}

def save_memory(memory):
    with open(MEMORY_FILE, 'w') as f:
        json.dump(memory, f, indent=4)

def neural_memory_engine():
    os.system('clear')
    memory = load_memory()
    
    print("\033[1;36m" + "="*50)
    print("      OPTIMUS JARVIS : NEURAL MEMORY (P339)")
    print("="*50 + "\033[0m")
    
    # Last interaction recall
    if memory["last_interaction"]:
        print(f"\033[1;32m[RECALL]: Last session was on {memory['last_interaction']}\033[0m")
    
    jarvis_speak("Memory protocols active. Is there any project update I should archive?")
    
    update = input("\033[1;33m[INPUT]: Update Jarvis (e.g., Drone Phase 1 complete): \033[0m")
    
    if update:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        project_name = update.split()[0] # Pehla word project name maan lega
        memory["projects"][project_name] = {"status": update, "date": timestamp}
        memory["last_interaction"] = timestamp
        
        save_memory(memory)
        jarvis_speak("Information successfully archived in the neural core.")
        print(f"\n\033[1;32m[SAVED]: {update}\033[0m")
    
    # Display current memory
    print("\n\033[1;35m--- CURRENT ACTIVE MEMORIES ---\033[0m")
    for proj, details in memory["projects"].items():
        print(f"| Project: {proj} | Status: {details['status']} | Date: {details['date']}")

if __name__ == "__main__":
    neural_memory_engine()
