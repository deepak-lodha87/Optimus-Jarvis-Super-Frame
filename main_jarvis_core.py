import os
import subprocess
import time

def jarvis_speak(text):
    print(f"\033[1;34m[JARVIS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def main_system_boot():
    os.system('clear')
    print("\033[1;36m" + "="*50)
    print("      OPTIMUS JARVIS SUPER-FRAME : PHASE 335")
    print("                MASTER CORE SYSTEM")
    print("="*50 + "\033[0m")
    
    jarvis_speak("Initializing Master Core. Systems are warming up.")
    time.sleep(1)

    # Step 1: Security Check (Face ID)
    print("\n\033[1;33m[STEP 1]: Biometric Authentication...\033[0m")
    # Yahan hum pichhle Phase 334 file ko call karenge
    auth_result = os.system('python jarvis_p334_faceid.py')

    # Step 2: Protocol Execution (Agar Face ID pass ho gaya)
    if auth_result == 0:
        jarvis_speak("Security check passed. Deep scanning and voice protocols are now standby.")
        print("\033[1;32m[SYSTEM]: CORE IS FULLY FUNCTIONAL.\033[0m")
        
        # Aap chahein toh yahan seedha Voice ya Gesture file jor sakte hain
        # os.system('python jarvis_voice_control.py')
    else:
        print("\033[1;31m[ERROR]: System Boot Failed. Unauthorized User.\033[0m")
        jarvis_speak("System boot failed. Please verify your identity.")

if __name__ == "__main__":
    main_system_boot()
