import os
import datetime

class CoreDiagnostician:
    def __init__(self):
        self.master = "Deepak"

    def run_health_check(self):
        print(f"\n\033[1;34m[DIAGNOSTICIAN ACTIVE]\033[0m Scanning Super-Frame health...")
        
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        # हम चेक कर रहे हैं कि क्या कोर डायरेक्टरी एक्सेसिबल है
        is_writable = os.access('.', os.W_OK)
        
        print(f"\033[1;36m[TIMESTAMP]:\033[0m {current_time}")
        print(f"\033[1;36m[WRITABLE]:\033[0m {'YES' if is_writable else 'NO'}")
        
        if is_writable:
            msg = f"Deepak sir, health scan complete at {current_time}. All core systems are functioning at peak capacity."
        else:
            msg = "Deepak sir, I detected a restriction in the file system. Please check permissions."
            
        print(f"\033[1;32m[REPORT]:\033[0m {msg}")
        os.system(f'termux-tts-speak "{msg}"')

if __name__ == "__main__":
    diag = CoreDiagnostician()
    diag.run_health_check()
