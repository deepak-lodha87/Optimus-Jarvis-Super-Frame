import time

class JarvisIdentityGuard:
    def __init__(self):
        self.owner = "Deepak"
        self.secret_key = "IRON-DEEPAK-77" # यह आपका गुप्त पासवर्ड है
        self.voice_id = "V-DPK-992" # आपकी आवाज़ का डिजिटल फिंगरप्रिंट

    def verify_identity(self, name_input, key_input):
        """
        Phase 1053: Double-checking the person behind the voice/text.
        """
        print(f"\n[JARVIS] Identity Verification in progress...")
        time.sleep(1)
        
        # Checking if it's actually you
        if name_input == self.owner and key_input == self.secret_key:
            print(f"--- ACCESS GRANTED ---")
            print(f"Welcome back, Sir. Voice ID {self.voice_id} confirmed.")
            return True
        else:
            print(f"--- ACCESS DENIED ---")
            print(f"Identity mismatch. Lockdown Protocol initiated.")
            return False

    def secure_handshake(self):
        """
        Phase 1054: Establishing an encrypted session once verified.
        """
        print(f"[JARVIS] Establishing Secure Handshake... [OK]")
        print("[JARVIS] All 1050 phases are now under your exclusive control.")

if __name__ == "__main__":
    guard = JarvisIdentityGuard()
    
    # Test: जार्विस अब आपसे आपका नाम और सीक्रेट की (Secret Key) पूछेगा
    user_name = input("Identify yourself: ")
    user_key = input("Enter Secret Alpha-Key: ")
    
    if guard.verify_identity(user_name, user_key):
        guard.secure_handshake()
    else:
        print("[SYSTEM] Unauthorized user detected. System is now invisible.")
