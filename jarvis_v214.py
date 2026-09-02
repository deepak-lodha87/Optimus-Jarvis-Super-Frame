import os
import time

def smart_file_finder():
    print("\n" + "="*40)
    print("      JARVIS SMART FILE EXPLORER")
    print("="*40)
    
    msg_ask = "Commander Deepak, please specify the file name or keyword to search."
    print(f"\n[JARVIS]: {msg_ask}")
    os.system(f"termux-tts-speak '{msg_ask}'")
    
    keyword = input("\n[INPUT]: Search keyword: ").lower()
    
    print("\n[SYSTEM]: Scanning directory structure...")
    time.sleep(1)
    
    # फाइल सर्च लॉजिक
    all_files = os.listdir('.')
    found_files = [f for f in all_files if keyword in f.lower()]
    
    if found_files:
        print(f"\n[SUCCESS]: Found {len(found_files)} matching items:")
        for idx, file in enumerate(found_files, 1):
            print(f" {idx}. {file}")
        
        result_msg = f"Commander, I have located {len(found_files)} files related to your search."
        os.system(f"termux-tts-speak '{result_msg}'")
    else:
        fail_msg = "No matching files found in the current directory."
        print(f"\n[ERROR]: {fail_msg}")
        os.system(f"termux-tts-speak '{fail_msg}'")
        
    print("="*40)

if __name__ == "__main__":
    smart_file_finder()
