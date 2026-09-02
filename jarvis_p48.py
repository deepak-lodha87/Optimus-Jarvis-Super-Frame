import time
import os
from gtts import gTTS

def speak(text, lang_code='hi'):
    print(f"[JARVIS]: {text}")
    try:
        tts = gTTS(text=text, lang=lang_code)
        tts.save("response.mp3")
        os.system("play-audio response.mp3")
    except Exception as e:
        print(f"Error: {e}")

def phase_48_multilingual():
    print("--- OPTIMUS JARVIS SUPER-FRAME: PHASE 48 ---")
    print("--- [INITIATING PHASE 48: MULTI-LANGUAGE SYSTEM] ---")
    time.sleep(1)
    
    # हिंदी रिस्पांस
    speak("नमस्ते दीपक। अब मैं हिंदी और अंग्रेजी दोनों भाषाओं में आपसे बात कर सकता हूँ।", 'hi')
    time.sleep(2)
    
    # English Response
    speak("System is now multi-lingual. Ready for the next command.", 'en')
    
    print("\n✅ Phase 48: Multi-Language Support Integrated.")
    print("✅ Jarvis is now more communicative.")

if __name__ == "__main__":
    phase_48_multilingual()
