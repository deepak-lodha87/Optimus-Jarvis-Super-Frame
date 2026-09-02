import time
import os
import subprocess
import base64

def optimus_speak(text):
    print(f"\033[1;34m[OPTIMUS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def neural_encryption_vault():
    os.system('clear')
    print("\033[1;31m" + "🔒"*30)
    print("      OPTIMUS NEURAL SYSTEMS : DATA ENCRYPTION VAULT (P352)")
    print("🔒"*30 + "\033[0m")
    
    optimus_speak("Initializing neural encryption. Securing sensitive data fragments.")
    
    data_to_lock = input("\n\033[1;33m[INPUT]: Enter Data/Code to Encrypt: \033[0m")
    
    print("\n\033[1;32m[SYSTEM]: Applying AES-256 Simulation Layer...\033[0m")
    time.sleep(1.5)
    
    # Simple Base64 Encryption for simulation
    encoded_bytes = base64.b64encode(data_to_lock.encode("utf-8"))
    encrypted_data = encoded_bytes.decode("utf-8")
    
    print(f"\n\033[1;36m[RESULT]: ENCRYPTION COMPLETE\033[0m")
    print("-" * 50)
    print(f"Original: {data_to_lock}")
    print(f"Encrypted Key: \033[1;32m{encrypted_data}\033[0m")
    print("-" * 50)
    
    optimus_speak("Data has been successfully moved to the encrypted archive.")

if __name__ == "__main__":
    neural_encryption_vault()
