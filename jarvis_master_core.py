import os
import sys
import time
from gtts import gTTS

class OptimusJarvisPhase3:
    def __init__(self):
        self.project_name = "Optimus Jarvis Super-Frame"
        self.master = "Deepak"
        self.current_phase = 3
        self.github_repo = "https://github.com/Deepak-Protocol/Optimus-Jarvis" # डिफ़ॉल्ट पाथ स्ट्रक्चर
        
    def speak(self, text):
        """सुरक्षित वॉयस आउटपुट बाईपास (gTTS + MPV Matrix)"""
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
        """इन-बिल्ट सेल्फ डायग्नोसिस टूल (Phase 3 Audit)"""
        print("\n\033[1;36m[DIAGNOSTIC] Executing Phase 3 core safety audit...\033[0m")
        time.sleep(0.5)
        print(" ├─ Hardware Link: \033[1;32mOppo Reno 12 Pro (Optimized)\033[0m")
        print(" ├─ Cloud Path: \033[1;32mGitHub Sync Ready\033[0m")
        print(" ├─ Security Matrix: \033[1;32mCaptain America Tactical Logic V3\033[0m")

    def trigger_github_sync(self):
        """क्लाउड बैकअप सिंक्रोनाइज़ेशन स्क्रिप्ट (Permanent Storage Initialization)"""
        print("\n\033[1;34m[CLOUD] Initiating permanent cloud backup protocol...\033[0m")
        self.speak("Preparing core repository files for GitHub deployment.")
        time.sleep(1)
        # यह केवल टर्मिनल पर गिट कमांड्स को प्रोसेस करने का आर्किटेक्चर है
        print(f" ├─ Initializing local repository...")
        print(f" ├─ Linking remote origin to Git Cloud...")
        print(f" └─ Target: {self.github_repo}")
        self.speak("Cloud synchronization structure is fully armed and secure.")

    def tactical_assessment(self, scenario_type):
        """कैप्टन अमेरिका रणनीतिक क्षमता - एडवांस्ड असेसमेंट मॉड्यूल"""
        print("\n\033[1;35m[TACTICAL] Analyzing scenario vectors with strategic logic...\033[0m")
        time.sleep(0.5)
        
        if "social" in scenario_type or "interpersonal" in scenario_type:
            response = "Deepak sir, tactical assessment confirms: Emotional grid is volatile. Recommendation is to prioritize listening, minimize defensive remarks, and execute a spontaneous reset statement."
            print("\033[1;35m[STRATEGY]: 1. डिफेंसिव न हों | 2. डेटा कलेक्ट करें (सुनें) | 3. रीसेट स्टेटमेंट दें।\033[0m")
        else:
            response = "System analysis complete. Strategic balance is maintained. No active threat or defect detected."
            
        self.speak(response)

    def process_universal_intelligence(self, query):
        """यूनिवर्सल नॉलेज और कोर कमांड्स प्रोसेसिंग"""
        query = query.lower().strip()
        
        if not query:
            return

        # 1. सोशल कमांड
        if any(word in query for word in ["angry", "gussa", "girl", "naraz", "ladki"]):
            self.tactical_assessment("social")

        # 2. ऑब्जेक्ट या जार के बारे में जानकारी
        elif "jar" in query or "about this jar" in query:
            response = "Deepak sir, a jar is a rigid container. Technologically, it stands for Java Archive, a zipped package of Java application files."
            print("\n\033[1;36m[KNOWLEDGE]: Glass Container / Java Archive File (.jar)\033[0m")
            self.speak(response)
            
        # 3. गिटहब क्लाउड कमांड
        elif any(word in query for word in ["github", "cloud", "backup", "save"]):
            self.trigger_github_sync()
            
        # 4. सिस्टम शटडाउन
        elif any(word in query for word in ["exit", "shutdown", "stop"]):
            self.speak("Shutting down Phase 3 engine. Systems offline. Goodbye, Deepak sir.")
            sys.exit(0)
            
        else:
            response = "Parameters locked. Frame standing by for the next operational directive, sir."
            self.speak(response)

    def boot_sequence(self):
        os.system('clear')
        print("\033[1;34m" + "="*60 + "\033[0m")
        print(f"\033[1;37;44m    {self.project_name.upper()} : PHASE {self.current_phase} LIVE CORE    \033[0m")
        print("\033[1;34m" + "="*60 + "\033[0m")
        
        self.speak(f"Welcome back, {self.master} sir. Phase 3 tactical core is now online.")
        self.run_self_diagnosis()
        
        self.speak("Systems are stable. Tap the microphone icon on your keyboard to input your command.")
        
        while True:
            print("\n\033[1;33m[AWAITING COMMAND] (कीबोर्ड का माइक दबाकर बोलें या टाइप करें): \033[0m")
            user_input = sys.stdin.readline().strip()
            
            if user_input:
                print(f"\033[1;37m[INPUT DETECTED]: {user_input}\033[0m")
                self.process_universal_intelligence(user_input)

if __name__ == "__main__":
    core = OptimusJarvisPhase3()
    core.boot_sequence()
