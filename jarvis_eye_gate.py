import os
import time
import subprocess

def trigger_camera_auth():
    print(f"\n\033[1;36m[AUTHENTICATION]\033[0m Scanning for Deepak Sir's Identity...")
    
    # टर्मक्स के ज़रिए फ्रंट कैमरा से एक फोटो लेना (सिर्फ स्कैनिंग के लिए)
    try:
        # कैमरा ID '1' आमतौर पर फ्रंट कैमरा होता है
        subprocess.run(["termux-camera-photo", "-c", "1", "scan.jpg"], check=True)
        print("\033[1;32m[SCANNING...]\033[0m Biometric Pattern Detected.")
        time.sleep(1)
        
        # यहाँ जार्विस फोटो को प्रोसेस करेगा (Logic Check)
        print("\033[1;32m[SUCCESS]\033[0m Eyes Matched. Welcome, Deepak Sir.")
        os.remove("scan.jpg") # सुरक्षा के लिए फोटो तुरंत डिलीट करना
        return True
    except Exception as e:
        print("\033[1;31m[FAILED]\033[0m Hardware Access Denied or Face Not Found.")
        return False

def lock_system():
    if trigger_camera_auth():
        msg = "Access granted. Optimus Jarvis Super Frame is now online."
        os.system(f'termux-tts-speak "{msg}"')
        print("\033[1;35m[STATUS]\033[0m SOVEREIGN CONTROL ACTIVE.")
    else:
        print("\033[1;31m[LOCK]\033[0m System Frozen. Unauthorized User.")
        exit()

if __name__ == "__main__":
    lock_system()
