import time
import os
import getpass
from gtts import gTTS

def speak(text, lang_code='hi'):
    print(f"[JARVIS]: {text}")
    try:
        tts = gTTS(text=text, lang=lang_code)
        tts.save("vault.mp3")
        os.system("play-audio vault.mp3")
    except:
        pass

def phase_61_vault():
    print("--- OPTIMUS JARVIS SUPER-FRAME: PHASE 61 ---")
    print("--- [INITIALIZING SECRET VAULT PROTECTION] ---")
    time.sleep(1)
    
    password = "MARS" # यह आपका गुप्त पासवर्ड है
    
    print("🔒 JARVIS SECURE VAULT")
    user_input = input("🔑 Please enter the Access Key: ")
    
    if user_input == password:
        print("🔓 Access Granted!")
        msg = "एक्सेस मिल गया है। आपका सीक्रेट वॉल्ट अब अनलॉक है।"
        speak(msg, 'hi')
        print("📂 [Secret Files]: project_blueprints.txt, personal_logs.db")
    else:
        print("❌ Access Denied! Security protocols activated.")
        msg = "चेतावनी! गलत पासवर्ड। सुरक्षा प्रोटोकॉल सक्रिय कर दिए गए हैं।"
        speak(msg, 'hi')
        os.system("termux-vibrate -d 1000")

    print("\n✅ Phase 61: Secret Vault System Integrated.")
    print("✅ Jarvis is now securing your sensitive data.")

if __name__ == "__main__":
    phase_61_vault()
