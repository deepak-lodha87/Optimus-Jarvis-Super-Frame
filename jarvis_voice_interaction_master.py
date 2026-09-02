import os
import sys
import time

try:
    import speech_recognition as sr
    from gtts import gTTS
except ImportError as e:
    print(f"\033[1;31m[CRITICAL]: Dependency missing -> {e}\033[0m")
    print("कृपया पहले 'स्टेप 2' वाली कमांड चलाकर लाइब्रेरी इंस्टॉल करें।")
    sys.exit(1)

class JarvisVoiceInteractionMaster:
    def __init__(self):
        self.master = "Deepak"
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        print("\033[1;36m[SYSTEM]: Calibrating microphone for ambient noise...\033[0m")
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=2)
            self.recognizer.energy_threshold = 300  # संवेदनशीलता सेटिंग्स

    def speak(self, text):
        """सुरक्षित मीडिया प्लेयर राउटिंग बाईपास"""
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

    def listen_voice(self):
        """लाइव माइक्रोफोन स्कैन - नो टाइपिंग ग्रिड"""
        with self.microphone as source:
            try:
                audio = self.recognizer.listen(source, timeout=None, phrase_time_limit=4)
                command = self.recognizer.recognize_google(audio, language='en-US')
                print(f"\033[1;37m[SPOKEN DATA DETECTED]: {command}\033[0m")
                return command.lower()
            except sr.UnknownValueError:
                return ""
            except sr.RequestError:
                print("\033[1;31m[ERROR]: Voice server connection timeout.\033[0m")
                return ""
            except Exception:
                return ""

    def trigger_social_intelligence(self, topic):
        """रियल-टाइम सोशल रिपॉन्स डेटाबेस"""
        if any(word in topic for word in ["starter", "start"]):
            self.speak("Deepak sir, use an open ended question about her profile to keep it spontaneous.")
        elif any(word in topic for word in ["boring", "slow"]):
            self.speak("The conversation is getting slow, sir. Ask her if she prefers mountains or beaches.")
        elif any(word in topic for word in ["dry", "reply"]):
            self.speak("Dry response detected, Deepak sir. Tell her that it seems like a busy Sunday and you will catch up later.")
        else:
            self.speak("Strategic module loaded, but command parameters did not match, sir.")

    def run_voice_core(self):
        os.system('clear')
        print("\033[1;34m" + "="*50 + "\033[0m")
        print(f"\033[1;37;44m   OPTIMUS JARVIS: AUTOMATED VOICE CHANNELS LIVE   \033[0m")
        print("\033[1;34m" + "="*50 + "\033[0m")
        
        self.speak("Voice engine active, Deepak sir. Persistent background listening mode enabled.")
        print("\n\033[1;32m[SCANNING...] बिना कुछ टाइप किए सीधे 'Hello Jarvis' बोलें...\033[0m")
        
        while True:
            spoken_text = self.listen_voice()
            
            # वेक-वर्ड डिटेक्शन प्रोटोकॉल
            if "hello jarvis" in spoken_text or "jarvis" in spoken_text:
                self.speak("Okay boss, bolie! Interaction matrix is standing by.")
                
                # सिचुएशन कमांड के लिए एक्टिव स्कैन मोड
                print("\033[1;35m[AWAITING COMMAND]: 'starter', 'boring', या 'dry' बोलें...\033[0m")
                scenario_command = self.listen_voice()
                
                if any(word in scenario_command for word in ["starter", "start", "boring", "slow", "dry", "reply"]):
                    self.trigger_social_intelligence(scenario_command)
                elif "exit" in scenario_command or "stop" in scenario_command:
                    self.speak("Returning to background scan.")
                else:
                    self.speak("Timeout. Resuming passive background monitoring.")

            elif "shutdown core" in spoken_text:
                self.speak("Shutting down automated voice network. Goodbye, Deepak sir.")
                break

if __name__ == "__main__":
    jarvis_voice = JarvisVoiceInteractionMaster()
    jarvis_voice.run_voice_core()
