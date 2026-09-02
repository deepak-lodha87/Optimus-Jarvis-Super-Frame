import os
import time

def speak(text):
    os.system(f"termux-tts-speak '{text}'")

def listen():
    print("\n[👂 LISTENING...]")
    return os.popen("termux-speech-to-text").read().strip().lower()

def brain():
    os.system("clear")
    print("--- OPTIMUS JARVIS 2.0: NEURAL CONNECTOR ACTIVE ---")
    speak("दीपक, अब मेरा पूरा डेटाबेस आपकी आवाज़ से जुड़ चुका है। पूछिए।")
    
    while True:
        query = listen()
        print(f"User: {query}")

        # 1. Royal Enfield / Engine Search (Mechanical Database)
        if "royal enfield" in query or "engine" in query:
            speak("दीपक, रॉयल एनफील्ड के इंजनों का डेटाबेस लोड हो रहा है। क्या आप 350 सीसी यूसीई या नए जे-सीरीज़ इंजन के बारे में जानना चाहते हैं?")
            # यहाँ हम आपके पुराने मैकेनिकल फेजेस को ट्रिगर कर सकते हैं

        # 2. Suits / Blueprints (Stark Database)
        elif "suit" in query or "blueprint" in query:
            speak("एक्सेसिंग स्टार्क डेटाबेस। आयरन मैन और स्पाइडर मैन सूट्स के ब्लूप्रिंट्स तैयार हैं।")

        # 3. Time/Date (Utility)
        elif "time" in query:
            os.system("date +'%I:%M %p' | xargs -I {} termux-tts-speak 'अभी समय {} हुआ है'")

        # 4. Phase 100 Launch (Main System)
        elif "full system" in query or "launch" in query:
            speak("सभी 100 लेयर्स को लोड किया जा रहा है।")
            os.system("python jarvis_final.py")
            break

        elif "exit" in query:
            speak("सिस्टम स्टैंडबाय मोड पर जा रहा है।")
            break
            
        else:
            speak("माफ कीजिये, इस कमांड को डेटाबेस में जोड़ने की ज़रूरत है।")

if __name__ == "__main__":
    brain()
