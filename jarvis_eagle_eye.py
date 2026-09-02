import time
import random

class EagleEye:
    def __init__(self):
        self.objects_in_view = ["Tree", "Person", "Landing Pad", "Bird"]

    def scan_environment(self):
        print("\033[1;36m[VISION]\033[0m Activating Camera Stream and Neural Processing...")
        time.sleep(1.5)
        
        # Simulating frame-by-frame analysis
        for _ in range(5):
            detected = random.choice(self.objects_in_view)
            confidence = random.randint(85, 99)
            
            print(f" \033[1;37m[SCAN]\033[0m Frame Analyzed: Found \033[1;32m{detected}\033[0m (Confidence: {confidence}%)")
            
            if detected == "Tree":
                print(" \033[1;31m[ADJUST]\033[0m Obstacle detected! Veering left to avoid collision.")
            elif detected == "Person":
                print(" \033[1;34m[LOCK]\033[0m Subject identified as 'Deepak'. Initiating Follow-Me mode.")
            
            time.sleep(0.8)

        print(f"\n\033[1;35m[VOICE] Deepak... sir, my eyes are open. \nI am no longer flying blind. I can see the \nworld in shapes, colors, and movements. \nI am tracking every detail of our flight \npath. You are in my sight.\033[0m")

if __name__ == "__main__":
    vision = EagleEye()
    vision.scan_environment()
