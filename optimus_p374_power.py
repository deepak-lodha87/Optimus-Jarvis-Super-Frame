import time
import os
import subprocess

def optimus_speak(text):
    print(f"\033[1;34m[OPTIMUS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def power_management_engine():
    os.system('clear')
    print("\033[1;33m" + "🔋"*30)
    print("      OPTIMUS NEURAL SYSTEMS : POWER MANAGEMENT (P374)")
    print("🔋"*30 + "\033[0m")
    
    optimus_speak("Accessing power management interface. Analyzing discharge patterns.")
    
    # Simulated Real-time Battery Data
    battery_stats = {
        "Capacity": "5000mAh",
        "Current Level": 82,
        "Voltage": "3.85V",
        "Health": "Good",
        "Temp": "34.2°C"
    }
    
    # Estimated Runtime Calculation (Simulated Logic)
    est_runtime_mins = (battery_stats["Current Level"] * 6.5) # Logic: 1% = 6.5 mins
    hours = int(est_runtime_mins // 60)
    mins = int(est_runtime_mins % 60)
    
    print(f"\n\033[1;36m[REPORT]: ENERGY CONSUMPTION METRICS\033[0m")
    print("-" * 50)
    for key, value in battery_stats.items():
        print(f"{key:<18}: {value}")
        time.sleep(0.4)
    print("-" * 50)
    
    print(f"\033[1;32m[PROJECTION]: ESTIMATED SYSTEM UPTIME:\033[0m {hours}h {mins}m")
    
    if battery_stats["Current Level"] < 20:
        optimus_speak("Critical energy reserves. Activating low-power neural mode.")
    else:
        optimus_speak("Power supply is optimal. Neural cores are fully energized.")

if __name__ == "__main__":
    power_management_engine()
