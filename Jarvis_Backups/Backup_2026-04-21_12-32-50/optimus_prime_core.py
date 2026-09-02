import os
import subprocess
import time

def optimus_speak(text):
    print(f"\033[1;34m[OPTIMUS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def main_dashboard():
    while True:
        os.system('clear')
        print("\033[1;36m" + "█" * 60)
        print("          OPTIMUS NEURAL SYSTEMS : PRIME CORE v1.0")
        print("                 GLOBAL COMMAND INTERFACE")
        print("█" * 60 + "\033[0m")
        
        # System Health Status
        print(f"\n\033[1;32m[STATUS]:\033[0m Neural Pathways Secure | \033[1;32m[UPLINK]:\033[0m Satellite Active")
        print("-" * 60)
        
        print("\033[1;33m[01]\033[0m SECURITY PROTOCOL  (Defense Core / Override)")
        print("\033[1;33m[02]\033[0m BLUEPRINT SCANNER  (UAV & Vehicle Data)")
        print("\033[1;33m[03]\033[0m FLIGHT TELEMETRY  (Autonomous UAV Logic)")
        print("\033[1;33m[04]\033[0m SATELLITE SYNC    (GPS & Location Tracking)")
        print("\033[1;33m[05]\033[0m RESOURCE OPTIMIZER (Hardware Diagnostics)")
        print("\033[1;33m[06]\033[0m ENVIRONMENTAL DATA (Atmospheric Sync)")
        print("\033[1;31m[00]\033[0m DEACTIVATE CORE")
        print("-" * 60)

        choice = input("\n\033[1;37m[INPUT]: Execute Protocol Number: \033[0m")

        if choice == '1':
            os.system('python optimus_p344_security.py')
        elif choice == '2':
            os.system('python optimus_p346_scanner.py')
        elif choice == '3':
            os.system('python optimus_p345_uav_flight.py')
        elif choice == '4':
            os.system('python optimus_p348_location.py')
        elif choice == '5':
            os.system('python optimus_p349_optimizer.py')
        elif choice == '6':
            os.system('python jarvis_p342_weather.py') # Background function
        elif choice == '0':
            optimus_speak("Deactivating all neural pathways. System offline.")
            print("\033[1;31m[OFFLINE]: Optimus Core Disengaged.\033[0m")
            break
        else:
            print("\033[1;31m[ERROR]: Invalid selection. Retry.\033[0m")
            time.sleep(1)

if __name__ == "__main__":
    optimus_speak("Optimus Prime Core is operational. Welcome back, Deepak.")
    main_dashboard()
