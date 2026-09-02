import subprocess
import os

def check_hardware():
    print("\033[1;33m>> SYSTEM: RE-SCANNING FOR VOICE HARDWARE INTERFACE...\033[0m")
    
    # Direct check for termux-api tools
    binary_path = "/data/data/com.termux/files/usr/bin/termux-microphone-record"
    
    if os.path.exists(binary_path):
        print("\033[1;32m[SUCCESS] Real Hardware Bridge Found at: " + binary_path + "\033[0m")
        print("[LOG] Jarvis is now authorized to access the physical mic.")
    else:
        print("\033[1;31m[ERROR] Hardware Link Missing!\033[0m")
        print("[FIX] Run this: pkg install termux-api")

if __name__ == "__main__":
    check_hardware()
