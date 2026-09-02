import os
import shutil
import json

def check_storage():
    # Get disk usage statistics
    total, used, free = shutil.disk_usage("/")
    
    # Calculate percentage
    used_percent = (used / total) * 100
    free_gb = free // (2**30)
    
    print("\n" + "="*40)
    print("║   JARVIS PHASE 129: STORAGE SENSE    ║")
    print("="*40)
    
    msg = f"Commander, current free storage is {free_gb} GB. System integrity is stable."
    
    if used_percent > 90:
        msg = f"Alert! Storage is critical. Only {free_gb} GB left. Please clear some space."
        print(f"[CRITICAL]: {msg}")
    else:
        print(f"[SYSTEM]: {msg}")

    # Voice output via Termux-TTS
    os.system(f"termux-tts-speak '{msg}'")

if __name__ == "__main__":
    check_storage()
