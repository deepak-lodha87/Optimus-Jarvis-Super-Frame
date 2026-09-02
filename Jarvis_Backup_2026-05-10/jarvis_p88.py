import os
import time

def speak(text):
    print(f"[JARVIS]: {text}")
    os.system(f"termux-tts-speak '{text}'")

def secret_diary():
    print("--- OPTIMUS JARVIS SUPER-FRAME: PHASE 88 ---")
    print("--- [INITIALIZING SECRET DIARY MODULE] ---")
    
    master_pass = "stark123" # यह आपका मुख्य पासवर्ड है
    password = input("🔐 Enter Master Password to access Diary: ")

    if password == master_pass:
        speak("एक्सेस मिल गया है। आप अपनी डायरी पढ़ सकते हैं या नया नोट लिख सकते हैं।")
        print("\n1. Read Diary\n2. Write New Entry")
        choice = input("Select option (1/2): ")

        if choice == '1':
            if os.path.exists("jarvis_diary.txt"):
                print("\n--- YOUR SECRET NOTES ---")
                with open("jarvis_diary.txt", "r") as f:
                    print(f.read())
            else:
                speak("दीपक, अभी डायरी खाली है।")
        
        elif choice == '2':
            note = input("Write your note: ")
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            with open("jarvis_diary.txt", "a") as f:
                f.write(f"[{timestamp}] - {note}\n")
            speak("नोट सुरक्षित रूप से सहेज लिया गया है।")
    else:
        speak("गलत पासवर्ड। सुरक्षा कारणों से एक्सेस रोक दिया गया है।")

if __name__ == "__main__":
    secret_diary()
