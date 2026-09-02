import os
import time

def biometric_voice_simulation():
    print("\n" + "="*40)
    print("      JARVIS BIOMETRIC VOICE CORE")
    print("="*40)
    
    msg_init = "Commander Deepak, standing by for voice pattern identification."
    print(f"\n[JARVIS]: {msg_init}")
    os.system(f"termux-tts-speak '{msg_init}'")
    
    # सिमुलेटेड वॉइस इनपुट
    print("\n[SYSTEM]: Recording voice sample for 3 seconds...")
    time.sleep(3)
    
    # यूनिक कमांडर आईडी की जांच
    commander_id = "DEEPAK-001"
    msg_verify = "Processing unique frequency patterns..."
    print(f"\n[JARVIS]: {msg_verify}")
    os.system(f"termux-tts-speak '{msg_verify}'")
    
    time.sleep(2)
    
    input_id = input("\n[INPUT]: Speak your Unique Commander ID: ").upper()
    
    if input_id == commander_id:
        access_granted = f"Welcome back, Commander Deepak. Identity confirmed. All systems at your disposal."
        print(f"\n[SUCCESS]: {access_granted}")
        os.system(f"termux-tts-speak '{access_granted}'")
    else:
        access_denied = "Alert! Voice pattern mismatch. Security breach protocol initiated."
        print(f"\n[DENIED]: {access_denied}")
        os.system(f"termux-tts-speak '{access_denied}'")

    print("\n" + "="*40)

if __name__ == "__main__":
    biometric_voice_simulation()
