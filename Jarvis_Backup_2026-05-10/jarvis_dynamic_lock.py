import time
import random

class JarvisDynamicSecurity:
    def __init__(self):
        self.project = "Optimus Jarvis Super-Frame"
        self.device = "Oppo Reno 12 Pro 5G"
        self.is_locked = True

    def generate_screen_code(self):
        """
        Phase 1055: Generating a random 4-digit code on the mobile screen.
        """
        code = random.randint(1000, 9999)
        print(f"\n[SYSTEM] Security Alert: Identity confirmation required.")
        print(f"--- SCREEN NOTIFICATION ({self.device}) ---")
        print(f" >>> VISUAL TOKEN: {code} <<<")
        print(f"-------------------------------------------")
        return code

    def verify_voice_token(self, generated_code):
        """
        Phase 1056: Waiting for the user to speak the code displayed on screen.
        """
        print(f"\n[JARVIS] Waiting for Voice Token, Deepak...")
        try:
            # यहाँ हम सिमुलेट कर रहे हैं कि आप कोड बोल रहे हैं
            user_input = int(input("[USER VOICE INPUT] >>> "))
            
            if user_input == generated_code:
                self.is_locked = False
                print(f"\n[JARVIS] Token Verified. Identity Confirmed.")
                print(f"Welcome back, Sir. All 1050 phases are now ACTIVE.")
            else:
                print(f"\n[JARVIS] INCORRECT TOKEN. Initiating Lockdown Protocol.")
                print("[SYSTEM] Access Denied. Camera capturing intruder image...")
        except ValueError:
            print("[SYSTEM] Invalid input format. Security breach suspected.")

if __name__ == "__main__":
    security = JarvisDynamicSecurity()
    
    # 1. स्क्रीन पर कोड दिखाओ (Phase 1055)
    secret_token = security.generate_screen_code()
    
    # 2. आवाज़ से कोड को चेक करो (Phase 1056)
    security.verify_voice_token(secret_token)
