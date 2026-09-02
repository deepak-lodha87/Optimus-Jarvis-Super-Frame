import shutil
import time

def check_storage():
    total, used, free = shutil.disk_usage("/")
    return total, used, free

def jarvis_storage_scan():
    print("--- OPTIMUS JARVIS SUPER-FRAME: PHASE 21 ---")
    print("[LOG] Scanning Internal Memory Matrix...")
    time.sleep(1)
    
    total, used, free = check_storage()
    
    # Converting bytes to GB
    print(f"\n[SYSTEM] Storage Analysis:")
    print(f"📁 Total Space: {total // (2**30)} GB")
    print(f"📊 Used Space: {used // (2**30)} GB")
    print(f"🆓 Free Space: {free // (2**30)} GB")
    
    print("\n✅ Phase 21: Storage Intelligence Integrated.")

if __name__ == "__main__":
    jarvis_storage_scan()
