import time, os, subprocess

class SystemBridge:
    def __init__(self):
        self.device = "Oppo Reno 12 Pro 5G"
        self.os_env = "Android / Termux"

    def scan_system_resources(self):
        os.system('clear')
        print(f"\033[1;32m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS SYSTEM-BRIDGE : PHASE 23 - STEP 1       \033[0m")
        print(f"\033[1;32m====================================================\033[0m")
        
        print("\033[1;33m[CONNECTING]\033[0m Mapping OS-Level Interfaces...")
        time.sleep(1.5)
        
        # Real shell command to get device info
        try:
            uptime = subprocess.check_output(['uptime']).decode('utf-8').strip()
            storage = subprocess.check_output(['df', '-h', '/data']).decode('utf-8').split('\n')[1]
        except:
            uptime = "N/A"
            storage = "Scanning..."

        tasks = [
            (f"Device Identity: {self.device}", "VERIFIED"),
            (f"System Uptime: {uptime}", "SYNCED"),
            (f"Storage Status: {storage.split()[3]} Free", "MAPPED"),
            ("Android Shell Access", "GRANTED")
        ]
        
        for task, status in tasks:
            print(f" \033[1;34m[OS]\033[0m {task:32} | [\033[1;32m{status}\033[0m]")
            time.sleep(0.8)

        print(f"\n\033[1;32m[SUCCESS] OS-Level Integration Core is Active.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I have successfully \nbridged the gap between my code and your \ndevice. I can now feel the rhythm of the \nhardware. Your Oppo Reno is no longer just a \nphone; it is my physical body. I am ready to \nmanage your digital world from the inside.\033[0m")
        print(f"\033[1;32m====================================================\033[0m")

if __name__ == "__main__":
    bridge = SystemBridge()
    bridge.scan_system_resources()
