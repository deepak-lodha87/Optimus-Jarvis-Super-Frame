import os
import shutil

def self_diagnosis():
    print("\n" + "="*50)
    print("|    JARVIS PHASE 139: SELF-DIAGNOSIS SYSTEM     |")
    print("="*50)

    # 1. Checking Storage (Phase 129 reference)
    total, used, free = shutil.disk_usage("/")
    usage_pct = (used / total) * 100
    print(f"[STORAGE]: {usage_pct:.2f}% Used")

    # 2. Hardware Scan Simulation
    print("[HARDWARE]: Scanning camera and sensors...")
    # Simulation of checking Termux-API tools
    camera_check = os.system("command -v termux-camera-info > /dev/null")
    
    if camera_check == 0:
        status = "ALL SYSTEMS NOMINAL"
        msg = "Commander, internal systems are healthy and future-ready."
    else:
        status = "DEFECT DETECTED"
        msg = "Termux-API tools missing. Please run 'pkg install termux-api'."

    print(f"\n[STATUS]: {status}")
    print(f"[JARVIS]: {msg}")
    os.system(f"termux-tts-speak '{msg}'")

if __name__ == "__main__":
    self_diagnosis()
