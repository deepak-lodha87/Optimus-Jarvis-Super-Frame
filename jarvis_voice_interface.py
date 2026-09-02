import os
import time
import json

class VoiceCommandInterface:
    def __init__(self):
        self.master = "Deepak"

    def listen_and_execute(self):
        print(f"\n\033[1;36m[LISTENING]\033[0m Awaiting your command, {self.master} sir...")
        
        # आवाज़ को टेक्स्ट में बदलने के लिए एंड्रॉइड का इंजन इस्तेमाल करना
        result = os.popen("termux-speech-to-text").read().strip().lower()
        
        if result:
            print(f"\033[1;32m[RECEIVED]:\033[0m {result}")
            
            if "status" in result or "battery" in result:
                os.system("python jarvis_system_health.py")
            elif "briefing" in result or "report" in result:
                os.system("python jarvis_daily_brief.py")
            elif "exit" in result or "stop" in result:
                os.system('termux-tts-speak "Understood sir. Systems going to standby."')
                return False
            else:
                msg = f"Sorry Deepak sir, I heard {result}, but that command is not in my database."
                os.system(f'termux-tts-speak "{msg}"')
        else:
            print("\033[1;31m[SILENCE]\033[0m No voice input detected.")
        
        return True

if __name__ == "__main__":
    vci = VoiceCommandInterface()
    os.system('termux-tts-speak "Voice control active. How can I help you, Deepak sir?"')
    
    # लूप ताकि जार्विस सुनता रहे
    active = True
    while active:
        active = vci.listen_and_execute()
        time.sleep(1)
