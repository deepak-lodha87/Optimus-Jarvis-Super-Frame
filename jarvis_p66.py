import datetime
import random
import os
import time
from gtts import gTTS

def speak(text, lang_code='hi'):
    print(f"[JARVIS]: {text}")
    try:
        tts = gTTS(text=text, lang=lang_code)
        tts.save("greet.mp3")
        os.system("play-audio greet.mp3")
    except:
        pass

def phase_66_greeting():
    print("--- OPTIMUS JARVIS SUPER-FRAME: PHASE 66 ---")
    print("--- [INITIALIZING DYNAMIC GREETING ENGINE] ---")
    time.sleep(1)

    hour = datetime.datetime.now().hour
    if hour < 12:
        wish = "सुप्रभात"
    elif 12 <= hour < 18:
        wish = "नमस्कार"
    else:
        wish = "शुभ संध्या"

    # अलग-अलग स्टाइल के मैसेज
    styles = [
        f"{wish} दीपक, सिस्टम पूरी तरह सक्रिय है। आज हम किस प्रोजेक्ट पर काम करेंगे?",
        f"{wish} दीपक, आपकी वापसी का स्वागत है। ऑप्टिमस जार्विस आपकी सेवा में हाजिर है।",
        f"प्रणाम दीपक, सभी कोर मॉड्यूल्स ऑनलाइन हैं। मैं आपके अगले आदेश का इंतज़ार कर रहा हूँ।"
    ]

    chosen_greet = random.choice(styles)
    speak(chosen_greet, 'hi')

    print("\n✅ Phase 66: Dynamic Greeting System Online.")

if __name__ == "__main__":
    phase_66_greeting()
