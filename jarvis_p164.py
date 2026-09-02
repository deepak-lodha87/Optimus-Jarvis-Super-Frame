import os
import time

def self_destruct_protocol():
    print("\n" + "!"*50)
    print("!    JARVIS PHASE 164: VIRTUAL SELF-DESTRUCT    !")
    print("!"*50)

    failed_attempts = 3 # Simulating 3 failed biometric attempts
    print(f"\n[ALERT]: {failed_attempts} Unauthorized access attempts detected.")
    
    msg = "Commander, security breached. Initiating Virtual Self-Destruct to protect the core logic."
    print(f"\n[JARVIS]: {msg}")
    os.system(f"termux-tts-speak '{msg}'")

    print("\n[ACTION]: Encrypting and Moving Phase 1-163 data to Deep Vault...")
    time.sleep(1.5)
    
    # Simulating data purge
    print("[SYSTEM]: Purging local interface files...")
    time.sleep(1)
    
    final_msg = "Core purged. Jarvis is now offline. Only physical biometric reset can restore system."
    print(f"\n[FINAL STATUS]: {final_msg}")
    os.system(f"termux-tts-speak '{final_msg}'")

    print("\n" + "!"*50)
    print("!             SYSTEM TERMINATED                !")
    print("!"*50)

if __name__ == "__main__":
    self_destruct_protocol()
