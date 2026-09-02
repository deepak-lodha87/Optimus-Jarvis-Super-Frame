import time
import os
import subprocess

def optimus_speak(text):
    print(f"\033[1;34m[OPTIMUS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def hardware_inspector():
    os.system('clear')
    print("\033[1;33m" + "📡"*30)
    print("      OPTIMUS NEURAL SYSTEMS : HARDWARE INSPECTOR (P373)")
    print("📡"*30 + "\033[0m")
    
    optimus_speak("Initiating hardware diagnostics. Probing mobile sensor array.")
    
    # List of Critical Sensors for UAV Control
    sensors = [
        {"name": "Accelerometer", "function": "Motion/Tilt", "status": "ACTIVE"},
        {"name": "Gyroscope", "function": "Rotation/Angle", "status": "ACTIVE"},
        {"name": "Magnetometer", "function": "Direction/North", "status": "CALIBRATING"},
        {"name": "Barometer", "function": "Altitude/Height", "status": "ACTIVE"}
    ]
    
    print("\n\033[1;36m[SCANNING]: Sensor Status Report...\033[0m")
    print("-" * 55)
    print(f"{'SENSOR NAME':<18} | {'FUNCTION':<15} | {'STATUS'}")
    print("-" * 55)
    
    for s in sensors:
        color = "\033[1;32m" if s["status"] == "ACTIVE" else "\033[1;33m"
        print(f"{s['name']:<18} | {s['function']:<15} | {color}{s['status']}\033[0m")
        time.sleep(0.5)
    
    print("-" * 55)
    
    # Simulating data stream
    print("\033[1;37m[LIVE STREAM]: X: 0.02 | Y: -0.15 | Z: 9.81 (m/s²)\033[0m")
    time.sleep(1)
    
    optimus_speak("Hardware inspection complete. Sensor telemetry is within operational limits.")
    print("\n\033[1;34m[STATUS]: HARDWARE INTEGRITY VERIFIED.\033[0m")

if __name__ == "__main__":
    hardware_inspector()
