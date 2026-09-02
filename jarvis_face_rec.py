import time, os

class FaceRecognition:
    def __init__(self):
        self.authorized_user = "Deepak"
        self.status = "SCANNING"

    def scan_face(self):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS FACE-REC : PHASE 20 - STEP 6            \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        print("\033[1;33m[CAMERA]\033[0m Activating Oppo Reno 12 Pro Front Lens...")
        time.sleep(1.5)
        
        print("\033[1;34m[SCANNING]\033[0m Analyzing Biometric Data...")
        # Visual Scanning Animation
        for i in range(1, 6):
            print(f"  Verifying Point Cloud {i*20}%...")
            time.sleep(0.5)

        print(f"\n\033[1;32m[MATCH FOUND] Identity Confirmed: {self.authorized_user}\033[0m")
        print(f"\n\033[1;35m[VOICE] Welcome back, Deepak sir. The systems are \nnow fully at your disposal. I have updated the \nwealth stream and security logs during your \nabsence. How can I assist you today?\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    scanner = FaceRecognition()
    scanner.scan_face()
