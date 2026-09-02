import time
import os
import subprocess
import getpass

def optimus_speak(text):
    print(f"\033[1;34m[OPTIMUS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def final_access_gate():
    os.system('clear')
    print("\033[1;31m" + "🔐"*30)
    print("      OPTIMUS NEURAL SYSTEMS : FINAL ACCESS GATE (P371)")
    print("🔐"*30 + "\033[0m")
    
    optimus_speak("System is locked. Initiating identity verification protocol.")
    
    # Authorized Credentials (In a real system, these would be hashed)
    ADMIN_PIN = "1234" # Aap ise change kar sakte hain
    
    print("\n\033[1;33m[CHALLENGE]: Please provide Authorization PIN:\033[0m")
    user_input = getpass.getpass("ENTER PIN: ") # Hidden input for security
    
    print("\n\033[1;36m[VALIDATING]: Checking neural signature and credentials...\033[0m")
    time.sleep(2)
    
    if user_input == ADMIN_PIN:
        print(f"\n\033[1;32m[SUCCESS]: Identity Confirmed. Neural pathways open.\033[0m")
        optimus_speak("Access granted. Welcome back, Administrator.")
        # Launching the Master Dashboard (Phase 360)
        os.system('python optimus_v2_core.py')
    else:
        print(f"\n\033[1;31m[FAILED]: Invalid Credentials. Security Lockdown Initiated.\033[0m")
        optimus_speak("Authentication failed. Unauthorized access attempt recorded in logs.")
        # Triggering the Log Archive from Phase 365
        from optimus_p365_logs import write_neural_log
        write_neural_log("Unauthorized Access Attempt", "BLOCKED")

if __name__ == "__main__":
    final_access_gate()
