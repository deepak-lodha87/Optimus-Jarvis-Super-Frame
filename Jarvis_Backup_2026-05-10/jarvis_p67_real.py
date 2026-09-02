import os
import json
import time
from gtts import gTTS

def speak(text):
    print(f"[JARVIS]: {text}")
    tts = gTTS(text=text, lang='hi')
    tts.save("battery_real.mp3")
    os.system("play-audio battery_real.mp3")

def get_battery():
    # Termux API से असली बैटरी डेटा लेना
    status = os.popen("termux-battery-status").read()
    data = json.loads(status)
    return data['percentage']

def phase_67_real():
    print("--- OPTIMUS JARVIS SUPER-FRAME: PHASE 67 (REAL-TIME) ---")
    
    try:
        level = get_battery()
        print(f"🔋 Actual Battery Level: {level}%")
        
        if level < 20:
            msg = f"दीपक, बैटरी केवल {level} प्रतिशत है। सिस्टम को पावर की जरूरत है।"
        elif level > 80:
            msg = f"बैटरी की स्थिति बेहतरीन है, अभी यह {level} प्रतिशत है।"
        else:
            msg = f"बैटरी लेवल {level} प्रतिशत पर स्थिर है।"
        
        speak(msg)
    except:
        print("❌ Error: 'termux-api' इंस्टॉल करें और बैटरी परमिशन दें।")

if __name__ == "__main__":
    phase_67_real()
