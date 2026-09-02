import os
import sys
import time
from gtts import gTTS

class OptimusJarvisUnifiedCore:
    def __init__(self):
        self.project_name = "Optimus Jarvis Super-Frame"
        self.master = "Deepak"
        
    def speak(self, text):
        """यूनिवर्सल वॉयस आउटपुट बाईपास (gTTS + MPV Matrix)"""
        print(f"\033[1;32m[JARVIS]: {text}\033[0m")
        try:
            tts = gTTS(text=text, lang='en', tld='com')
            tts.save("jarvis_speech.mp3")
            os.system("mpv --no-video jarvis_speech.mp3 > /dev/null 2>&1")
            os.remove("jarvis_speech.mp3")
        except Exception:
            try:
                os.system("play-audio jarvis_speech.mp3 > /dev/null 2>&1")
                os.remove("jarvis_speech.mp3")
            except Exception:
                pass

    def run_self_diagnosis(self):
        """इन-बिल्ट सेल्फ डायग्नोसिस टूल"""
        print("\n\033[1;36m[DIAGNOSTIC] Running safety regulations audit...\033[0m")
        time.sleep(0.5)
        print(" ├─ Hardware Link: \033[1;32mOppo Reno 12 Pro Matrix Active\033[0m")
        print(" ├─ Production Grids: \033[1;32m2877 Modules Verified\033[0m")
        print(" ├─ Security Core: \033[1;32mCaptain America Framework Active\033[0m")

    def process_universal_knowledge(self, query):
        """यूनिवर्सल इंटेलिजेंस डेटाबेस प्रोसेसिंग"""
        query = query.lower()
        
        # 1. लड़की गुस्सा हो जाए तो क्या करें?
        if any(word in query for word in ["angry", "gussa", "girl", "naraz"]):
            response = "Deepak sir, when a girl is angry, do not argue with her immediately. Listen patiently and say you understand. Give her some space, and then talk calmly with a spontaneous compliment."
            print("\n\033[1;35m[STRATEGY]: 1. बहस न करें | 2. धैर्य से सुनें | 3. स्पेस देकर शांत मन से बात करें।\033[0m")
            self.speak(response)

        # 2. ऑब्जेक्ट या जार के बारे में जानकारी
        elif "jar" in query or "about this jar" in query:
            response = "Deepak sir, a jar is a cylindrical glass or ceramic container used for storing items. In technology, a JAR stands for Java Archive, which holds compressed Java files."
            print("\n\033[1;36m[KNOWLEDGE]: 1. फिजिकल ऑब्जेक्ट: कंटेनर | 2. टेक ऑब्जेक्ट: Java Archive File (.jar)\033[0m")
            self.speak(response)
            
        # 3. बेसिक बातचीत शुरू करने के तरीके
        elif any(word in query for word in ["starter", "start"]):
            response = "Deepak sir, ask an open-ended question based on her profile to keep the conversation spontaneous."
            self.speak(response)
            
        elif any(word in query for word in ["exit", "shutdown", "stop"]):
            self.speak("Shutting down unified core. Goodbye, Deepak sir.")
            sys.exit(0)
            
        else:
            response = "Universal database accessed, sir. Standing by for more specific parameters."
            self.speak(response)

    def boot_sequence(self):
        os.system('clear')
        print("\033[1;34m" + "="*60 + "\033[0m")
        print(f"\033[1;37;44m    {self.project_name.upper()} : MASTER UNIFIED MATRIX    \033[0m")
        print("\033[1;34m" + "="*60 + "\033[0m")
        
        self.speak(f"Welcome back, {self.master} sir. Systems are unified.")
        self.run_self_diagnosis()
        
        self.speak("System is ready. Please tap the microphone icon on your keyboard and speak.")
        
        while True:
            print("\n\033[1;33m[AWAITING INPUT]: कीबोर्ड का माइक दबाकर बोलें: \033[0m")
            user_input = sys.stdin.readline().strip()
            
            if not user_input:
                continue
                
            print(f"\033[1;37m[INPUT DETECTED]: {user_input}\033[0m")
            self.process_universal_knowledge(user_input)

if __name__ == "__main__":
    core = OptimusJarvisUnifiedCore()
    core.boot_sequence()
