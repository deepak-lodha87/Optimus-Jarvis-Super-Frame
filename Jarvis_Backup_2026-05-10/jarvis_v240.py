import os
import time

def master_command_center():
    while True:
        print("\n" + "="*45)
        print("      OPTIMUS JARVIS MASTER COMMAND CENTER")
        print("="*45)
        
        msg_greet = "Commander Deepak, Master Core is active. Awaiting your selection."
        print(f"\n[JARVIS]: {msg_greet}")
        os.system(f"termux-tts-speak '{msg_greet}'")
        
        print("\n[ACTIVE CORES]:")
        print("1. Security Core (Lockdown/Biometrics/Firewall)")
        print("2. Academic Hub (Quiz/Study Logs)")
        print("3. System Vitality (Storage/Diagnostics/Reboot)")
        print("4. Utility Core (Weather/Expenses/Reminders)")
        print("5. Neural Intent Parser (Analysis)")
        print("Q. Exit Master Center")
        
        choice = input("\n[INPUT]: Select Sector (1-5 or Q): ").upper()
        
        if choice == '1':
            print("\n[ROUTING]: Accessing Security Protocols...")
            # यहाँ आप अपने security modules को import/call कर सकते हैं
        elif choice == '2':
            print("\n[ROUTING]: Opening Academic Database...")
        elif choice == '3':
            print("\n[ROUTING]: Running System Health Check...")
        elif choice == '4':
            print("\n[ROUTING]: Fetching Daily Utilities...")
        elif choice == '5':
            print("\n[ROUTING]: Activating Intent Analysis...")
        elif choice == 'Q':
            msg_exit = "Powering down Master Center. Stay safe, Commander."
            print(f"\n[JARVIS]: {msg_exit}")
            os.system(f"termux-tts-speak '{msg_exit}'")
            break
        else:
            print("\n[ERROR]: Invalid sector selection.")
            
        time.sleep(2)

if __name__ == "__main__":
    master_command_center()
