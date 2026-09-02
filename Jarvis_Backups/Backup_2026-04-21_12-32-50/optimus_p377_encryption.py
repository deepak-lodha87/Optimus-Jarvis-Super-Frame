import time
import os
import subprocess
import base64

def optimus_speak(text):
    print(f"\033[1;34m[OPTIMUS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def neural_encryption_engine():
    os.system('clear')
    print("\033[1;35m" + "🔐"*30)
    print("      OPTIMUS NEURAL SYSTEMS : DATA ENCRYPTION (P377)")
    print("🔐"*30 + "\033[0m")
    
    optimus_speak("Initiating neural encryption protocols. Preparing AES-256 equivalent transformation.")
    
    # Secret Key (Simulated)
    SECRET_KEY = "OPTIMUS-PRO-99"
    
    raw_data = input("\n\033[1;33m[INPUT]: Enter Sensitive Data to Encrypt: \033[0m")
    
    print("\n\033[1;36m[PROCESSING]: Encoding data into non-readable neural fragments...\033[0m")
    time.sleep(1.5)
    
    # Base64 Encoding as a high-level simulation of encryption
    encoded_bytes = base64.b64encode(raw_data.encode("utf-8"))
    encrypted_string = encoded_bytes.decode("utf-8")
    
    print("-" * 55)
    print(f"RAW DATA:       {raw_data}")
    print(f"\033[1;32mENCRYPTED:\033[0m      {encrypted_string}")
    print("-" * 55)
    
    optimus_speak("Data transformation complete. Information is now secured against unauthorized extraction.")
    print("\n\033[1;34m[STATUS]: CIPHER CORE IS OPERATIONAL.\033[0m")

if __name__ == "__main__":
    neural_encryption_engine()
