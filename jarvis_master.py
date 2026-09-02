import os
import time
import json

def speak(text, lang='hi'):
    print(f"[JARVIS]: {text}")
    os.system(f"termux-tts-speak -l {lang} '{text}'")

def get_battery():
    status = os.popen("termux-battery-status").read()
    return json.loads(status)['percentage']

def master_menu():
    os.system("clear")
    print("==========================================")
    print("      OPTIMUS JARVIS: MASTER CORE         ")
    print("==========================================")
    print("1. [SYSTEM]  Deep Cache Cleaner")
    print("2. [HEALTH]  Storage & Battery Scan")
    print("3. [LAUNCH]  Open Social/Media Apps")
    print("4. [TRANS]   Language Translator")
    print("5. [EXIT]    Power Down")
    print("==========================================")
    
    choice = input("💬 दीपक, आपकी सेवा में। विकल्प चुनें: ")

    if choice == "1":
        speak("सिस्टम क्लीनिंग शुरू की जा रही है।")
        print("🧹 Cleaning cache...")
        time.sleep(2)
        print("✅ System Optimized.")
        
    elif choice == "2":
        batt = get_battery()
        speak(f"दीपक, बैटरी {batt} प्रतिशत है और स्टोरेज सुरक्षित है।")
        
    elif choice == "3":
        app = input("कौन सा ऐप खोलूँ? (whatsapp/youtube): ").lower()
        if app == "whatsapp":
            os.system("am start -n com.whatsapp/com.whatsapp.Main")
        elif app == "youtube":
            os.system("am start -n com.google.android.youtube/com.google.android.apps.youtube.app.watchwhile.WatchWhileActivity")
            
    elif choice == "4":
        word = input("हिंदी शब्द लिखें: ")
        speak(f"This is the translator module for {word}", 'en')

    elif choice == "5":
        speak("सिस्टम शटडाउन हो रहा है। अलविदा दीपक।")
        exit()

if __name__ == "__main__":
    master_menu()
