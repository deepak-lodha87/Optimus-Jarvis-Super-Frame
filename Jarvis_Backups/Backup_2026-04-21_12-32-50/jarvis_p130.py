import os
import time

def intruder_capture():
    print("\n" + "="*40)
    print("|    JARVIS PHASE 130: OPTICAL INTRUDER   |")
    print("="*40)

    # Vibration alert
    os.system("termux-vibrate -d 500")

    # Security Message
    msg = "Security Breach! Optical capture initiated. Smile for the camera."
    print(f"\n[SECURITY]: {msg}")
    
    # Speak the alert
    os.system(f"termux-tts-speak '{msg}'")

    # Capturing image using front camera (ID 1)
    # Note: Make sure 'termux-api' package is installed
    print("[SYSTEM]: Capturing image...")
    os.system("termux-camera-photo -c 1 intruder.jpg")

    time.sleep(2)
    
    if os.path.exists("intruder.jpg"):
        print("[SUCCESS]: Intruder image saved as intruder.jpg")
        os.system("termux-tts-speak 'Intruder captured successfully, Commander.'")
    else:
        print("[ERROR]: Camera capture failed. Check Termux-API permissions.")

if __name__ == "__main__":
    # Ensure camera tools are available
    intruder_capture()
