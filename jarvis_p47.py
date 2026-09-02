import time
import os
from gtts import gTTS

def speak(text):
    print(f"[JARVIS]: {text}")
    # आवाज़ वाली फाइल बनाना
    tts = gTTS(text=text, lang='en')
    tts.save("speech.mp3")
    # फाइल को प्ले करना
    os.system("play-audio speech.mp3")

def phase_47_vocal_output():
    print("--- OPTIMUS JARVIS SUPER-FRAME: PHASE 47 ---")
    print("--- [INITIATING PHASE 47: VOCAL OUTPUT MODULE] ---")
    time.sleep(1)
    
    speak("Hello Deepak. Vocal output module is now active. I can now speak to you.")
    
    print("\n✅ Phase 47: Audio Integration Successful.")
    print("✅ Jarvis is now capable of audible communication.")

if __name__ == "__main__":
    phase_47_vocal_output()
