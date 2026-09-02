import subprocess
import os
import time

def save_master_voice():
    print("\033[1;35m>> SYSTEM: PHASE 3001 - FINAL VOICE ENROLLMENT <<\033[0m")
    filename = "master_identity.wav"
    
    if os.path.exists(filename): os.remove(filename)

    print("\033[1;36m[READY] Jarvis is listening. Prepare to speak...\033[0m")
    time.sleep(1)
    
    print("\033[1;31m[!!! SPEAK NOW !!!]\033[0m")
    print("Command: 'Optimus Jarvis, Initiate Voice Protocol. System Access: Deepak.'")
    
    # Recording for 7 seconds to capture the full sentence
    subprocess.run(["termux-microphone-record", "-f", filename, "-l", "7"])
    
    if os.path.exists(filename):
        size = os.path.getsize(filename)
        if size > 30000: # Ensuring actual voice data is there
            print(f"\n\033[1;32m[SUCCESS] Master Voice Profile Created! ({size} bytes)\033[0m")
            print("\033[1;32m>> STATUS: DEEPAK VERIFIED AS ARCHITECT <<\033[0m")
        else:
            print("\033[1;31m[FAILED] Data too small. Please speak louder and clearly.\033[0m")
    else:
        print("[ERROR] Hardware failed to write file.")

if __name__ == "__main__":
    save_master_voice()
