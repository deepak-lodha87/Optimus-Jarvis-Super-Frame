import os
import shutil

class ResilientMonitor:
    def __init__(self):
        self.master = "Deepak"

    def check_allowed_vitals(self):
        print(f"\n\033[1;36m[RESILIENT MONITOR ACTIVE]\033[0m Scanning accessible vitals...")
        
        # CPU के बजाय हम Storage और Memory stats पर ध्यान देंगे जो सुरक्षित हैं
        total, used, free = shutil.disk_usage("/")
        storage_percent = (used / total) * 100
        
        print(f"\033[1;32m[SYSTEM]:\033[0m Storage is {storage_percent:.2f}% occupied.")
        
        msg = f"Deepak sir, resilient monitoring is active. Storage usage is nominal at {int(storage_percent)} percent."
        os.system(f'termux-tts-speak "{msg}"')

if __name__ == "__main__":
    monitor = ResilientMonitor()
    monitor.check_allowed_vitals()
