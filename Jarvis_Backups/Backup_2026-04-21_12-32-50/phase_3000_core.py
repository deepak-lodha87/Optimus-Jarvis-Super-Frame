import subprocess
import os

def final_attempt():
    print("\033[1;35m>> ARCHITECT DEEPAK: WELCOME TO PHASE 3000 PREPARATION <<\033[0m")
    filename = "test.wav"
    
    # Try recording without a sub-shell to catch direct errors
    try:
        print("[LOG] Testing direct hardware path...")
        result = subprocess.run(["termux-microphone-record", "-f", filename, "-l", "2"])
        if result.returncode != 0:
            print("\033[1;31m[CRITICAL] Android is blocking Termux! Check 'Draw over other apps' & 'Mic' permissions.\033[0m")
        else:
            print("\033[1;32m[SUCCESS] Hardware Path Clear. Ready for Infinite Expansion.\033[0m")
    except Exception as e:
        print(f"[ERROR] System Error: {e}")

if __name__ == "__main__":
    final_attempt()
