import time
import os
import subprocess

def optimus_speak(text, lang="en"):
    print(f"\033[1;34m[OPTIMUS]:\033[0m {text}")
    # Termux voice engine use karega
    subprocess.run(['termux-tts-speak', '-l', lang, text])

def language_bridge():
    os.system('clear')
    print("\033[1;32m" + "🌐"*30)
    print("      OPTIMUS NEURAL SYSTEMS : MULTI-LANGUAGE BRIDGE (P353)")
    print("🌐"*30 + "\033[0m")
    
    optimus_speak("Neural bridge is active. Calibrating linguistic output.")
    
    print("\n\033[1;33m[SELECT]: 1. English (Professional) | 2. Hindi (Native Support)\033[0m")
    mode = input("\n\033[1;37m[INPUT]: Choose Interface Language: \033[0m")
    
    if mode == '1':
        msg = "The system is now operating in English professional mode."
        optimus_speak(msg, "en")
        print(f"\n\033[1;36m[STATUS]: English Protocol Activated.\033[0m")
    elif mode == '2':
        msg = "Ab Optimus Neural System Hindi mein baat karne ke liye taiyar hai."
        optimus_speak(msg, "hi")
        print(f"\n\033[1;36m[STATUS]: Hindi Protocol Activated.\033[0m")
    else:
        optimus_speak("Invalid selection. Defaulting to English.")

if __name__ == "__main__":
    language_bridge()
