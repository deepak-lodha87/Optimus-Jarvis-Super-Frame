import os
import subprocess
import time

def jarvis_speak(text):
    print(f"\033[1;34m[JARVIS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def main_menu():
    while True:
        os.system('clear')
        print("\033[1;36m" + "="*50)
        print("      OPTIMUS JARVIS SUPER-FRAME : PHASE 340")
        print("              MASTER CONTROL CENTER")
        print("="*50 + "\033[0m")
        print("\n\033[1;32m[1]\033[0m Biometric Authentication (Face Unlock)")
        print("\033[1;32m[2]\033[0m Asset Registry (Vehicle/Drone Blueprints)")
        print("\033[1;32m[3]\033[0m Tactical Scan (Real-time News/Status)")
        print("\033[1;32m[4]\033[0m Self-Diagnosis (Repair Assistance)")
        print("\033[1;32m[5]\033[0m Neural Memory (Project Archive)")
        print("\033[1;32m[6]\033[0m Cloud Sync (GitHub Backup)")
        print("\033[1;31m[0]\033[0m Shutdown System")
        print("\n" + "="*50)

        choice = input("\033[1;33m[COMMAND]: Select Protocol: \033[0m")

        if choice == '1':
            os.system('python jarvis_p334_faceid.py')
        elif choice == '2':
            os.system('python jarvis_p336_database.py')
        elif choice == '3':
            os.system('python jarvis_v331_scanner.py')
        elif choice == '4':
            os.system('python jarvis_p337_diagnosis.py')
        elif choice == '5':
            os.system('python jarvis_p339_memory.py')
        elif choice == '6':
            os.system('./jarvis_p338_cloud_sync.sh')
        elif choice == '0':
            jarvis_speak("Powering down all systems. Sleep well, Deepak.")
            break
        else:
            print("\033[1;31m[ERROR]: Invalid Protocol Selection.\033[0m")
            time.sleep(1)

if __name__ == "__main__":
    jarvis_speak("All systems are operational. Master Core is online.")
    main_menu()
