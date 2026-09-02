import time
import datetime
import os
from gtts import gTTS

def speak(text, lang_code='hi'):
    print(f"[JARVIS]: {text}")
    try:
        tts = gTTS(text=text, lang=lang_code)
        tts.save("night.mp3")
        os.system("play-audio night.mp3")
    except:
        pass

def phase_64_night_mode():
    print("--- OPTIMUS JARVIS SUPER-FRAME: PHASE 64 ---")
    print("--- [INITIALIZING SMART NIGHT MODE] ---")
    time.sleep(1)
    
    current_hour = datetime.datetime.now().hour
    
    # रात 10 बजे (22) से सुबह 6 बजे तक का समय
    if current_hour >= 22 or current_hour < 6:
        print("🌙 Night Mode Condition: ACTIVE")
        msg = "दीपक, काफी रात हो गई है। आंखों की सुरक्षा के लिए मैंने नाइट मोड का सुझाव सक्रिय कर दिया है। कृपया स्क्रीन की ब्राइटनेस कम कर लें।"
        speak(msg, 'hi')
    else:
        print("☀️ Day Mode Condition: ACTIVE")
        msg = "सिस्टम सामान्य मोड में है। दिन की रोशनी के अनुसार ब्राइटनेस ऑप्टिमाइज़्ड है।"
        speak(msg, 'hi')

    print("\n✅ Phase 64: Smart Night Mode Analysis Complete.")

if __name__ == "__main__":
    phase_64_night_mode()
