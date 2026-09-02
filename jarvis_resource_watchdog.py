import os
import psutil

class ResourceWatchdog:
    def __init__(self):
        self.master = "Deepak"
        self.threshold = 85.0 # 85% से ऊपर लोड होने पर अलर्ट

    def check_vitals(self):
        print(f"\n\033[1;33m[WATCHDOG ACTIVE]\033[0m Monitoring system memory...")
        
        # RAM का उपयोग चेक करना
        memory = psutil.virtual_memory()
        usage_pct = memory.percent
        
        print(f"\033[1;36m[RAM USAGE]:\033[0m {usage_pct}%")
        
        if usage_pct > self.threshold:
            msg = f"Warning Deepak sir, memory usage is critical at {usage_pct} percent. Initiating standby mode."
            print(f"\033[1;31m[CRITICAL]:\033[0m {msg}")
        else:
            msg = f"Deepak sir, memory usage is stable at {usage_pct} percent. System is healthy."
            print(f"\033[1;32m[SAFE]:\033[0m {msg}")
            
        os.system(f'termux-tts-speak "{msg}"')

if __name__ == "__main__":
    watchdog = ResourceWatchdog()
    watchdog.check_vitals()
