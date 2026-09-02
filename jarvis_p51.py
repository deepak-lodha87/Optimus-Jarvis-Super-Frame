import time
import os
import sys

def startup_animation():
    frames = [
        "--- [            ] 0%",
        "--- [====        ] 30%",
        "--- [========    ] 65%",
        "--- [============] 100%"
    ]
    print("\n--- OPTIMUS JARVIS SUPER-FRAME: PHASE 51 ---")
    print("--- [INITIALIZING STARTUP ANIMATION] ---")
    
    for frame in frames:
        sys.stdout.write(f"\r{frame} Loading Core Modules...")
        sys.stdout.flush()
        time.sleep(0.5)
    
    print("\n\n" + "="*40)
    print("   O P T I M U S   J A R V I S   V 1.0   ")
    print("="*40)
    print("      STATUS: ONLINE | SECURE: YES       ")
    print("="*40)

def phase_51_branding():
    startup_animation()
    time.sleep(1)
    
    # जार्विस की वॉयस कन्फर्मेशन
    try:
        from gtts import gTTS
        text = "Deepak, system branding and animation is now active. Welcome back."
        tts = gTTS(text=text, lang='en')
        tts.save("welcome.mp3")
        os.system("play-audio welcome.mp3")
    except:
        print("[JARVIS]: System online.")

    print("\n✅ Phase 51: Visual Branding Integrated.")
    print("✅ Jarvis now has a professional startup interface.")

if __name__ == "__main__":
    phase_51_branding()
