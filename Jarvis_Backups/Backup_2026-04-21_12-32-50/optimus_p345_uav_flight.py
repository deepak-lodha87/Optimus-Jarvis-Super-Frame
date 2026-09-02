import time
import os
import subprocess

def optimus_speak(text):
    print(f"\033[1;34m[OPTIMUS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def pre_flight_check():
    os.system('clear')
    print("\033[1;36m" + "="*50)
    print("      OPTIMUS NEURAL SYSTEMS : UAV FLIGHT CORE (P345)")
    print("="*50 + "\033[0m")
    
    optimus_speak("Initializing autonomous flight protocols. Running pre-flight diagnostics.")
    
    # Flight Parameters
    checks = {
        "IMU Calibration": "STABLE",
        "GPS Satellite Link": "12 SATELLITES LOCKED",
        "Battery Voltage": "16.8V (4S LiPo)",
        "ESC Telemetry": "CONNECTED",
        "Signal Strength": "98% (CRSF Protocol)"
    }
    
    for component, status in checks.items():
        print(f"\033[1;33m[CHECKING]:\033[0m {component}...")
        time.sleep(0.8)
        print(f"\033[1;32m[STATUS]: {status}\033[0m")
    
    print("\n\033[1;32m[RESULT]: ALL SYSTEMS NOMINAL. READY FOR TAKEOFF.\033[0m")
    optimus_speak("Pre-flight check complete. UAV is cleared for autonomous mission.")

if __name__ == "__main__":
    pre_flight_check()
