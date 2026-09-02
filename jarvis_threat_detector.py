import os
import time
import random

class ThreatDetector:
    def __init__(self):
        self.master = "Deepak"
        self.security_level = "High"

    def scan_perimeter(self):
        print(f"\n\033[1;31m[SCANNING PERIMETER]\033[0m E.D.I.T.H. is analyzing surroundings...")
        time.sleep(2)
        
        objects = ["Pedestrian", "Unknown Vehicle", "Obstacle", "Clear Path"]
        
        for _ in range(5):
            detected = random.choice(objects)
            color = "\033[1;32m" if detected == "Clear Path" else "\033[1;31m"
            print(f"\033[1;37m[OBJECT FOUND]:\033[0m {color}{detected}\033[0m")
            time.sleep(0.8)
            
            if detected != "Clear Path":
                self.alert(detected)

    def alert(self, target):
        msg = f"Deepak sir, I have identified a {target} in your path. Adjusting suspension and security protocols now."
        print(f"\033[1;33m[ALERT]:\033[0m Action initiated for {target}")
        os.system(f'termux-tts-speak "{msg}"')

if __name__ == "__main__":
    scanner = ThreatDetector()
    scanner.scan_perimeter()
