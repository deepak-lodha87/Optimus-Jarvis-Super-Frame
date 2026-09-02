import os
import time

def system_reboot_protocol():
    print("\n" + "="*40)
    print("      JARVIS SYSTEM REBOOT INTERFACE")
    print("="40)
    
    msg_confirm = "Commander Deepak, do you wish to initiate a full system refresh?"
    print(f"\n[JARVIS]: {msg_confirm}")
    os.system(f"termux-tts-speak '{msg_confirm}'")
    
    confirm = input("\n[INPUT]: Type 'REBOOT' to confirm: ").upper()
    
    if confirm == 'REBOOT':
        print("\n" + "-"*40)
        reboot_msg = "Initiating core refresh. Closing all active sub-routines..."
        print(f"[PROCESS]: {reboot_msg}")
        os.system(f"termux-tts-speak '{reboot_msg}'")
        
        # सिमुलेटेड प्रोग्रेस बार
        for i in range(1, 6):
            print(f"[REBOOTING]: {'█' * (i * 8)} {i*20}%", end='\r')
            time.sleep(0.8)
        
        print("\n\n[SUCCESS]: All cores synchronized. Optimus Jarvis is back online.")
        os.system("termux-tts-speak 'System reboot complete. All cores online, Commander.'")
    else:
        print("\n[CANCELLED]: Reboot aborted by Commander.")

    print("\n" + "="*40)

if __name__ == "__main__":
    system_reboot_protocol()
