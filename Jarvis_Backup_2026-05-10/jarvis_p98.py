import os
import time

def speak(text):
    print(f"[JARVIS]: {text}")
    os.system(f"termux-tts-speak '{text}'")

def file_vault():
    print("--- OPTIMUS JARVIS SUPER-FRAME: PHASE 98 ---")
    print("--- [INITIALIZING ENCRYPTED FILE VAULT] ---")
    
    master_pass = "stark123"
    
    print("\n1. Lock a File (Hide Content)")
    print("2. Unlock a File (Show Content)")
    choice = input("\nMaster, select an option: ")

    filename = input("📄 Enter the filename: ")

    if not os.path.exists(filename):
        speak("माफ़ कीजिये, यह फाइल मौजूद नहीं है।")
        return

    password = input("🔐 Enter Vault Password: ")

    if password == master_pass:
        if choice == '1':
            # फाइल को रीनेम करके 'छिपा' देना
            if not filename.endswith(".locked"):
                os.rename(filename, filename + ".locked")
                speak("फाइल को सफलतापूर्वक लॉक कर दिया गया है।")
            else:
                speak("फाइल पहले से ही लॉक है।")
        
        elif choice == '2':
            # फाइल को वापस सामान्य करना
            if filename.endswith(".locked"):
                new_name = filename.replace(".locked", "")
                os.rename(filename, new_name)
                speak("फाइल अनलॉक हो गई है। अब आप इसे पढ़ सकते हैं।")
            else:
                speak("यह फाइल लॉक नहीं है।")
    else:
        speak("गलत पासवर्ड। एक्सेस ठुकरा दिया गया है।")

if __name__ == "__main__":
    file_vault()
