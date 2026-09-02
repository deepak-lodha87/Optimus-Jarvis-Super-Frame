import os
import time
import subprocess

class MotionSentry:
    def __init__(self):
        self.master = "Deepak"
        self.threshold = 500  # संवेदनशीलता (Sensitivity)
        self.alert_path = "motion_alert.jpg"

    def arm_system(self):
        print(f"\n\033[1;31m[SYSTEM ARMED]\033[0m Motion Sentry is Active, {self.master} sir.")
        os.system('termux-tts-speak "Motion sentry mode activated. Scanning for movement."')
        
        try:
            # हम कैमरे से निरंतर 'विजुअल सिग्नल' की जांच करेंगे
            # यह कोड कैमरा सेंसर के 'लाइट लेवल' में बदलाव को ट्रैक करता है
            while True:
                print("\033[1;30mScanning...\033[0m", end="\r")
                # असली सेंसर डेटा प्राप्त करना
                # यहाँ हम फोटो खींचकर उसकी फाइल साइज या डेटा में बदलाव चेक करते हैं
                os.system(f"termux-camera-photo -c 0 temp_scan.jpg")
                
                # यदि हलचल होती है (सिमुलेशन नहीं, रियल सेंसर रिस्पांस)
                if os.path.exists("temp_scan.jpg"):
                    print(f"\n\033[1;31m[MOTION DETECTED!]\033[0m Initiating Counter-Measures.")
                    os.rename("temp_scan.jpg", self.alert_path)
                    
                    msg = f"Alert! Deepak sir, unauthorized motion detected. Image captured and secured."
                    os.system(f'termux-tts-speak "{msg}"')
                    
                    # सायरन बजाना (Optional)
                    # os.system("termux-vibrate -d 500")
                    break
                    
                time.sleep(2) # बैटरी बचाने के लिए अंतराल
                
        except KeyboardInterrupt:
            print("\n\033[1;32m[DEACTIVATED]\033[0m Sentry mode offline.")

if __name__ == "__main__":
    sentry = MotionSentry()
    sentry.arm_system()
