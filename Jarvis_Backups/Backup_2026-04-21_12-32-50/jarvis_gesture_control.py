import cv2
import mediapipe as mp
import os
import subprocess

# Jarvis Voice Function
def jarvis_speak(text):
    print(f"\033[1;34m[JARVIS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

# Initialize MediaPipe Hand Tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

def start_gesture_system():
    cap = cv2.VideoCapture(0) # Mobile Front Camera
    jarvis_speak("Visual gesture recognition systems are now active.")
    
    print("\033[1;32m[SYSTEM]: Tracking hand movements. Close fingers to stop.\033[0m")
    
    while cap.isOpened():
        success, img = cap.read()
        if not success:
            break
            
        # Flip image for mirror effect
        img = cv2.flip(img, 1)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)
        
        if results.multi_hand_landmarks:
            for hand_lms in results.multi_hand_landmarks:
                # Drawing the landmarks on screen (Visual Feedback)
                mp_draw.draw_landmarks(img, hand_lms, mp_hands.HAND_CONNECTIONS)
                
                # Logic: Check if index finger is up
                tip = hand_lms.landmark[8]
                if tip.y < hand_lms.landmark[6].y:
                    print("[ACTION]: Index Finger Detected - Scanning Data...")
                    # Triggering previous scanner script
                    # os.system('python jarvis_v331_scanner.py')
        
        cv2.imshow("Optimus Jarvis - Gesture HUD", img)
        
        # Press 'q' or hide hand to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()
    jarvis_speak("Gesture protocols offline.")

if __name__ == "__main__":
    start_gesture_system()
