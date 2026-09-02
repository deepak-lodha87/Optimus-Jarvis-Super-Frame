import time
import datetime
import os
from gtts import gTTS

def speak(text, lang_code='hi'):
    print(f"[JARVIS]: {text}")
    try:
        tts = gTTS(text=text, lang=lang_code)
        tts.save("schedule.mp3")
        os.system("play-audio schedule.mp3")
    except:
        pass

def phase_52_scheduler():
    print("--- OPTIMUS JARVIS SUPER-FRAME: PHASE 52 ---")
    print("--- [INITIALIZING TIME & SCHEDULE MODULE] ---")
    time.sleep(1)
    
    # वर्तमान समय प्राप्त करना
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")
    
    print(f"🕒 Current System Time: {current_time}")
    
    # समय के अनुसार ग्रीट करना
    hour = now.hour
    if 5 <= hour < 12:
        greeting = "सुप्रभात दीपक।"
    elif 12 <= hour < 17:
        greeting = "नमस्कार दीपक, दोपहर हो रही है।"
    else:
        greeting = "शुभ संध्या दीपक।"
        
    status_report = f"{greeting} अभी समय {current_time} है। आपका अगला शेड्यूल 'प्रोजेक्ट कोडिंग' के लिए तैयार है।"
    
    speak(status_report, 'hi')
    
    print("\n✅ Phase 52: Time-Management System Online.")
    print("✅ Jarvis can now track schedules and greet you based on time.")

if __name__ == "__main__":
    phase_52_scheduler()
