import os
import subprocess

def optimus_speak(text):
    subprocess.run(['termux-tts-speak', text])

def main_interface():
    os.system('clear')
    print("\033[1;34m" + "■"*60)
    print("           OPTIMUS NEURAL SYSTEMS : MASTER CORE v1.5")
    print("■"*60 + "\033[0m")
    
    print("\n\033[1;32m[01]\033[0m SECURITY OVERRIDE (Passcode Unlock)")
    print("\033[1;32m[02]\033[0m BLUEPRINT SCANNER (Technical Data)")
    print("\033[1;32m[03]\033[0m UAV FLIGHT CORE (Drone Telemetry)")
    print("\033[1;32m[04]\033[0m NEURAL MEMORY (Archive)")
    print("\033[1;31m[00]\033[0m DEACTIVATE SYSTEM")
    
    choice = input("\n\033[1;33m[PROTOCOL]: Selection? \033[0m")
    
    if choice == '1':
        os.system('python jarvis_p334_faceid.py')
    elif choice == '2':
        os.system('python optimus_p346_scanner.py')
    elif choice == '3':
        os.system('python optimus_p345_uav_flight.py')
    elif choice == '4':
        os.system('python jarvis_p339_memory.py')
    elif choice == '0':
        print("Optimus Core: Shutting down.")
        exit()

if __name__ == "__main__":
    main_interface()
