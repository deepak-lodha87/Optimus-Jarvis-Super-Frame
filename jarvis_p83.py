import os
import time
import sys

def speak(text):
    os.system(f"termux-tts-speak '{text}'")

def shutdown_protocol():
    print("--- OPTIMUS JARVIS SUPER-FRAME: PHASE 83 ---")
    print("--- [INITIALIZING SAFE SHUTDOWN PROTOCOL] ---")
    time.sleep(1)

    confirm = input("❗ दीपक, क्या आप वाकई सिस्टम बंद करना चाहते हैं? (yes/no): ").lower()

    if confirm == "yes":
        speak("सिस्टम शटडाउन प्रक्रिया शुरू की जा रही है। सुरक्षित रहें, दीपक।")
        
        steps = ["Saving System Logs...", "Closing Neural Links...", "Cutting Power Supply...", "Jarvis Offline."]
        
        for step in steps:
            print(f"[-] {step}")
            time.sleep(0.8)
        
        print("\n[SYSTEM OFFLINE]")
        os.system("clear")
        sys.exit()
    else:
        print("\n[ABORTED] शटडाउन रद्द कर दिया गया है।")
        speak("शटडाउन रद्द। मैं आपकी सेवा में वापस आ गया हूँ।")

if __name__ == "__main__":
    shutdown_protocol()
