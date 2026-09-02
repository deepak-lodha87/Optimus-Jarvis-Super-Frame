import subprocess
import os

def start_manual_capture():
    print("\033[1;33m>> SYSTEM: Optimus Jarvis Voice Calibration\033[0m")
    filename = "deepak_final_voice.wav"
    
    if os.path.exists(filename):
        os.remove(filename)

    print("\033[1;36m[READY] Jarvis is listening but waiting for your signal.\033[0m")
    input("\033[1;32m[ACTION] Press ENTER and then IMMEDIATELY speak 'OPTIMUS JARVIS'...\033[0m")
    
    print("\033[1;31m[RECORDING...] Speak Now (5 Seconds Active)\033[0m")
    
    # Real-time capture without the dumb timer delay before recording
    subprocess.run(["termux-microphone-record", "-f", filename, "-l", "5"])
    
    if os.path.exists(filename):
        size = os.path.getsize(filename)
        print(f"\n\033[1;32m[SUCCESS] Captured: {size} bytes.\033[0m")
        if size > 25000:
            print("[LOG] Clear Voice Data Found. Proceeding to Phase 3000.")
        else:
            print("\033[1;31m[REJECTED] Too quiet. Please try again with more volume.\033[0m")
    else:
        print("[ERROR] Capture failed.")

if __name__ == "__main__":
    start_manual_capture()
