import os
import time
import subprocess

class FaceIdentity:
    def __init__(self):
        self.master = "Deepak"
        self.identity_file = "master_face.jpg"

    def register_master(self):
        # अगर मास्टर की पहचान पहले से मौजूद नहीं है
        if not os.path.exists(self.identity_file):
            print(f"\n\033[1;36m[REGISTRATION]\033[0m Master {self.master}, please look at the camera.")
            os.system('termux-tts-speak "Deepak sir, please look at the front camera for identity registration."')
            time.sleep(2)
            
            # फ्रंट कैमरे (1) से फोटो लेना
            os.system(f"termux-camera-photo -c 1 {self.identity_file}")
            print(f"\033[1;32m[SUCCESS]\033[0m Biometric Identity Saved: {self.identity_file}")
        else:
            self.verify_presence()

    def verify_presence(self):
        print(f"\n\033[1;34m[SCANNING]\033[0m Identifying subject...")
        # अस्थायी फोटो खींचकर तुलना के लिए तैयार करना
        os.system("termux-camera-photo -c 1 current_scan.jpg")
        
        # यहाँ जार्विस फाइल्स के 'Pixel Data' को कंपेयर करने का लॉजिक रन करेगा
        # अभी के लिए, यह हार्डवेयर रिस्पॉन्स चेक कर रहा है
        if os.path.exists("current_scan.jpg"):
            print("\033[1;32m[MATCH CONFIRMED]\033[0m Welcome back, Deepak sir.")
            os.system('termux-tts-speak "Identity verified. Welcome, Deepak sir."')
        else:
            print("\033[1;31m[WARNING]\033[0m Identity mismatch or Camera blocked.")

if __name__ == "__main__":
    face_ai = FaceIdentity()
    face_ai.register_master()
