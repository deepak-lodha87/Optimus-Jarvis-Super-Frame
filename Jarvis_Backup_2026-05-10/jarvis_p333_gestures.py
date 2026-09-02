import cv2
import mediapipe as mp
import subprocess
import os
import time

# Voice Feedback
def jarvis_speak(text):
    print(f"\033[1;34m[JARVIS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

# Initialize Hand Tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

def gesture_control_center():
    cap = cv2.VideoCapture(0)
    jarvis_speak("Phase 333 Gesture Intelligence Hub is now active.")
    print("\033[1;32m[SYSTEM]: Scanning for hand landmarks...\033[0m")

    while cap.isOpened():
        success, img = cap.read()
        if not success: break
        
        img = cv2.flip(img, 1)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)

        if results.multi_hand_landmarks:
            for hand_lms in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(img, hand_lms, mp_hands.HAND_CONNECTIONS)
                
                # Finger Detection Logic
                # Index finger tip (ID 8) aur middle finger tip (ID 12)
                index_y = hand_lms.landmark[8].y
                base_y = hand_lms.landmark[6].y
                
                if index_y < base_y:
                    print("\033[1;33m[GESTURE]: Index Finger Up - Running Scanner...\033[0m")
                    jarvis_speak("Scanning data clusters.")
                    cap.release()
                    cv2.destroyAllWindows()
                    os.system('python jarvis_v331_scanner.py')
                    return

        cv2.imshow("Optimus Jarvis HUD - P333", img)
        if cv2.waitKey(1) & 0xFF == ord('q'): break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    gesture_control_center()
