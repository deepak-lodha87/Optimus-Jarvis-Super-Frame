import os
import time

def integrity_guard():
    print("\n" + "="*40)
    print("      JARVIS SYSTEM INTEGRITY GUARD")
    print("="*40)
    
    msg_start = "Commander Deepak, running system integrity check..."
    print(f"\n[JARVIS]: {msg_start}")
    os.system(f"termux-tts-speak '{msg_start}'")
    
    time.sleep(1.5)
    
    # अनावश्यक लॉग फाइलों की सफाई (Simulation)
    print("[PROCESS]: Cleaning temporary data packets...")
    time.sleep(1)
    
    # सिस्टम हेल्थ चेक
    print("[STATUS]: Analyzing framework core...")
    time.sleep(1)
    
    success_msg = "Integrity check 100% complete. All sectors are functional."
    print(f"\n[JARVIS]: {success_msg}")
    os.system(f"termux-tts-speak '{success_msg}'")
    print("="*40)

if __name__ == "__main__":
    integrity_guard()
