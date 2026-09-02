import psutil
import os
import shutil

class SystemPulse:
    def __init__(self):
        self.master = "Deepak"

    def check_vitals(self):
        print(f"\n\033[1;34m[SYSTEM PULSE ACTIVE]\033[0m Analyzing device vitals...")
        
        # 1. RAM Usage
        ram = psutil.virtual_memory()
        ram_percent = ram.percent
        
        # 2. Storage Usage
        total, used, free = shutil.disk_usage("/")
        storage_percent = (used / total) * 100
        
        # 3. Battery Stats (using Termux API)
        # Note: accurate battery temp usually requires termux-battery-status
        
        print(f"\033[1;33m>>> RAM Usage:\033[0m {ram_percent}%")
        print(f"\033[1;33m>>> Storage Usage:\033[0m {storage_percent:.2f}%")
        
        report = f"Deepak sir, system analysis complete. RAM is at {ram_percent} percent and storage is {int(storage_percent)} percent full."
        
        if ram_percent > 85:
            report += " Warning: RAM usage is high. Consider closing background apps."
            print("\033[1;31m[WARNING]: High RAM Load Detected!\033[0m")
            
        os.system(f'termux-tts-speak "{report}"')
        print("\033[1;32m[PULSE NOMINAL]\033[0m Reports delivered.")

if __name__ == "__main__":
    pulse = SystemPulse()
    pulse.check_vitals()
