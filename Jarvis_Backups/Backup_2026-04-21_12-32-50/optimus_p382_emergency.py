import time
import os
import subprocess

def optimus_speak(text):
    print(f"\033[1;34m[OPTIMUS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def emergency_lockdown_protocol():
    os.system('clear')
    print("\033[1;31m" + "🚨"*30)
    print("      OPTIMUS NEURAL SYSTEMS : EMERGENCY PROTOCOL (P382)")
    print("🚨"*30 + "\033[0m")
    
    optimus_speak("Warning. Critical security breach detected. Initiating emergency lockdown.")
    
    # Emergency Actions List
    actions = [
        "Disconnecting Mesh Network Nodes (P376)",
        "Encrypting Local Log Archives (P365)",
        "Shutting Down Neural Decision Engine (P364)",
        "Clearing Active Session Cache (P370)",
        "Activating Stealth Mode Perimeter"
    ]
    
    print("\n\033[1;33m[EXECUTING]: Counter-Measures Active...\033[0m")
    time.sleep(1.5)
    
    for action in actions:
        print(f"\033[1;31m[ACTION]:\033[0m {action}...")
        time.sleep(0.6)
    
    print("-" * 55)
    print(f"\033[1;32m[STATUS]: SYSTEM ENCRYPTED & LOCKED.\033[0m")
    optimus_speak("All neural pathways have been purged. System is now in cold-storage mode. Manual hardware reset required.")

if __name__ == "__main__":
    confirm = input("\033[1;31m[CRITICAL]: Trigger Emergency Wipe? (yes/no): \033[0m").lower()
    if confirm == "yes":
        emergency_lockdown_protocol()
    else:
        print("\033[1;32m[CANCELLED]: Aborting emergency protocol.\033[0m")
