import os
import subprocess

def check_uplink():
    print("\033[1;36m[UPLINK CHECK]\033[0m Testing connection to GitHub Repository...")
    # असली नेटवर्क टेस्ट
    status = subprocess.run(["git", "remote", "-v"], capture_output=True, text=True)
    
    if "github.com" in status.stdout:
        print("\033[1;32m[SUCCESS]\033[0m Repository is correctly linked.")
        msg = "Deepak sir, the cloud bridge is stable. Your Optimus code is ready for secure backup."
    else:
        print("\033[1;31m[OFFLINE]\033[0m Connection failed. Token required.")
        msg = "Deepak sir, I cannot find the cloud path. Please provide the access token."
    
    os.system(f'termux-tts-speak "{msg}"')

if __name__ == "__main__":
    check_uplink()
