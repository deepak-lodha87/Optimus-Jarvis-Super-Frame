import os
import time

def speak(text):
    print(f"[JARVIS]: {text}")
    os.system(f"termux-tts-speak '{text}'")

def system_reboot():
    print("--- OPTIMUS JARVIS SUPER-FRAME: PHASE 95 ---")
    print("--- [INITIALIZING INTELLIGENT REBOOT] ---")
    time.sleep(1)

    speak("सिस्टम रीबूट प्रक्रिया शुरू हो रही है। सभी मॉड्यूल्स को रीफ्रेश किया जा रहा है।")
    
    animations = ["|", "/", "-", "\\"]
    for _ in range(10):
        for char in animations:
            print(f"\r♻️ Rebooting {char}", end="")
            time.sleep(0.1)
    
    # पुरानी अस्थायी फाइलों को साफ करना
    os.system("rm -rf __pycache__")
    
    print("\n\n--- REBOOT COMPLETE ---")
    speak("सिस्टम अब पूरी तरह रीफ्रेश है, दीपक।")

if __name__ == "__main__":
    system_reboot()
