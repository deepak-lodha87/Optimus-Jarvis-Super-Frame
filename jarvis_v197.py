import os
import time

def sentry_mode_protocol():
    print("\n[SYSTEM]: Activating Digital Sentry Mode...")
    time.sleep(1)
    print("[STATUS]: Monitoring device motion sensors...")
    
    # सिम्युलेटेड सेंसर चेक
    # वास्तविक उपयोग के लिए termux-sensor का डेटा इस्तेमाल किया जा सकता है
    motion_detected = True 
    
    if motion_detected:
        alert_msg = "Commander Deepak, motion detected in the immediate vicinity. Security scan recommended."
        print(f"\n[!!! ALERT !!!]: {alert_msg}")
        os.system(f"termux-tts-speak '{alert_msg}'")
    else:
        print("[JARVIS]: Perimeter is secure. No motion detected.")

def jarvis_main():
    print("\n" + "="*50)
    print("|    JARVIS PHASE 197: DIGITAL SENTRY MODE    |")
    print("="*50)
    
    sentry_mode_protocol()
    
    print("\n[SYSTEM]: Sentry remains active in background.")
    print("="*50)

if __name__ == "__main__":
    jarvis_main()
