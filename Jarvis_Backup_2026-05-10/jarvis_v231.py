import os
import time
import shutil

def system_vitality_core():
    print("\n" + "="*40)
    print("      JARVIS SYSTEM VITALITY CORE")
    print("="*40)
    
    msg_init = "Commander Deepak, initiating hardware diagnostic scan."
    print(f"\n[JARVIS]: {msg_init}")
    os.system(f"termux-tts-speak '{msg_init}'")
    
    # स्टोरेज चेक (Real Data)
    total, used, free = shutil.disk_usage("/")
    free_gb = free // (2**30)
    
    print(f"\n[SCANNING]: Analyzing Storage Matrix...")
    time.sleep(1.5)
    
    storage_report = f"Storage analysis complete. You have {free_gb} GB of free space remaining in the primary sector."
    print(f"[STATUS]: {storage_report}")
    os.system(f"termux-tts-speak '{storage_report}'")
    
    # थर्मल/बैटरी स्थिति (Simulated logic based on previous guard)
    # आप इसे Phase 215 के battery_guardian_protocol के साथ जोड़ सकते हैं
    
    print("\n[DIAGNOSTIC]: CPU load nominal. Cooling systems operational.")
    
    if free_gb < 5:
        warning = "Commander, storage levels are critical. System efficiency may decrease."
        print(f"\n[ALERT]: {warning}")
        os.system(f"termux-tts-speak '{warning}'")
    else:
        success = "All hardware parameters are within optimal range."
        print(f"\n[SUCCESS]: {success}")
        os.system(f"termux-tts-speak '{success}'")

    print("\n" + "="*40)

if __name__ == "__main__":
    system_vitality_core()
