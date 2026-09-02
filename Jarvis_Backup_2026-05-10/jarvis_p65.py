import time
import shutil
import os
from gtts import gTTS

def speak(text, lang_code='hi'):
    print(f"[JARVIS]: {text}")
    try:
        tts = gTTS(text=text, lang=lang_code)
        tts.save("storage.mp3")
        os.system("play-audio storage.mp3")
    except:
        pass

def phase_65_storage_monitor():
    print("--- OPTIMUS JARVIS SUPER-FRAME: PHASE 65 ---")
    print("--- [INITIALIZING STORAGE HEALTH MONITOR] ---")
    time.sleep(1)
    
    # स्टोरेज की जानकारी प्राप्त करना
    total, used, free = shutil.disk_usage("/")
    
    free_gb = free // (2**30)
    used_percent = (used / total) * 100
    
    print(f"📊 Storage Used: {used_percent:.1f}%")
    print(f"💾 Free Space: {free_gb} GB")
    
    if used_percent > 80:
        msg = f"दीपक, आपके सिस्टम की अस्सी प्रतिशत से ज्यादा स्टोरेज भर चुकी है। केवल {free_gb} जीबी जगह बची है। क्या मैं फालतू फाइलों को हटाने की प्रक्रिया शुरू करूँ?"
    else:
        msg = f"स्टोरेज की स्थिति सामान्य है। आपके पास {free_gb} जीबी फ्री स्पेस उपलब्ध है।"
    
    speak(msg, 'hi')
    
    print("\n✅ Phase 65: Storage Health Monitor Integrated.")

if __name__ == "__main__":
    phase_65_storage_monitor()
