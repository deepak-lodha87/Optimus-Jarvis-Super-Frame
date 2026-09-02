import os
import time

def ghost_protocol_emergency():
    print("\n" + "="*45)
    print("      JARVIS EMERGENCY GHOST PROTOCOL")
    print("="*45)
    
    msg_alert = "Commander Deepak, critical security breach detected. Initiating Ghost Protocol?"
    print(f"\n[JARVIS]: {msg_alert}")
    os.system(f"termux-tts-speak '{msg_alert}'")
    
    confirm = input("\n[SECURITY]: Enter Master Key to ABORT or 'WIPE' to execute: ")
    
    if confirm == "WIPE":
        print("\n[PROCESS]: Searching for sensitive encrypted logs...")
        # उन फाइलों को ढूंढना जो Phase 238 में एन्क्रिप्ट की गई थीं
        targets = [f for f in os.listdir('.') if f.startswith('ENCRYPTED_')]
        
        if not targets:
            print("[STATUS]: No sensitive data found. System is already clean.")
        else:
            for file in targets:
                print(f"[ACTION]: Shredding {file}...")
                os.remove(file)
                time.sleep(0.5)
            
            success = "Ghost Protocol successful. All sensitive logs have been vaporized."
            print(f"\n[SUCCESS]: {success}")
            os.system(f"termux-tts-speak '{success}'")
    else:
        print("\n[STATUS]: Ghost Protocol aborted. Systems returning to normal.")

    print("\n" + "="*45)

if __name__ == "__main__":
    ghost_protocol_emergency()
