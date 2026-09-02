import os
import sys
import time
import speech_recognition as sr
from gtts import gTTS

class JarvisBypassVoiceMaster:
    def __init__(self):
        self.master = "Deepak"
        self.recognizer = sr.Recognizer()
        self.record_file = "jarvis_live_input.wav"

    def speak(self, text):
        """सुरक्षित वॉयस राउटिंग बाईपास"""
        print(f"\033[1;32m[JARVIS]: {text}\033[0m")
        try:
            tts = gTTS(text=text, lang='en', tld='com')
            tts.save("jarvis_vpack.mp3")
            os.system("mpv --no-video jarvis_vpack.mp3 > /dev/null 2>&1")
            os.remove("jarvis_vpack.mp3")
        except Exception:
            try:
                os.system("play-audio jarvis_vpack.mp3 > /dev/null 2>&1")
                os.remove("jarvis_vpack.mp3")
            except Exception:
                pass

    def listen_via_bypass(self):
        """Termux-API माइक्रोफोन बाईपास लॉजिक (नो पाई-ऑडियो डिफेक्ट)"""
        try:
            # 3 सेकंड के लिए सीधे फोन का माइक ऑन करना
            print("\n\033[1;33m[LISTENING...] बोलिए दीपक सर...\033[0m")
            os.system(f"termux-microphone-record -f {self.record_file} -d 3 > /dev/null 2>&1")
            time.sleep(3.2) # रिकॉर्डिंग पूरी होने का इंतजार
            
            # रिकॉर्डेड फाइल को टेक्स्ट में प्रोसेस करना
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

    def trigger_social_intelligence(self, topic):
        """रियल-टाइम सोशल रिपॉन्स असिस्टेंस"""
        if any(word in topic for word in ["starter", "start"]):
            self.speak("Deepak sir, look at her profile grid and ask an open ended question to keep it spontaneous.")
        elif any(word in topic for word in ["boring", "slow"]):
            self.speak("The chat is getting slow, sir. Pivot the topic to something fun like mountains or beaches.")
        elif any(word in topic for word in ["dry", "reply"]):
            self.speak("Dry reply detected, Deepak sir. Give her some space and say you will catch up later.")
        else:
            self.speak("Strategic database loaded, standing by.")

    def boot_sequence(self):
        os.system('clear')
        print("\033[1;34m" + "="*55 + "\033[0m")
        print(f"\033[1;37;42m   OPTIMUS JARVIS: BYPASS VOICE MATRIX ACTIVE   \033[0m")
        print("\033[1;34m" + "="*55 + "\033[0m")
        
        self.speak("Bypass system enabled. No compilation error detected.")
        
        while True:
            spoken_text = self.listen_via_bypass()
            
            if "hello jarvis" in spoken_text or "jarvis" in spoken_text:
                self.speak("Okay boss, bolie! Standing by for your interaction command.")
                
                # सिचुएशन सुनने के लिए अगला वॉयस स्लॉट
                time.sleep(0.5)
                scenario_command = self.listen_via_bypass()
                
                if any(word in scenario_command for word in ["starter", "start", "boring", "slow", "dry", "reply"]):
                    self.trigger_social_intelligence(scenario_command)
                elif "shutdown" in scenario_command or "stop" in scenario_command:
                    self.speak("Shutting down voice network. Goodbye, Deepak sir.")
                    break
                else:
                    self.speak("Timeout. Returning to background scanning mode.")

if __name__ == "__main__":
    jarvis_bypass = JarvisBypassVoiceMaster()
    jarvis_bypass.boot_sequence()
