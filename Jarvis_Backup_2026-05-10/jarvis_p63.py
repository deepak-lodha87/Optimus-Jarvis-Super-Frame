import time
import os
from gtts import gTTS

def speak(text, lang_code='hi'):
    print(f"[JARVIS]: {text}")
    try:
        tts = gTTS(text=text, lang=lang_code)
        tts.save("sos.mp3")
        os.system("play-audio sos.mp3")
    except:
        pass

def phase_63_sos():
    print("--- OPTIMUS JARVIS SUPER-FRAME: PHASE 63 ---")
    print("--- [INITIALIZING EMERGENCY SOS PROTOCOL] ---")
    time.sleep(1)
    
    trigger = input("🆘 Enter Command (Type SOS for Emergency): ").upper()
    
    if trigger == "SOS":
        print("🚨 ALERT! Emergency Protocol Alpha Activated.")
        print("📡 Tracking Location: Kota, Rajasthan...")
        time.sleep(1.5)
        print("📲 Sending Help Message to Emergency Contacts...")
        
        msg = "दीपक, आपातकालीन स्थिति सक्रिय हो गई है। मैंने आपकी लोकेशन ट्रैक कर ली है और सहायता के लिए संदेश भेज दिया है।"
        speak(msg, 'hi')
        
        # डिवाइस को वाइब्रेट करना
        os.system("termux-vibrate -d 2000")
    else:
        print("🛡️ System Secure. No threats detected.")

    print("\n✅ Phase 63: Emergency SOS Simulation Complete.")

if __name__ == "__main__":
    phase_63_sos()
