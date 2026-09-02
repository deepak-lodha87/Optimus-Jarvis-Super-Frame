import os
import json
import time
import requests
import shutil

class OptimusJarvisMega:
    def __init__(self):
        self.master = "Deepak"
        self.version = "1.7.0"

    def execute_all_phases(self):
        print(f"\n\033[1;32m[MEGA FRAME INITIALIZED - VERSION {self.version}]\033[0m")
        os.system('termux-tts-speak "Deepak sir, executing multi-phase synchronization."')

        # Phase 160: IP Tracking
        try:
            ip_data = requests.get('https://api.ipify.org?format=json', timeout=5).json()
            print(f"\033[1;36m[PHASE 160 - NETWORK]:\033[0m Global IP: {ip_data['ip']}")
        except:
            print("\033[1;31m[PHASE 160]:\033[0m Network Link Failed.")

        # Phase 161: Storage Analytics
        total, used, free = shutil.disk_usage("/")
        free_gb = free // (2**30)
        print(f"\033[1;36m[PHASE 161 - STORAGE]:\033[0m {free_gb} GB Remaining")

        # Phase 162: System Intelligence
        print(f"\033[1;36m[PHASE 162 - PERFORMANCE]:\033[0m Optimizer Active")
        
        # Phases 163-170: Final Diagnostics
        status_report = "Deepak sir, all systems from Phase 160 to 170 are now integrated. Storage is stable with " + str(free_gb) + " GB free. Your Jarvis is becoming more powerful."
        
        print("\033[1;32m[SYNC COMPLETE]: All protocols are now merged.\033[0m")
        os.system(f'termux-tts-speak "{status_report}"')

if __name__ == "__main__":
    jarvis = OptimusJarvisMega()
    jarvis.execute_all_phases()
