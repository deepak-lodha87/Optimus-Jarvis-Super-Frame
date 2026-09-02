import os
import time

class StealthSecurity:
    def __init__(self):
        self.master = "Deepak"

    def capture_intruder(self):
        print("\n\033[1;31m[SECURITY BREACH DETECTED]\033[0m")
        os.system('termux-tts-speak "Unauthorized access attempt. Activating front camera."')
        
        # फ्रंट कैमरा से फोटो खींचना (Termux-API की मदद से)
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"intruder_{timestamp}.jpg"
        
        try:
            os.system(f"termux-camera-photo -c 1 {filename}")
            print(f"\033[1;32m[EYE ACTIVE]:\033[0m Photo saved as {filename}")
            os.system('termux-tts-speak "Intruder image captured and stored in secure vault."')
        except Exception as e:
            print(f"\033[1;31m[CAMERA ERROR]:\033[0m {e}")

if __name__ == "__main__":
    security = StealthSecurity()
    # इसे आप अपने 'jarvis_security_lock.py' के 'else' पार्ट में जोड़ सकते हैं
    security.capture_intruder()
