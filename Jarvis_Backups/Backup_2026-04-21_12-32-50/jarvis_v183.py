import time
import random
import os

def data_eraser_protocol():
    print("\n[CLEANUP]: Initiating Log Eraser...")
    time.sleep(1)
    temp_files = ["cache.tmp", "session_log.txt", "trace.db"]
    for file in temp_files:
        print(f" -> Scrubbing {file}...")
        time.sleep(0.3)
    print("[SUCCESS]: Digital footprints removed. System is clean.")

def stealth_ghost_protocol():
    print("\n" + "="*50)
    print("|    JARVIS PHASE 183: LOG ERASER & STEALTH    |")
    print("="*50)
    print("[SYSTEM]: Ghost Protocol v2.0 engaged.")
    time.sleep(1)
    
    # Commander Deepak's custom message
    stealth_msg = "Commander Deepak, Mission complete. Erasing all traces now."
    print(f"\n[JARVIS]: {stealth_msg}")
    os.system(f"termux-tts-speak '{stealth_msg}'")
    
    # Cleanup before shutdown
    data_eraser_protocol()
    print("="*50)

if __name__ == "__main__":
    stealth_ghost_protocol()
