import subprocess
import os
import time

def jarvis_speak(text):
    print(f"\033[1;34m[JARVIS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def listen_command():
    print("\n\033[1;33m[LISTENING]: Please speak your command...\033[0m")
    # Termux voice recognition call
    try:
        result = subprocess.check_output(['termux-speech-to-text']).decode('utf-8').lower()
        print(f"\033[1;32m[USER]:\033[0m {result}")
        return result
    except Exception as e:
        return ""

def voice_interface():
    os.system('clear')
    print("\033[1;36m" + "="*50)
    print("      OPTIMUS JARVIS SUPER-FRAME : PHASE 332")
    print("             VOICE CONTROL ACTIVE")
    print("="*50 + "\033[0m")
    
    jarvis_speak("Voice protocols online. I am listening, Deepak.")
    
    while True:
        command = listen_command()
        
        if "scan" in command:
            jarvis_speak("Initializing deep tactical scan.")
            subprocess.run(['python', 'jarvis_v331_scanner.py'])
        
        elif "status" in command:
            jarvis_speak("System is optimal. Battery and network are stable.")
        
        elif "exit" in command or "stop" in command:
            jarvis_speak("Powering down voice protocols. Goodbye.")
            break
        
        elif command == "":
            print("[SYSTEM]: No voice detected.")
        
        else:
            jarvis_speak("Command not recognized. Standing by.")

if __name__ == "__main__":
    voice_interface()
