import time
import hashlib

class VoiceBiometrics:
    def __init__(self, owner_name):
        self.owner = owner_name
        self.voice_hash = hashlib.sha256(owner_name.encode()).hexdigest()

    def verify_vocal_frequency(self, input_voice):
        print("\033[1;34m[BIO-SCAN] Analyzing Audio Frequency Patterns...\033[0m")
        time.sleep(1.5)
        # Checking if the voice matches the owner's unique biometric signature
        if hashlib.sha256(input_voice.encode()).hexdigest() == self.voice_hash:
            return True
        return False

class EncryptedResponse:
    def grant_access(self):
        print("\033[1;32m[ACCESS GRANTED] Voice Identity Confirmed: Hello, Deepak.\033[0m")
        print("  • Decrypting Command Interface... [OK]")
        return "JARVIS_ACTIVE"

    def deny_access(self):
        print("\033[1;31m[SECURITY ALERT] Unknown Voice Frequency Detected!\033[0m")
        print("  • System in Silent-Ghost Mode. No Response Sent.")
        return "STAY_SILENT"

if __name__ == "__main__":
    secure_voice = VoiceBiometrics("Deepak")
    response = EncryptedResponse()
    
    print("-" * 50)
    print("   JARVIS VOICE-BIOMETRIC INTERFACE (P3157-58)")
    print("-" * 50)
    
    # Simulating a command from the owner
    if secure_voice.verify_vocal_frequency("Deepak"):
        print(response.grant_access())
    else:
        print(response.deny_access())
    print("-" * 50)
