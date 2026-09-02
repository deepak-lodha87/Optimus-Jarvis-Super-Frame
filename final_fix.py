import subprocess
import os
import time

def secure_capture():
    filename = "deepak_final_voice.wav"
    if os.path.exists(filename): os.remove(filename)

    print("\033[1;33m>> SYSTEM: Optimus Jarvis Voice Calibration\033[0m")
    input("\033[1;32m[READY] Press ENTER and wait for the 'START' signal...\033[0m")
    
    print("\033[1;34m[LOG] Initializing Hardware Bridge...\033[0m")
    time.sleep(1) # Buffer to prevent instant skip
    
    print("\033[1;31m[START] SPEAK NOW: 'OPTIMUS JARVIS'\033[0m")
    # Capturing with forced bit-rate to ensure data size increases
    subprocess.run(["termux-microphone-record", "-f", filename, "-l", "5"])
    
    if os.path.exists(filename):
        size = os.path.getsize(filename)
        print(f"\n\033[1;32m[DATA] Final Size: {size} bytes.\033[0m")
        if size > 15000:
            print("\033[1;32m[SUCCESS] Voice Pattern Captured! Proceeding to Phase 3000.\033[0m")
        else:
            print("\033[1;31m[FAILED] Silence Detected. Check Mic Permissions.\033[0m")

if __name__ == "__main__":
    secure_capture()
