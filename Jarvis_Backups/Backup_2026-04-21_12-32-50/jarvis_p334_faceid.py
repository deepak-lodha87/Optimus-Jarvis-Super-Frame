import subprocess
import os

def jarvis_speak(text):
    print(f"\033[1;34m[JARVIS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def biometric_unlock():
    os.system('clear')
    print("\033[1;31m[SECURITY]: BIOMETRIC HARDWARE NOT DETECTED\033[0m")
    jarvis_speak("Biometric hardware failure. Switching to manual override passcode.")
    
    # Bypass code for Deepak
    passcode = input("\033[1;33m[SECURITY]: Enter Master Passcode: \033[0m")
    
    if passcode == "1010":
        jarvis_speak("Passcode verified. Welcome back, Deepak.")
        return 0
    else:
        jarvis_speak("Access denied. Lockdown engaged.")
        return 1

if __name__ == "__main__":
    if biometric_unlock() == 0:
        # Success trigger for next phase
        exit(0)
    else:
        exit(1)
