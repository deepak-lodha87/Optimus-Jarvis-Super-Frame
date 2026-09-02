import time

class SecurityBarrier:
    def __init__(self):
        self.access_key = "Deepak_Jarvis_2026"
        self.is_locked = True

    def authenticate(self, key):
        print("\033[1;35m[SECURITY] Scanning Access Key...\033[0m")
        time.sleep(1.5)
        
        if key == self.access_key:
            self.is_locked = False
            print("\033[1;32m[ACCESS GRANTED] Welcome, Deepak. Encryption Barrier Offline.\033[0m")
        else:
            print("\033[1;31m[DENIED] Intruder Detected. Lockdown Protocol Active!\033[0m")

    def encrypt_vault(self):
        if self.is_locked:
            print("\033[1;34m[ENCRYPTION] All Phase files are now under AES-256 Simulation.\033[0m")
        else:
            print("\033[1;33m[WARNING] System is currently decrypted for maintenance.\033[0m")

if __name__ == "__main__":
    guard = SecurityBarrier()
    print("-" * 50)
    print("   JARVIS ENCRYPTION & SECURITY BARRIER")
    print("-" * 50)
    
    # Simulating a login attempt
    user_input = "Deepak_Jarvis_2026" # Aap ise badal kar test kar sakte hain
    guard.authenticate(user_input)
    guard.encrypt_vault()
