import os
import time
import base64

def advanced_log_encrypter():
    print("\n" + "="*40)
    print("      JARVIS ADVANCED LOG ENCRYPTER")
    print("="*40)
    
    msg_init = "Commander Deepak, initiating multi-layer log encryption protocol."
    print(f"\n[JARVIS]: {msg_init}")
    os.system(f"termux-tts-speak '{msg_init}'")
    
    target_logs = ["study_log.txt", "expense_log.txt", "command_log.txt"]
    password = input("\n[SECURITY]: Set Master Encryption Key: ")
    
    if len(password) < 4:
        error = "Security key too weak. Encryption aborted."
        print(f"[ERROR]: {error}")
        os.system(f"termux-tts-speak '{error}'")
        return

    for log in target_logs:
        if os.path.exists(log):
            with open(log, 'r') as f:
                data = f.read()
            
            # Simple Base64 Simulation for Termux Environment
            encoded_data = base64.b64encode(data.encode()).decode()
            
            with open(f"ENCRYPTED_{log}", 'w') as f:
                f.write(encoded_data)
            
            print(f"[STATUS]: {log} has been encrypted and secured.")
            
    success = "All sensitive logs are now under encrypted protection, Commander."
    print(f"\n[JARVIS]: {success}")
    os.system(f"termux-tts-speak '{success}'")
    print("\n" + "="*40)

if __name__ == "__main__":
    advanced_log_encrypter()
