import os
import time
import sys

def speak(text):
    os.system(f"termux-tts-speak '{text}'")

def boot_animation():
    os.system("clear")
    # यहाँ हमने 'Stark Industries' को बदलकर आपके प्रोजेक्ट का नाम कर दिया है
    header = """
    =========================================
        OPTIMUS JARVIS SUPER-FRAME - CORE
    =========================================
    """
    print(header)
    speak("सिस्टम बूट सीक्वेंस शुरू किया जा रहा है।")
    
    tasks = [
        "Initializing Optimus Neural Networks...",
        "Loading Super-Frame Modules...",
        "Scanning Hardware Integrity...",
        "Finalizing System UI..."
    ]

    for task in tasks:
        sys.stdout.write(f"\r[ ] {task}")
        sys.stdout.flush()
        time.sleep(0.7)
        sys.stdout.write(f"\r[✔] {task}\n")
        sys.stdout.flush()

    print("\n=========================================")
    print("      SYSTEM READY: WELCOME DEEPAK")
    print("=========================================")
    speak("ऑप्टिमस जार्विस सक्रिय है। वेलकम बैक, दीपक।")

if __name__ == "__main__":
    boot_animation()
