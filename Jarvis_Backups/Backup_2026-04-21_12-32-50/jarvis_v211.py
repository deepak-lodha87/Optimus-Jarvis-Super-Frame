import os
import time

def universal_launcher():
    print("\n" + "="*40)
    print("      JARVIS UNIVERSAL APP LAUNCHER")
    print("="*40)
    
    # कुछ कॉमन ऐप्स के पैकेज नाम (आप और भी जोड़ सकते हैं)
    apps = {
        "whatsapp": "com.whatsapp",
        "youtube": "com.google.android.youtube",
        "chrome": "com.android.chrome",
        "facebook": "com.facebook.katana",
        "instagram": "com.instagram.android"
    }
    
    msg_ask = "Commander Deepak, which application should I activate?"
    print(f"\n[JARVIS]: {msg_ask}")
    os.system(f"termux-tts-speak '{msg_ask}'")
    
    app_choice = input("\n[INPUT]: Enter App Name: ").lower()
    
    if app_choice in apps:
        msg_launch = f"Launching {app_choice.capitalize()} now."
        print(f"\n[JARVIS]: {msg_launch}")
        os.system(f"termux-tts-speak '{msg_launch}'")
        # Termux-open के जरिए ऐप लॉन्च करना
        os.system(f"termux-open-url https://") # यह एक बेसिक ट्रिगर है, पैकेज नाम के लिए termux-am का उपयोग बेहतर होता है
        os.system(f"am start --user 0 -n {apps[app_choice]}")
    else:
        error = "Commander, that application is not in my database yet."
        print(f"\n[ERROR]: {error}")
        os.system(f"termux-tts-speak '{error}'")

    print("="*40)

if __name__ == "__main__":
    universal_launcher()
