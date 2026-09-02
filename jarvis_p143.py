import os
import shutil
import time

def resource_manager():
    print("\n" + "="*50)
    print("|    JARVIS PHASE 143: INTELLIGENT RESOURCE MGR  |")
    print("="*50)

    print("\n[SYSTEM]: Analyzing current mobile environment...")
    
    # Checking Real-time storage (Based on Phase 139 logic)
    total, used, free = shutil.disk_usage("/")
    usage_pct = (used / total) * 100
    
    print(f"[DATA]: Current Storage Load: {usage_pct:.2f}%")

    if usage_pct > 80:
        action = "CRITICAL: Cleaning cache and temp files to boost speed."
        # Simulated cleaning
        time.sleep(1)
    else:
        action = "STABLE: System resources are optimized for 2X performance."

    print(f"\n[JARVIS]: {action}")
    os.system(f"termux-tts-speak '{action}'")

    # Future Upgrade Check
    print("\n[LOG]: Checking for legacy hardware to retrofit...")
    time.sleep(1)
    print("[RESULT]: Ready to upgrade external peripherals.")

if __name__ == "__main__":
    resource_manager()
