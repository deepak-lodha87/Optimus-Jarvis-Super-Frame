import os
import time

def speak(text):
    os.system(f"termux-tts-speak '{text}'")

def github_backup_protocol():
    print("--- OPTIMUS JARVIS SUPER-FRAME: PHASE 91 ---")
    print("--- [INITIALIZING GITHUB CLOUD BACKUP] ---")
    time.sleep(1)

    speak("दीपक, आपके डेटा को क्लाउड पर सुरक्षित करने की प्रक्रिया शुरू हो रही है।")
    
    # GitHub setup check
    print("Checking Local Repository...")
    if not os.path.exists(".git"):
        print("⚠️ Repository not found. Initializing...")
        os.system("git init")
    
    # Backup process
    os.system("git add .")
    os.system('git commit -m "Jarvis Phase 91 Auto-Update"')
    
    print("\n✅ Code added to local staging.")
    speak("कोड लोकल स्टोरेज में सुरक्षित कर लिया गया है।")
    
    print("\n--- NEXT STEP: PUSH TO CLOUD ---")
    print("Note: Make sure you have connected your GitHub Token.")

if __name__ == "__main__":
    github_backup_protocol()
