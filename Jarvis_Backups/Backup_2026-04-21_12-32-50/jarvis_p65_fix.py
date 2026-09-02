import time
import shutil
import os
from gtts import gTTS

def speak(text, lang_code='hi'):
    print(f"[JARVIS]: {text}")
    try:
        tts = gTTS(text=text, lang=lang_code)
        tts.save("storage_fix.mp3")
        os.system("play-audio storage_fix.mp3")
    except:
        pass

def phase_65_fix():
    print("--- OPTIMUS JARVIS SUPER-FRAME: PHASE 65 (FIX) ---")
    
    # एंड्रॉइड इंटरनल स्टोरेज चेक करने के लिए पाथ
    path = "/sdcard"
    
    try:
        total, used, free = shutil.disk_usage(path)
        
        free_gb = free // (2**30)
        total_gb = total // (2**30)
        used_percent = (used / total) * 100
        
        print(f"📊 Total Storage: {total_gb} GB")
        print(f"💾 Free Space: {free_gb} GB")
        print(f"📈 Usage: {used_percent:.1f}%")
        
        msg = f"दीपक, स्टोरेज एनालिसिस अपडेट कर दिया गया है। आपके फोन में {free_gb} GB जगह खाली है।"
        speak(msg, 'hi')
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("💡 Tip: 'termux-setup-storage' कमांड चलाकर अनुमति दें।")

if __name__ == "__main__":
    phase_65_fix()
