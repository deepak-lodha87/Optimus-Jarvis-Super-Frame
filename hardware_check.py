import os
import subprocess
import time

def check_real_mic():
    print("\033[1;33m>> SCANNING FOR EXTERNAL API TOOLS...\033[0m")
    # Termux:API command to check hardware
    check = subprocess.run(['which', 'termux-microphone-record'], capture_output=True, text=True)
    
    if check.returncode == 0:
        print("\033[1;32m[SUCCESS] Real Hardware Bridge Found.\033[0m")
        print("[LOG] Jarvis is now ready to access the physical microphone.")
    else:
        print("\033[1;31m[ERROR] API Bridge Missing! Run: pkg install termux-api\033[0m")

if __name__ == "__main__":
    check_real_mic()
