import os
import sys
import time
from gtts import gTTS

class JarvisInteractionEngine:
    def __init__(self):
        self.master = "Deepak"
        self.project = "Optimus Jarvis Super-Frame"
        
    def speak(self, text):
        """सुरक्षित वॉयस राउटिंग बाईपास"""
        try:
            tts = gTTS(text=text, lang='en', tld='com')
            tts.save("jarvis_temp.mp3")
            os.system("mpv --no-video jarvis_temp.mp3 > /dev/null 2>&1")
            os.remove("jarvis_temp.mp3")
        except Exception:
            try:
                os.system("play-audio jarvis_temp.mp3 > /dev/null 2>&1")
                os.remove("jarvis_temp.mp3")
            except Exception:
                pass

    def voice_activation_simulate(self, command):
        """वॉयस एक्टिवेशन रेस्पॉन्स लूप"""
        print(f"\n\033[1;33m[YOU]: {command}\033[0m")
        if "hello jarvis" in command.lower():
            response = "Okay boss, bolie! Interaction matrix is fully active. How can I assist you today?"
            print(f"\033[1;32m[JARVIS]: {response}\033[0m")
            self.speak(response)
        else:
            response = "System is on standby, Deepak sir."
            print(f"\033[1;32m[JARVIS]: {response}\033[0m")
            self.speak(response)

    def get_social_guide(self, scenario):
        """सोशल असिस्टेंस मॉड्यूल: बातचीत के बेहतरीन तरीके"""
        print("\n\033[1;35m" + "═" * 50 + "\033[0m")
        print(f"\033[1;37;45m   JARVIS SOCIAL ASSISTANCE PROTOCOL   \033[0m")
        print("\033[1;35m" + "═" * 50 + "\033[0m")
        
        self.speak("Deepak sir, accessing interpersonal communication database.")

        guides = {
            "1": {
                "situation": "Conversation Starter (बातचीत की शुरुआत करने के लिए)",
                "tips": [
                    "सिंपल 'Hi' या 'Hello' के बजाय उसकी प्रोफाइल या वाइब से जुड़ा कोई ओपन-एंडेड सवाल पूछें।",
                    "उदाहरण: 'Hey, मुझे तुम्हारी प्रोफाइल का वाइब काफी क्रिएटिव लगा, क्या तुम आर्ट या डिजाइनिंग में इंटरेस्टेड हो?'"
                ],
                "speech": "Deepak sir, always use an open ended question based on her profile to start naturally."
            },
            "2": {
                "situation": "When Conversation gets Boring (जब बातचीत धीमी या बोरिंग हो जाए)",
                "tips": [
                    "सिचुएशनल ह्यूमर (मजाक) या ट्रेंडी टॉपिक्स का इस्तेमाल करें। खुद के बारे में ज्यादा बताने के बजाय उसके इंटरेस्ट पर फोकस करें।",
                    "उदाहरण: 'वैसे, अगर तुम्हें किसी अनजान ट्रिप पर जाना हो, तो पहाड़ों में जाना पसंद करोगी या बीच पर?'"
                ],
                "speech": "Shift the focus to her travel or lifestyle preferences to keep it engaging."
            },
            "3": {
                "situation": "Handling Dry Replies (अगर सामने से छोटा या रूखा जवाब आ रहा हो)",
                "tips": [
                    "जबरदस्ती बातचीत खींचने की कोशिश न करें। एक मजेदार काउंटर-स्टेटमेंट दें और उसे स्पेस दें।",
                    "उदाहरण: 'लगता है आज आपका संडे काफी बिजी जा रहा है! जब फ्री हो जाओ, तब बताना।'"
                ],
                "speech": "Give her some space and avoid double texting, Deepak sir."
            }
        }

        if scenario in guides:
            g = guides[scenario]
            print(f"\n\033[1;36m[SITUATION]: {g['situation']}\033[0m")
            for index, tip in enumerate(g['tips'], 1):
                print(f" {index}. {tip}")
            self.speak(g['speech'])
        else:
            print("\033[1;31mInvalid Scenario Matrix.\033[0m")

    def run_menu(self):
        os.system('clear')
        print("\033[1;34m⚡ OPTIMUS JARVIS: PHASE 2 CHANNELS LIVE ⚡\033[0m")
        
        # 1. वॉयस एक्टिवेशन का लाइव टेस्ट
        print("\n--- [TESTING VOICE ACTIVATION L01] ---")
        self.voice_activation_simulate("Hello Jarvis")
        
        time.sleep(2)
        
        # 2. सोशल असिस्टेंस लूप
        while True:
            print("\n--- [SOCIAL GUIDANCE CHANNELS] ---")
            print("1. Conversation Starter (शुरुआत कैसे करें)")
            print("2. Revive Boring Chat (बोरिंग चैट को मजेदार बनाएं)")
            print("3. Handle Dry Replies (रूखे जवाबों को कैसे संभालें)")
            print("4. Exit Core (बाहर निकलें)")
            
            choice = input("\nदीपक सर, सिचुएशन नंबर सिलेक्ट करें (1-4): ")
            if choice == "4":
                self.speak("Closing social assistance channel. Standing by.")
                print("\n\033[1;32m[SYSTEM]: जार्विस स्टैंडबाय मोड पर है।\033[0m")
                break
            else:
                self.get_social_guide(choice)
                input("\nअगला चैनल लोड करने के लिए ENTER दबाएं...")
                os.system('clear')

if __name__ == "__main__":
    engine = JarvisInteractionEngine()
    engine.run_menu()
