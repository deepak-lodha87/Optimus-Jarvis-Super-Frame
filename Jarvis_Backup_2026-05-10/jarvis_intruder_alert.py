import time
import os

class JarvisIntruderGuard:
    def __init__(self):
        self.project = "Optimus Jarvis Super-Frame"
        self.owner = "Deepak"
        self.attempts = 0
        self.max_attempts = 3

    def trigger_stealth_capture(self):
        """
        Phase 1057: Capturing the intruder's image using Termux-API.
        (Note: Requires termux-camera-photo to be installed)
        """
        print(f"\n[JARVIS] ALERT: Multiple failed attempts detected!")
        print(f"[JARVIS] Activating Front Camera on Oppo Reno 12 Pro...")
        
        # Simulating a silent photo capture
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"intruder_{timestamp}.jpg"
        
        print(f"--- STEALTH MODE ACTIVE ---")
        print(f"Captured: {filename} | Location: Daulatganj, Rajasthan")
        print(f"Status: Photo saved to encrypted vault.")
        return filename

    def send_remote_notification(self, photo_file):
        """
        Phase 1058: Sending a high-priority alert to the owner.
        """
        print(f"\n[JARVIS] Sending Urgent Security Alert to {self.owner}...")
        time.sleep(1)
        
        message = f"Security Breach! Intruder detected at {time.ctime()}. Photo: {photo_file}"
        
        print(f"--- CLOUD NOTIFICATION ---")
        print(f"Notification Sent: {message}")
        print(f"RESULT: Owner has been notified. System Locked Down.")

    def verification_loop(self):
        correct_token = 7788 # मान लीजिए यह कोड फोन पर दिखा था
        
        while self.attempts < self.max_attempts:
            try:
                user_input = int(input(f"[Attempt {self.attempts + 1}] Enter Code: "))
                if user_input == correct_token:
                    print(f"\n[JARVIS] Welcome back, {self.owner}. Access Unlocked.")
                    return True
                else:
                    print("Invalid Token.")
                    self.attempts += 1
            except ValueError:
                print("Error: Input numeric digits only.")
                self.attempts += 1

        # अगर 3 बार गलत हुआ
        photo = self.trigger_stealth_capture()
        self.send_remote_notification(photo)
        return False

if __name__ == "__main__":
    guard = JarvisIntruderGuard()
    print(f"--- {guard.project} | Security Phase 1057-1058 ---")
    guard.verification_loop()
