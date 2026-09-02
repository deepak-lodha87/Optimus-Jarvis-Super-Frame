import time
import os
from gtts import gTTS

def speak(text, lang_code='hi'):
    print(f"[JARVIS]: {text}")
    try:
        tts = gTTS(text=text, lang=lang_code)
        tts.save("security_alert.mp3")
        os.system("play-audio security_alert.mp3")
    except:
        pass

def phase_55_security_alarm():
    print("--- OPTIMUS JARVIS SUPER-FRAME: PHASE 55 ---")
    print("--- [INITIALIZING SECURITY ALARM SYSTEM] ---")
    time.sleep(1)
    
    print("⚠️  Monitoring System Access...")
    time.sleep(1.5)
    
    # सिमुलेशन: गलत एक्सेस प्रयास
    print("🚨 [ALERT] Unauthorized access attempt detected!")
    print("🛡️  Activating Defensive Protocols...")
    time.sleep(1)
    
    # अलार्म के लिए बीप साउंड (Termux-API की मदद से)
    os.system("termux-vibrate -d 500")
    
    alert_msg = "चेतावनी! अनधिकृत एक्सेस का पता चला है। सिस्टम अब लॉक किया जा रहा है और आपकी लोकेशन ट्रैक की जा रही है।"
    
    speak(alert_msg, 'hi')
    
    print("\n✅ Phase 55: Security Alarm System Online.")
    print("✅ Jarvis is now acting as a digital sentry.")

if __name__ == "__main__":
    phase_55_security_alarm()
