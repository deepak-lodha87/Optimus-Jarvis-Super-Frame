import time
import os
import subprocess

def optimus_speak(text):
    print(f"\033[1;34m[OPTIMUS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def security_protocol():
    os.system('clear')
    print("\033[1;31m" + "="*50)
    print("      OPTIMUS NEURAL SYSTEMS : DEFENSE CORE (P344)")
    print("="*50 + "\033[0m")
    
    optimus_speak("Perimeter defense active. Monitoring for unauthorized access.")
    
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        print(f"\n\033[1;33m[ALERT]: Unauthorized touch detected. Confirm Identity.\033[0m")
        key = input("\033[1;33m[SECURITY]: Enter System Access Key: \033[0m")
        
        if key == "1010":
            optimus_speak("Access verified. Defense protocols standby.")
            print("\033[1;32m[STATUS]: SYSTEM SECURE.\033[0m")
            return 0
        else:
            attempts += 1
            optimus_speak(f"Incorrect access key. Attempt {attempts} of {max_attempts}.")
            print(f"\033[1;31m[WARNING]: {max_attempts - attempts} attempts remaining.\033[0m")
            
    # System Lockdown Trigger
    os.system('termux-vibrate -d 1000') # Mobile vibrate karega
    optimus_speak("Maximum attempts reached. Initiating system lockdown and capturing intruder logs.")
    print("\033[1;31;47m !!! SYSTEM LOCKDOWN ENGAGED !!! \033[0m")
    # Yahan hum future mein camera photo click function add karenge

if __name__ == "__main__":
    security_protocol()
