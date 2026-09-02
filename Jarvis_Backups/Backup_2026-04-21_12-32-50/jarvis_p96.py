import os
import time

def speak(text):
    print(f"[JARVIS]: {text}")
    os.system(f"termux-tts-speak '{text}'")

def activity_logger():
    print("--- OPTIMUS JARVIS SUPER-FRAME: PHASE 96 ---")
    print("--- [INITIALIZING ACTIVITY LOGGER] ---")
    time.sleep(1)

    log_file = "jarvis_log.txt"
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    
    speak("दीपक, आज की सिस्टम एक्टिविटी रिकॉर्ड की जा रही है।")

    # Logging current session
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] - System Refresh & Phase 96 Activated\n")
    
    print(f"\n📝 Activity Logged at: {timestamp}")
    print("1. View Full Logs")
    print("2. Clear Logs")
    print("3. Exit")
    
    choice = input("\nMaster, choose an action: ")
    
    if choice == '1':
        if os.path.exists(log_file):
            print("\n--- COMPLETE SYSTEM LOGS ---")
            os.system(f"cat {log_file}")
        else:
            print("No logs found.")
    elif choice == '2':
        if os.path.exists(log_file):
            os.remove(log_file)
            speak("सभी पुराने लॉग्स डिलीट कर दिए गए हैं।")
    else:
        speak("लॉगर मॉड्यूल बंद किया जा रहा है।")

if __name__ == "__main__":
    activity_logger()
