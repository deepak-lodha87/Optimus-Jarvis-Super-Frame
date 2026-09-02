import time
import getpass

class IAMController:
    def __init__(self):
        self.authorized_user = "Deepak"
        self.master_key = "DEEPAK_JARVIS_99" # Simulated Master Key

    def verify_identity(self):
        print("\033[1;34m[GATEKEEPER]\033[0m Initializing Identity Verification...")
        user_input = input("Enter Username: ")
        
        if user_input == self.authorized_user:
            # Note: In real Termux, we use getpass for hidden passwords
            key_input = input("Enter Master Security Key: ")
            
            if key_input == self.master_key:
                print("\n\033[1;32m[ACCESS GRANTED]\033[0m Welcome back, Sir.")
                self.load_personal_protocol()
            else:
                print("\n\033[1;31m[CRITICAL ALERT]\033[0m Wrong Key! Intrusion detected.")
        else:
            print("\n\033[1;31m[DENIED]\033[0m Unknown user. System Locking...")

    def load_personal_protocol(self):
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I have verified your \nidentity. The digital perimeter is secure. \nNo one can touch your code or your vision \nwithout your permission. You are the only \nMaster of this frame.\033[0m")

if __name__ == "__main__":
    iam = IAMController()
    iam.verify_identity()
