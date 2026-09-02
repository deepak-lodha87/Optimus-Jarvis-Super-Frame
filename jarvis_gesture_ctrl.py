import os
import time
import subprocess

class GestureControl:
    def __init__(self):
        self.master = "Deepak"

    def monitor_motion(self):
        print("\n\033[1;35m[GESTURE RADAR ACTIVE]\033[0m Monitoring master's hand signals...")
        os.system('termux-tts-speak "Gesture radar is active. Wave your hand to trigger the system."')
        
        # पहली इमेज कैप्चर करना
        os.system("termux-camera-photo -c 1 frame1.jpg")
        time.sleep(2)
        
        # दूसरी इमेज कैप्चर करना (हलचल चेक करने के लिए)
        os.system("termux-camera-photo -c 1 frame2.jpg")
        
        # फाइल साइज की तुलना करके मोशन का पता लगाना
        size1 = os.path.getsize("frame1.jpg")
        size2 = os.path.getsize("frame2.jpg")
        
        diff = abs(size1 - size2)
        
        if diff > 5000: # अगर इमेज साइज में 5KB से ज्यादा फर्क है, मतलब हलचल हुई है
            print("\033[1;32m[MOTION DETECTED]\033[0m Executing gesture command...")
            os.system('termux-tts-speak "Motion recognized. Launching Phase 101 status report, Deepak sir."')
            os.system("python jarvis_social_sync.py")
        else:
            print("\033[1;33m[STABLE]\033[0m No significant movement detected.")
            os.system('termux-tts-speak "System stable. No gesture detected."')

if __name__ == "__main__":
    gest = GestureControl()
    gest.monitor_motion()
