import os
import time

def speak(text):
    print(f"[JARVIS]: {text}")
    os.system(f"termux-tts-speak '{text}'")

def phase_82_speed_test():
    print("--- OPTIMUS JARVIS SUPER-FRAME: PHASE 82 ---")
    print("--- [INITIALIZING NETWORK SPEED ANALYTICS] ---")
    time.sleep(1)

    speak("दीपक, मैं आपकी इंटरनेट कनेक्टिविटी की जांच कर रहा हूँ। कृपया प्रतीक्षा करें।")
    
    print("\n📡 Testing Network Speed (Connecting to nearest server)...")
    # यह कमांड इंटरनेट स्पीड चेक करेगी
    result = os.popen("speedtest-cli --simple").read()

    if result:
        print("\n===============================")
        print(result)
        print("===============================")
        speak("स्पीड टेस्ट पूरा हुआ। आपका नेटवर्क स्टेटस अभी स्क्रीन पर है।")
    else:
        speak("माफ़ कीजिये दीपक, इंटरनेट कनेक्शन नहीं मिल रहा है।")

    print("\n✅ Phase 82: Speed Analytics Operational.")

if __name__ == "__main__":
    phase_82_speed_test()
