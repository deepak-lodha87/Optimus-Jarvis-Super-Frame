import os
import time

def speak(text):
    print(f"[JARVIS]: {text}")
    os.system(f"termux-tts-speak '{text}'")

def phase_80_voice_control():
    print("--- OPTIMUS JARVIS SUPER-FRAME: PHASE 80 ---")
    print("--- [INITIALIZING VOICE CONTROL SIMULATION] ---")
    time.sleep(1)

    speak("दीपक, मैं आपके आदेश का इंतज़ार कर रहा हूँ। टॉर्च जलाने के लिए 'on' या बुझाने के लिए 'off' लिखें।")
    
    command = input("🎤 Voice Input Simulation (on/off): ").lower()

    if "on" in command:
        os.system("termux-torch on")
        speak("टॉर्च जला दी गई है।")
        print("🔦 FLASHLIGHT: ON")
    elif "off" in command:
        os.system("termux-torch off")
        speak("टॉर्च बंद कर दी गई है।")
        print("🌑 FLASHLIGHT: OFF")
    else:
        speak("क्षमा करें, यह कमांड मेरी समझ से बाहर है।")

    print("\n✅ Phase 80: Voice Control Interface Operational.")

if __name__ == "__main__":
    phase_80_voice_control()
