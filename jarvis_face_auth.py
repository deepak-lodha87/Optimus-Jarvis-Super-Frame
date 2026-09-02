import time

class VisualAuth:
    def __init__(self):
        self.master_id = "DEEPAK_FACIAL_VECTOR_001"
        self.security_status = "ARMED"

    def scan_face(self, detected_vector):
        print(f"\033[1;36m[SCANNING]\033[0m Analyzing Facial Landmarks...")
        time.sleep(1.5)
        
        if detected_vector == self.master_id:
            print(" \033[1;32m[MATCHED]\033[0m Identity Confirmed: Deepak Sir.")
            self.unlock_sanctuary()
        else:
            print(" \033[1;31m[DENIED]\033[0m Unknown Subject. Lockdown maintained.")

    def unlock_sanctuary(self):
        print(" \033[1;34m[ACTION]\033[0m Retracting Magnetic Bolts... Welcome Home.")

if __name__ == "__main__":
    auth = VisualAuth()
    # Simulating a successful face match
    auth.scan_face("DEEPAK_FACIAL_VECTOR_001")
