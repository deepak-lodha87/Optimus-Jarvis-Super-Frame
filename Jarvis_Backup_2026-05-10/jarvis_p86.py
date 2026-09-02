import os
import time

def speak(text):
    print(f"[JARVIS]: {text}")
    os.system(f"termux-tts-speak '{text}'")

def battery_alert_protocol():
    print("--- OPTIMUS JARVIS SUPER-FRAME: PHASE 86 ---")
    print("--- [INITIALIZING BATTERY MONITOR] ---")
    time.sleep(1)

    # बैटरी की जानकारी प्राप्त करना
    battery_info = os.popen("termux-battery-status").read()
    
    # बैटरी लेवल निकालना (अगर Termux:API इंस्टॉल है)
    try:
        import json
        data = json.loads(battery_info)
        level = data['percentage']
        status = data['status']
        
        print(f"🔋 Battery Level: {level}%")
        print(f"⚡ Status: {status}")

        if level <= 20 and status != "CHARGING":
            # Red UI इफेक्ट (ANSI Color Code for Red)
            print("\033[91m" + "!"*40)
            print("   CRITICAL WARNING: BATTERY LOW")
            print("!"*40 + "\033[0m")
            
            msg = f"चेतावनी दीपक! सिस्टम की ऊर्जा कम हो रही है। बैटरी केवल {level} प्रतिशत बची है। कृपया चार्जर कनेक्ट करें।"
            speak(msg)
        else:
            msg = f"दीपक, पावर लेवल पर्याप्त है। सिस्टम स्थिरता के साथ काम कर रहा है।"
            speak(msg)
            
    except:
        print("⚠️ त्रुटि: Termux:API बैटरी डेटा नहीं पढ़ पा रहा है।")

    print("\n✅ Phase 86: Battery Alert Protocol Active.")

if __name__ == "__main__":
    battery_alert_protocol()
