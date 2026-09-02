import os
import time
import subprocess

class SecurityLock:
    def __init__(self):
        self.master = "Deepak"
        self.secret_word = "Jarvis, activate Protocol 108" # आपका गुप्त शब्द

    def authenticate(self):
        print("\n\033[1;31m[SYSTEM LOCKED]\033[0m")
        os.system('termux-tts-speak "System is locked. Please provide the secret keyphrase, Deepak sir."')
        
        print("\033[1;33m[LISTENING...]\033[0m")
        # वॉयस रिकॉर्डिंग शुरू करना (5 सेकंड के लिए)
        os.system("termux-microphone-record -f auth_voice.mp3 -l 5")
        time.sleep(5)
        os.system("termux-microphone-record -q") # रिकॉर्डिंग रोकना

        # यहाँ हम अभी सिमुलेशन कर रहे हैं, अगले फेज में हम इसे असली वॉयस-टू-टेक्स्ट से जोड़ेंगे
        print("\033[1;36m[ANALYZING VOICE PATTERNS...]\033[0m")
        time.sleep(2)
        
        # यूज़र इनपुट के जरिए अभी टेस्ट करें
        user_voice_input = input("Speak Secret Phrase: ")
        
        if user_voice_input.lower() == self.secret_word.lower():
            print("\033[1;32m[ACCESS GRANTED]\033[0m Welcome back, Master Deepak.")
            os.system('termux-tts-speak "Identity confirmed. Access granted. All systems online."')
            return True
        else:
            print("\033[1;31m[ACCESS DENIED]\033[0m Intruder alert!")
            os.system('termux-tts-speak "Unauthorized access attempt detected. Locking system core."')
            return False

if __name__ == "__main__":
    lock = SecurityLock()
    if lock.authenticate():
        # सफल होने पर अगला मॉड्यूल यहाँ लोड करें
        os.system("python jarvis_daily_brief.py")
