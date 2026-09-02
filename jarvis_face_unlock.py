import cv2
import mediapipe as mp
import subprocess
import time
import os

# Voice Function
def jarvis_speak(text):
    print(f"\033[1;34m[JARVIS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

# Initialize Face Detection
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5)

def security_scan():
    cap = cv2.VideoCapture(0)
    os.system('clear')
    print("\033[1;31m[SECURITY]: SCANNING FOR AUTHORIZED USER...\033[0m")
    jarvis_speak("Initiating biometric facial recognition.")
    
    start_time = time.time()
    authorized = False

    while cap.isOpened():
        success, img = cap.read()
        if not success: break
        
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = face_detection.process(img_rgb)

        if results.detections:
            print("\033[1;32m[SYSTEM]: USER DETECTED. MATCHING BIOMETRICS...\033[0m")
            authorized = True
            break
        
        # Timeout after 10 seconds if no face found
        if time.time() - start_time > 10:
            break

    cap.release()
    cv2.destroyAllWindows()

    if authorized:
        jarvis_speak("Welcome back, Deepak. Access granted. Optimus Jarvis is at your service.")
        # Triggering the main dashboard
        subprocess.run(['python', 'jarvis_v331_scanner.py'])
    else:
        jarvis_speak("Unauthorized access detected. Locking system protocols.")
        print("\033[1;31m[ALERT]: ACCESS DENIED.\033[0m")

if __name__ == "__main__":
    security_scan()
