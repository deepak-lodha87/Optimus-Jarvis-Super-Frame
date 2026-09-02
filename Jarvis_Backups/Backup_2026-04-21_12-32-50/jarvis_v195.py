import os
import time

def optical_scan():
    print("\n[SYSTEM]: Initializing Optical Reconnaissance...")
    time.sleep(1)
    print("[SYSTEM]: Activating Primary Camera Sensor...")
    
    # फाइल का नाम टाइमस्टैम्प के साथ
    filename = f"scan_{int(time.time())}.jpg"
    
    try:
        # Termux API कमांड फोटो खींचने के लिए
        # (इसके लिए termux-camera-photo इंस्टॉल होना चाहिए)
        os.system(f"termux-camera-photo -c 0 {filename}")
        
        msg = f"Commander Deepak, scan complete. Image saved as {filename}."
        print(f"\n[JARVIS]: {msg}")
        os.system(f"termux-tts-speak '{msg}'")
    except Exception as e:
        print("[ERROR]: Camera access denied or API not found.")

def jarvis_main():
    print("\n" + "="*50)
    print("|    JARVIS PHASE 195: OPTICAL SCAN MATRIX    |")
    print("="*50)
    
    optical_scan()
    
    print("\n[STATUS]: Visual data logged in local database.")
    print("="*50)

if __name__ == "__main__":
    jarvis_main()
