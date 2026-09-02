import time
import os
from gtts import gTTS

def speak(text, lang_code='hi'):
    print(f"[JARVIS]: {text}")
    try:
        tts = gTTS(text=text, lang=lang_code)
        tts.save("wake.mp3")
        os.system("play-audio wake.mp3")
    except:
        pass

def phase_62_wake_word():
    print("--- OPTIMUS JARVIS SUPER-FRAME: PHASE 62 ---")
    print("--- [INITIALIZING WAKE-WORD DETECTION] ---")
    time.sleep(1)
    
    wake_word = "WAKE UP"
    print(f"🛰️  Jarvis is in 'Passive Listening' mode...")
    print("💡 Tip: Type 'WAKE UP' to activate the system.")
    
    user_input = input("🎤 User: ").upper()
    
    if wake_word in user_input:
        print("⚡ Signal Detected! Powering up core systems...")
        time.sleep(1)
        msg = "प्रोजेक्ट ऑप्टिमस ऑनलाइन। नमस्कार दीपक, मैं आपके आदेश का इंतज़ार कर रहा हूँ।"
        speak(msg, 'hi')
    else:
        print("💤 System remaining in Standby Mode.")

    print("\n✅ Phase 62: Wake-Word Detection Module Online.")
    print("✅ Jarvis can now be remotely activated.")

if __name__ == "__main__":
    phase_62_wake_word()
