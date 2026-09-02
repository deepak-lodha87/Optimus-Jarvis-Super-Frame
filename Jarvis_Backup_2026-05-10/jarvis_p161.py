import os
import time

def biometric_voice_lock():
    print("\n" + "="*50)
    print("|    JARVIS PHASE 161: BIOMETRIC VOICE LOCK     |")
    print("="*50)

    # Authorized Commander Name
    commander = "DEEPAK"
    
    print("\n[SYSTEM]: Waiting for voice authorization...")
    # Simulating voice input
    voice_input = input("[INPUT]: Speak Command (Identify yourself): ").upper().strip()
    
    print("[LOG]: Analyzing vocal frequency and patterns...")
    time.sleep(1.5)
    
    if voice_input == commander:
        status = "ACCESS GRANTED"
        msg = f"Voice match confirmed. Welcome back, Commander {commander}. System is now fully unlocked."
    else:
        status = "ACCESS DENIED"
        msg = "Vocal patterns do not match. System remaining in lockdown mode."

    print(f"\n[RESULT]: {status}")
    print(f"[JARVIS]: {msg}")
    os.system(f"termux-tts-speak '{msg}'")

    if status == "ACCESS GRANTED":
        print("\n[STATUS]: Biometric shield deactivated. Core is open.")
    else:
        print("\n[ALERT]: Unauthorized attempt logged.")
        
    print("="*50)

if __name__ == "__main__":
    biometric_voice_lock()
