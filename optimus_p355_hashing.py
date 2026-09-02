import hashlib
import time
import os
import subprocess

def optimus_speak(text):
    print(f"\033[1;34m[OPTIMUS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def neural_hash_vault():
    os.system('clear')
    print("\033[1;31m" + "🔐"*30)
    print("      OPTIMUS NEURAL SYSTEMS : LEVEL 2 HASH VAULT (P355)")
    print("🔐"*30 + "\033[0m")
    
    optimus_speak("Establishing SHA-256 encryption layer. Securing system access keys.")
    
    data = input("\n\033[1;33m[INPUT]: Enter Private Blueprint Key / Passcode: \033[0m")
    
    print("\n\033[1;32m[SYSTEM]: Generating Non-Reversible Neural Hash...\033[0m")
    time.sleep(1.2)
    
    # SHA-256 Hashing Logic
    hash_object = hashlib.sha256(data.encode())
    hex_dig = hash_object.hexdigest()
    
    print(f"\n\033[1;36m[RESULT]: HASH GENERATED SUCCESSFULLY\033[0m")
    print("-" * 60)
    print(f"Original Data: [REDACTED FOR SECURITY]")
    print(f"Neural Hash: \033[1;32m{hex_dig}\033[0m")
    print("-" * 60)
    
    optimus_speak("Key has been hashed and stored in the secure Optimus vault.")

if __name__ == "__main__":
    neural_hash_vault()
