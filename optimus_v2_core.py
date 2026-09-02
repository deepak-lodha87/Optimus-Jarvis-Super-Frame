import os
import subprocess
import time

def optimus_speak(text):
    print(f"\033[1;34m[OPTIMUS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def master_dashboard_v2():
    while True:
        os.system('clear')
        print("\033[1;36m" + "⣿" * 60)
        print("          OPTIMUS NEURAL SYSTEMS : COMMAND CENTER v2.0")
        print("                 ADVANCED ANALYTICS & DEFENSE")
        print("⣿" * 60 + "\033[0m")
        
        # Live Telemetry Stream Simulation
        print(f"\n\033[1;32m[LOG]:\033[0m Neural Sync Active | \033[1;32m[TMP]:\033[0m 36.4°C | \033[1;32m[AUTH]:\033[0m VERIFIED")
        print("-" * 60)
        
        print("\033[1;33m[01]\033[0m VOICE IDENTITY SCAN  (Biometric Auth)")
        print("\033[1;33m[02]\033[0m LOGISTICS & INVENTORY (Asset Tracking)")
        print("\033[1;33m[03]\033[0m THERMAL SHIELD        (Hardware Safety)")
        print("\033[1;33m[04]\033[0m CLOUD ARCHIVE SYNC    (GitHub Pro)")
        print("\033[1;33m[05]\033[0m PREDICTIVE ANALYSIS   (Maintenance)")
        print("\033[1;33m[06]\033[0m DATA ENCRYPTION VAULT (SHA-256)")
        print("\033[1;31m[00]\033[0m DEACTIVATE ALL NEURAL PATHWAYS")
        print("-" * 60)

        choice = input("\n\033[1;37m[SYSTEM]: SELECT PROTOCOL: \033[0m")

        if choice == '1':
            os.system('python optimus_p358_voice_id.py')
        elif choice == '2':
            os.system('python optimus_p359_inventory.py')
        elif choice == '3':
            os.system('python optimus_p357_thermal.py')
        elif choice == '4':
            os.system('bash optimus_p356_cloud_pro.sh')
        elif choice == '5':
            os.system('python optimus_p351_predictive.py')
        elif choice == '6':
            os.system('python optimus_p355_hashing.py')
        elif choice == '0':
            optimus_speak("Initiating full system shutdown. All Optimus protocols disengaged.")
            print("\033[1;31m[OFFLINE]: Optimus Core Terminated.\033[0m")
            break
        else:
            print("\033[1;31m[ERROR]: Protocol not recognized.\033[0m")
            time.sleep(1)

if __name__ == "__main__":
    optimus_speak("Optimus Command Center version 2.0 is now online. All neural links are stable.")
    master_dashboard_v2()
