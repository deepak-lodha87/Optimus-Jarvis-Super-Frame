import os
import time
from gtts import gTTS

def speak(text):
    print(f"[JARVIS]: {text}")
    try:
        tts = gTTS(text=text, lang='hi')
        tts.save("sys_info.mp3")
        os.system("play-audio sys_info.mp3")
    except:
        pass

def phase_72_sys_info():
    print("--- OPTIMUS JARVIS SUPER-FRAME: PHASE 72 ---")
    print("--- [FETCHING DEVICE INTELLIGENCE] ---")
    time.sleep(1)

    # डिवाइस की जानकारी प्राप्त करना
    model = os.popen("getprop ro.product.model").read().strip()
    android_ver = os.popen("getprop ro.build.version.release").read().strip()
    cpu = os.popen("getprop ro.product.cpu.abi").read().strip()
    manufacturer = os.popen("getprop ro.product.manufacturer").read().strip()

    print("\n" + "="*30)
    print(f"📱 MANUFACTURER : {manufacturer.upper()}")
    print(f"🤖 DEVICE MODEL  : {model}")
    print(f"💿 ANDROID VER  : {android_ver}")
    print(f"⚙️  PROCESSOR    : {cpu}")
    print("="*30)

    msg = f"दीपक, यह आपके {model} डिवाइस की तकनीकी जानकारी है। सिस्टम पूरी तरह स्टेबल है।"
    speak(msg)

    print("\n✅ Phase 72: System Info Visualizer Online.")

if __name__ == "__main__":
    phase_72_sys_info()
