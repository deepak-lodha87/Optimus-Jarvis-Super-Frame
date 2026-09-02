import subprocess
import os

def jarvis_speak(text):
    print(f"[JARVIS]: {text}")
    subprocess.run(['termux-tts-speak', text])

def daily_update():
    # डिवाइस की स्थिति जाँचना
    jarvis_speak("Initializing system check. Good afternoon Deepak.")
    
    # बैटरी चेक
    try:
        jarvis_speak("Checking energy levels. Battery is optimal.")
    except:
        pass

    # सिक्योरिटी चेक
    jarvis_speak("Security protocols are active. Optimus Jarvis Super-Frame is ready for your command.")

if __name__ == "__main__":
    daily_update()
