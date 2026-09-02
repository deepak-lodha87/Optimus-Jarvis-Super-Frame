import subprocess
import time

def get_battery_status():
    try:
        # Termux battery status command
        status = subprocess.check_output(['termux-battery-status']).decode('utf-8')
        return status
    except:
        return "Battery data unavailable. (Ensure termux-api is installed)"

def jarvis_env_scan():
    print("--- OPTIMUS JARVIS SUPER-FRAME: PHASE 19 ---")
    print("[LOG] Initiating Environmental Awareness Scan...")
    time.sleep(1)
    
    battery = get_battery_status()
    print(f"\n[SYSTEM] Hardware Integrity Check:")
    print(f"🔋 {battery}")
    
    print("\n✅ Phase 19: Environmental Core Integrated.")

if __name__ == "__main__":
    jarvis_env_scan()
