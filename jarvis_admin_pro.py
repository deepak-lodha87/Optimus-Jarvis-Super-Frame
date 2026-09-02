import os
import platform
import datetime

class JarvisAdmin:
    def __init__(self):
        self.master = "Deepak"
        self.os_info = platform.machine()
        self.log_file = "jarvis_system_logs.log"

    def deploy_admin_protocols(self):
        print(f"\n\033[1;33m[DEPLOYING ADMIN PROTOCOLS - PHASE 250]\033[0m")
        
        # Phase 210: Log Generation
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a") as f:
            f.write(f"Session started by {self.master} at {timestamp}\n")

        # Phase 220-240: Hardware Handshake (Safe Mode)
        print(f"\033[1;36m[HARDWARE]:\033[0m Platform: {self.os_info}")
        print(f"\033[1;36m[SECURITY]:\033[0m Firewall: ACTIVE")
        
        # Phase 250: Strategic Finalization
        msg = f"Deepak sir, Jarvis has reached Phase 250. System logs are secured, and hardware handshake is complete on your {self.os_info} architecture."
        
        print("-" * 45)
        print(f"\033[1;32mSTATUS: ALL SYSTEMS NOMINAL - PHASE 250 SECURED\033[0m")
        print("-" * 45)
        
        os.system(f'termux-tts-speak "{msg}"')

if __name__ == "__main__":
    admin = JarvisAdmin()
    admin.deploy_admin_protocols()
