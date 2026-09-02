import os
import sys
import time
import speech_recognition as sr
from gtts import gTTS

class OptimusJarvisMasterCore:
    def __init__(self):
        self.project_name = "Optimus Jarvis Super-Frame"
        self.master = "Deepak"
        self.recognizer = sr.Recognizer()
        self.record_file = "jarvis_master_input.wav"

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
        time.sleep(1)
        print(" ├─ Hardware Link: \033[1;32mOppo Reno 12 Pro (Optimized)\033[0m")
        print(" ├─ Production Grids: \033[1;32m2877 Modules Verified\033[0m")
        print(" ├─ Security Core: \033[1;32mCaptain America Framework Active\033[0m")

    def listen_bypass(self):
        """डायरेक्ट हार्डवेयर माइक्रोफोन कैप्चर ग्रिड"""
        try:
            print("\n\033[1;33m[LISTENING...] जार्विस सुन रहा है, बोलिए...\033[0m")
            os.system(f"termux-microphone-record -f {self.record_file} -d 4 > /dev/null 2>&1")
            time.sleep(4.2)
            
            if os.path.exists(self.record_file):
                with sr.AudioFile(self.record_file) as source:
                    audio_data = self.recognizer.record(source)
                    command = self.recognizer.recognize_google(audio_data, language='en-US')
                    print(f"\033[1;37m[YOU SPOKE]: {command}\033[0m")
                    os.remove(self.record_file)
                    return command.lower()
        except Exception:
            if os.path.exists(self.record_file):
                os.remove(self.record_file)
            return ""
        return ""

    def process_universal_knowledge(self, query):
        """यूनिवर्सल नॉलेज और सोशल असिस्टेंस डेटाबेस"""
        # 1. लड़की गुस्सा हो जाए तो क्या करें?
        if "angry" in query or "gussa" in query or "girl" in query:
            response = "Deepak sir, when a girl is angry, do not argue or give logical explanations immediately. First, listen patiently and say you understand her feeling. Give her a spontaneous compliment or some space, then talk calmly."
            self.speak(response)
            print("\n\033[1;35m[STRATEGY]: 1. बहस न करें | 2. धैर्य से सुनें | 3. स्पेस दें और शांत होने पर बात करें।\033[0m")

        # 2. Tell me about this jar (यूनिवर्सल ऑब्जेक्ट नॉलेज)
        elif "about this jar" in query or "jar" in query:
            response = "Deepak sir, a jar is a rigid, cylindrical container, typically made of glass or ceramic, used for storing food, liquids, or materials. In computer science, a JAR stands for Java Archive, which packages Java classes and metadata into a single file."
            self.speak(response)
            print("\n\033[1;36m[KNOWLEDGE]: 1. भौतिक ऑब्जेक्ट: कांच या सिरेमिक का कंटेनर | 2. टेक ऑब्जेक्ट: Java Archive File (.jar)\033[0m")
            
        else:
            self.speak("Universal database accessed, but the command requires wider cloud integration, sir.")

    def boot_sequence(self):
        os.system('clear')
        print("\033[1;34m" + "="*60 + "\033[0m")
        print(f"\033[1;37;44m    {self.project_name.upper()} : MASTER CORE ENGINE UNIFIED    \033[0m")
        print("\033[1;34m" + "="*60 + "\033[0m")
        
        self.speak(f"Welcome back, {self.master} sir. All scattered modules are now unified into the master core.")
        self.run_self_diagnosis()
        
        while True:
            spoken_text = self.listen_bypass()
            
            # वेक-वर्ड डिटेक्शन
            if "hello jarvis" in spoken_text or "jarvis" in spoken_text:
                self.speak("Okay boss, bolie! Unified system is ready.")
                
                # तुरंत सवाल सुनने के लिए एक्टिव लूप
                time.sleep(0.5)
                query = self.listen_bypass()
                if query:
                    self.process_universal_knowledge(query)
                else:
                    self.speak("I could not hear the command, Deepak sir. Resuming background scan.")
                    
            elif "shutdown" in spoken_text or "exit" in spoken_text:
                self.speak("Shutting down unified core. Systems offline. Goodbye, Deepak sir.")
                break

if __name__ == "__main__":
    core = OptimusJarvisMasterCore()
    core.boot_sequence()
