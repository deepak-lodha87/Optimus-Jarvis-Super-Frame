import os
import sys
import time

# OpenCV चेक करने के लिए
try:
    import cv2
except ImportError:
    print("Error: OpenCV not found. Run 'pkg install opencv'")

class OptimusJarvis:
    def __init__(self):
        self.name = "Jarvis"
        
    def speak(self, text):
        print(f"{self.name}: {text}")
        os.system(f"termux-tts-speak '{text}'")

    def vision_scan(self):
        self.speak("Starting background landmark scan.")
        # कैमरा कैप्चर
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        if ret:
            cv2.imwrite("scan.jpg", frame)
            self.speak("Scan complete. Background data saved.")
        else:
            self.speak("Unable to access camera. Check permissions.")
        cap.release()

    def startup(self):
        self.speak("Systems online. Vision module initiated.")

if __name__ == "__main__":
    jarvis = OptimusJarvis()
    jarvis.startup()
    
    while True:
        cmd = input("Deepak: ").lower()
        if "scan" in cmd:
            jarvis.vision_scan()
        elif "exit" in cmd:
            jarvis.speak("Goodbye.")
            break
