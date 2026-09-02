import os
import time

def audio_memo_protocol():
    print("\n[SYSTEM]: Activating Audio Recording Sensors...")
    time.sleep(1)
    
    # फाइल का नाम टाइमस्टैम्प के साथ
    audio_file = f"memo_{int(time.time())}.mp3"
    duration = 5 # रिकॉर्डिंग का समय (सेकंड में)
    
    try:
        print(f"[STATUS]: Recording in progress for {duration} seconds...")
        # Termux API कमांड ऑडियो रिकॉर्ड करने के लिए
        # (इसके लिए termux-microphone-record इंस्टॉल होना चाहिए)
        os.system(f"termux-microphone-record -d {duration} -f {audio_file}")
        
        msg = f"Commander Deepak, voice memo saved as {audio_file}."
        print(f"\n[JARVIS]: {msg}")
        os.system(f"termux-tts-speak '{msg}'")
    except Exception as e:
        print("[ERROR]: Microphone access denied or API not found.")

def jarvis_main():
    print("\n" + "="*50)
    print("|    JARVIS PHASE 196: AUDIO MEMO LOGGER    |")
    print("="*50)
    
    audio_memo_protocol()
    
    print("\n[STATUS]: Audio packet secured in core database.")
    print("="*50)

if __name__ == "__main__":
    jarvis_main()
