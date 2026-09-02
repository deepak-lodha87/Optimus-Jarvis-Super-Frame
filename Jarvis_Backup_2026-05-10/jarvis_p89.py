import os
import time
from datetime import datetime

def speak(text):
    print(f"[JARVIS]: {text}")
    os.system(f"termux-tts-speak '{text}'")

def voice_reminder():
    print("--- OPTIMUS JARVIS SUPER-FRAME: PHASE 89 ---")
    print("--- [INITIALIZING VOICE REMINDER MODULE] ---")
    
    task = input("📝 Kya yaad dilana hai? (e.g., Coding practice): ")
    rem_time = input("⏰ Kis samay? (Format HH:MM in 24hr, e.g., 21:00): ")

    speak(f"Theek hai Deepak, main aapko {rem_time} baje {task} ke liye yaad dila dunga.")

    while True:
        now = datetime.now().strftime("%H:%M")
        if now == rem_time:
            print(f"\n🔔 REMINDER: {task}")
            for i in range(3): # 3 baar repeat karega
                speak(f"Deepak, dhyan dein. Yeh aapke {task} ka samay hai.")
                time.sleep(2)
            break
        time.sleep(30) # Har 30 second mein check karega

    print("\n✅ Phase 89: Reminder Executed & Closed.")

if __name__ == "__main__":
    voice_reminder()
