import os
import time
import json

def speak(text):
    os.system(f"termux-tts-speak '{text}'")

def listen_voice():
    # यह कमांड माइक्रोफोन से 3 सेकंड की आवाज़ रिकॉर्ड करके उसे टेक्स्ट में बदलती है
    print("\n[👂 LISTENING...]")
    # Termux voice-to-text engine का उपयोग
    result = os.popen("termux-speech-to-text").read().strip().lower()
    return result

def main_wake_system():
    os.system("clear")
    print("--- OPTIMUS JARVIS 2.0: VOICE ENGINE ACTIVE ---")
    speak("वॉयस इंजन सक्रिय है। जार्विस बोलने पर मैं रिस्पॉन्स दूंगा।")
    
    while True:
        voice_data = listen_voice()
        print(f"User said: {voice_data}")
        
        if "jarvis" in voice_data:
            print("\n🌟 [WAKE-WORD DETECTED]")
            speak("जी दीपक, मैं सक्रिय हूँ। आदेश दें।")
            os.system("python jarvis_final.py")
            break
        elif "exit" in voice_data:
            speak("वॉयस इंजन बंद हो रहा है।")
            break
        else:
            print("Status: Waiting for 'Jarvis'...")
            time.sleep(1)

if __name__ == "__main__":
    main_wake_system()
