import os
import shutil
import time

def speak(text):
    print(f"[JARVIS]: {text}")
    os.system(f"termux-tts-speak '{text}'")

def phase_84_health_alert():
    print("--- OPTIMUS JARVIS SUPER-FRAME: PHASE 84 ---")
    print("--- [INITIALIZING STORAGE HEALTH ALERT] ---")
    time.sleep(1)

    # स्टोरेज की जानकारी लेना
    total, used, free = shutil.disk_usage("/sdcard")
    used_percent = (used / total) * 100

    print(f"📊 Current Storage Usage: {used_percent:.2f}%")

    if used_percent > 90:
        msg = "चेतावनी दीपक! आपके फोन की स्टोरेज 90 प्रतिशत से ज्यादा भर चुकी है। कृपया कुछ फाइलें डिलीट करें वरना सिस्टम धीमा हो सकता है।"
        print("⚠️ ALERT: CRITICAL STORAGE LEVEL")
        speak(msg)
    elif used_percent > 70:
        msg = "दीपक, स्टोरेज भरने लगी है। अभी यह " + str(int(used_percent)) + " प्रतिशत है।"
        speak(msg)
    else:
        msg = "सिस्टम हेल्थ सामान्य है। स्टोरेज पर्याप्त मात्रा में उपलब्ध है।"
        speak(msg)

    print("\n✅ Phase 84: Health Alert System Active.")

if __name__ == "__main__":
    phase_84_health_alert()
