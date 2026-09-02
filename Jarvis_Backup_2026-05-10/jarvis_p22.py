import os
import subprocess
import time

def self_diagnosis():
    print("--- OPTIMUS JARVIS SUPER-FRAME: PHASE 22 ---")
    print("[LOG] Starting Self-Diagnosis Protocol...")
    time.sleep(1.5)

    # 1. Connectivity Check
    try:
        subprocess.check_output(['ping', '-c', '1', 'google.com'])
        net_status = "ONLINE"
    except:
        net_status = "OFFLINE (Network Defect Detected)"

    # 2. Battery Safety Check
    try:
        battery_data = subprocess.check_output(['termux-battery-status']).decode('utf-8')
        if '"health": "GOOD"' in battery_data:
            hw_status = "HEALTHY"
        else:
            hw_status = "HARDWARE WEAKNESS DETECTED"
    except:
        hw_status = "UNKNOWN (Termux-API missing)"

    print(f"\n[DIAGNOSIS REPORT]:")
    print(f"📡 Network Status: {net_status}")
    print(f"⚡ Hardware Status: {hw_status}")
    print(f"🛠  Status: {'SYSTEM READY' if net_status == 'ONLINE' else 'REPAIR REQUIRED'}")
    
    print("\n✅ Phase 22: Self-Diagnosis Tool Integrated.")

if __name__ == "__main__":
    self_diagnosis()
