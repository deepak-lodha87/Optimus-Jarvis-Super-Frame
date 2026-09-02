import os
import time
from datetime import datetime

def adaptive_greeting():
    # वर्तमान समय प्राप्त करना
    current_hour = datetime.now().hour
    
    if 5 <= current_hour < 12:
        greet = "Good morning, Commander Deepak. Systems are warming up for the day."
    elif 12 <= current_hour < 17:
        greet = "Good afternoon, Commander. All sectors are operational under the sun."
    elif 17 <= current_hour < 21:
        greet = "Good evening, Sir. The sun is setting, switching to night-vision mode."
    else:
        greet = "It is late, Commander. Systems are in low-power stealth mode for the night."

    print(f"\n[JARVIS]: {greet}")
    os.system(f"termux-tts-speak '{greet}'")

def jarvis_main():
    print("\n" + "="*50)
    print("|    JARVIS PHASE 187: ADAPTIVE GREETING    |")
    print("="*50)
    adaptive_greeting()
    time.sleep(1)
    print("\n[SYSTEM]: Ready for your command.")
    print("="*50)

if __name__ == "__main__":
    jarvis_main()
