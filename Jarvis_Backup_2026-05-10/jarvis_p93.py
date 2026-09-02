import os
import time

def speak(text):
    os.system(f"termux-tts-speak '{text}'")

def security_lockdown():
    print("--- OPTIMUS JARVIS SUPER-FRAME: PHASE 93 ---")
    print("--- [INITIALIZING SECURITY LOCKDOWN] ---")
    
    attempts = 3
    master_pass = "stark123"

    while attempts > 0:
        val = input(f"\n🔐 Enter Security Code ({attempts} attempts left): ")
        
        if val == master_pass:
            print("\n🔓 ACCESS GRANTED")
            speak("Welcome back, Deepak. Security scan complete.")
            return
        else:
            attempts -= 1
            print(f"❌ Wrong Password! Warning sent to administrator.")
            speak("Galat password. Kripya dhyan dein.")

    # Agar 3 baar galat password dala to lockdown
    print("\n🛑 [SYSTEM LOCKDOWN ACTIVE]")
    speak("Suraksha kaaranon se system ko lock kiya ja raha hai.")
    os.system("termux-torch off") # Safety feature
    time.sleep(5)
    exit()

if __name__ == "__main__":
    security_lockdown()
