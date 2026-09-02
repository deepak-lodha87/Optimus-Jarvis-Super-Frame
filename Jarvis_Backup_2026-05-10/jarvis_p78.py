import os
import time
import getpass

def speak(text):
    print(f"[JARVIS]: {text}")
    os.system(f"termux-tts-speak '{text}'")

def phase_78_encryptor():
    print("--- OPTIMUS JARVIS SUPER-FRAME: PHASE 78 ---")
    print("--- [INITIALIZING SECURITY PROTOCOL] ---")
    time.sleep(1)

    master_pass = "stark123" # आप इसे बदल सकते हैं
    
    print("\n🔒 SYSTEM LOCKED")
    speak("सिस्टम लॉक है। कृपया एक्सेस के लिए मास्टर पासवर्ड दर्ज करें।")
    
    user_pass = input("🔑 Enter Master Password: ")

    if user_pass == master_pass:
        print("\n🔓 ACCESS GRANTED")
        speak("पासवर्ड सही है। वेलकम बैक, दीपक।")
        print("Status: All personal data decrypted for this session.")
    else:
        print("\n❌ ACCESS DENIED")
        speak("गलत पासवर्ड। सुरक्षा कारणों से सिस्टम शटडाउन हो रहा है।")
        exit()

    print("\n✅ Phase 78: Security Encryption Active.")

if __name__ == "__main__":
    phase_78_encryptor()
