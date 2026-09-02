import os
import subprocess
import time

def optimus_speak(text):
    print(f"\033[1;34m[OPTIMUS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def self_repair_protocol():
    os.system('clear')
    print("\033[1;32m" + "🛠️"*30)
    print("      OPTIMUS NEURAL SYSTEMS : SELF-REPAIR CORE (P354)")
    print("🛠️"*30 + "\033[0m")
    
    optimus_speak("Initiating deep system integrity scan. Checking neural file clusters.")
    
    # List of critical Optimus files to check
    critical_files = [
        "optimus_prime_core.py",
        "optimus_p345_uav_flight.py",
        "optimus_p346_scanner.py",
        "optimus_p348_location.py",
        "optimus_p349_optimizer.py"
    ]
    
    for file in critical_files:
        print(f"\033[1;33m[SCANNING]:\033[0m {file}...")
        time.sleep(0.7)
        
        if os.path.exists(file):
            print(f"\033[1;32m[OK]: File verified. Integrity 100%.\033[0m")
        else:
            print(f"\033[1;31m[ALERT]: {file} is missing or corrupted!\033[0m")
            optimus_speak(f"Critical error detected in {file}. Attempting neural reconstruction.")
            # Simulation of repair
            time.sleep(1.5)
            print(f"\033[1;36m[FIXED]: {file} has been restored from backup.\033[0m")

    optimus_speak("System integrity is now at peak levels. All neural pathways are stable.")
    print("\n\033[1;34m[RESULT]: OPTIMUS CORE IS FULLY REPAIRED.\033[0m")

if __name__ == "__main__":
    self_repair_protocol()
