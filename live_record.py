import subprocess
import os
import time

def start_pulse_capture():
    print("\033[1;33m>> INITIATING PULSE CAPTURE: Phase 2997\033[0m")
    filename = "deepak_voice.wav"
    
    # Cleaning old samples
    if os.path.exists(filename):
        os.remove(filename)
    
    print("\033[1;36m[ACTION]: Speak 'OPTIMUS JARVIS' into the mic in 3 seconds...\033[0m")
    time.sleep(3)
    
    print("\033[1;31m[RECORDING STARTED] - Speak Now...\033[0m")
    # Using termux-microphone-record for 5 seconds
    subprocess.run(["termux-microphone-record", "-f", filename, "-l", "5"])
    
    if os.path.exists(filename):
        print("\033[1;32m\n[SUCCESS] Audio Pulse Captured and Saved as: " + filename + "\033[0m")
        file_size = os.path.getsize(filename)
        print(f"[DATA] Captured Size: {file_size} bytes.")
    else:
        print("\033[1;31m[ERROR] No data captured. Check permissions!\033[0m")

if __name__ == "__main__":
    start_pulse_capture()
