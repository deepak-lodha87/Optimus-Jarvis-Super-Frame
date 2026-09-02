import os
import time

def academic_memo_protocol():
    print("\n" + "="*40)
    print("      JARVIS ACADEMIC MEMO CREATOR")
    print("="*40)
    
    msg_ask = "Commander Deepak, please specify the subject and the topic detail."
    print(f"\n[JARVIS]: {msg_ask}")
    os.system(f"termux-tts-speak '{msg_ask}'")
    
    subject = input("\n[INPUT]: Subject (e.g., Sociology/Economics): ")
    detail = input("[INPUT]: Enter Note/Summary: ")
    
    # डेटा को एकेडेमिक फाइल में सेव करना
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    memo_entry = f"[{timestamp}] SUBJECT: {subject} | NOTE: {detail}\n"
    
    try:
        with open("academic_vault.txt", "a") as f:
            f.write(memo_entry)
        
        success = f"Academic note for {subject} has been archived, Commander."
        print(f"\n[JARVIS]: {success}")
        os.system(f"termux-tts-speak '{success}'")
        
    except Exception as e:
        print(f"[ERROR]: Protocol failed. {e}")

    # रिव्यु करने का विकल्प
    review = input("\n[JARVIS]: Access academic vault now? (y/n): ").lower()
    if review == 'y':
        if os.path.exists("academic_vault.txt"):
            print("\n" + "-"*30)
            with open("academic_vault.txt", "r") as f:
                print(f.read())
            print("-"*30)
        else:
            print("[EMPTY]: Vault is currently empty.")

if __name__ == "__main__":
    academic_memo_protocol()
