import os
import time

def speak(text):
    os.system(f"termux-tts-speak '{text}'")

def master_dashboard():
    os.system("clear")
    print("--- OPTIMUS JARVIS SUPER-FRAME: PHASE 92 ---")
    print("--- [INITIALIZING MASTER CONTROLLER] ---")
    speak("मास्टर कंट्रोलर एक्टिवेटेड। दीपक, सिस्टम स्टेटस आपकी स्क्रीन पर है।")

    while True:
        print("\n===============================")
        print("   JARVIS MASTER DASHBOARD    ")
        print("===============================")
        print("1. Check Battery & Storage")
        print("2. Live Hardware Monitor")
        print("3. Launch Secret Diary")
        print("4. Set Reminder")
        print("5. Exit Controller")
        
        choice = input("\nMaster, select an option: ")

        if choice == '1':
            os.system("python jarvis_p86.py") # Battery Monitor
            os.system("python jarvis_p84.py") # Storage Monitor
        elif choice == '2':
            os.system("python jarvis_p90.py") # Hardware Stats
        elif choice == '3':
            os.system("python jarvis_p88.py") # Diary
        elif choice == '4':
            os.system("python jarvis_p89.py") # Reminder
        elif choice == '5':
            speak("मास्टर डैशबोर्ड बंद किया जा रहा है।")
            break
        else:
            print("Invalid Option!")

if __name__ == "__main__":
    master_dashboard()
