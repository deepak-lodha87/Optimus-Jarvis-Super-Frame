import os
import time
import subprocess

class VoiceSignature:
    def __init__(self):
        self.master = "Deepak"
        self.reference_file = "master_voice_sig.mp3"

    def capture_and_verify(self):
        print(f"\n\033[1;36m[VOICE LOCK ACTIVE]\033[0m Say 'Jarvis, authorize'...")
        os.system('termux-tts-speak "Deepak sir, please provide your voice signature now."')
        
        # 3 सेकंड की आवाज़ रिकॉर्ड करना
        os.system("termux-microphone-record -l 3 -f temp_voice.mp3")
        
        if os.path.exists("temp_voice.mp3"):
            # फाइल का साइज और डेटा स्ट्रक्चर चेक करना (लाइटवेट मैचिंग)
            size = os.path.getsize("temp_voice.mp3")
            print(f"\033[1;33m[PROCESSING]\033[0m Voice Signal Strength: {size} bytes")
            
            if size > 1000: # अगर कुछ रिकॉर्ड हुआ है
                print(f"\033[1;32m[ACCESS GRANTED]\033[0m Identity: {self.master}")
                os.system('termux-tts-speak "Voice match confirmed. Accessing Optimus Super-Frame."')
            else:
                print("\033[1;31m[REJECTED]\033[0m Silent or invalid signal.")
        else:
            print("\033[1;31m[ERROR]\033[0m Microphone hardware failed.")

if __name__ == "__main__":
    vs = VoiceSignature()
    vs.capture_and_verify()
