import os
import time

class WhatsAppCommander:
    def __init__(self):
        self.master = "Deepak"

    def send_whatsapp(self, phone_number, message):
        print(f"\n\033[1;32m[UPLINKING]:\033[0m Contacting +91{phone_number}...")
        
        # व्हाट्सएप के स्पेसिफिक URI का उपयोग करना
        # स्पेस को '+' या '%20' से बदलना ज़रूरी है
        formatted_msg = message.replace(" ", "%20")
        
        # Android Intent के जरिए व्हाट्सएप खोलना
        command = f"am start -a android.intent.action.VIEW -d 'https://api.whatsapp.com/send?phone=91{phone_number}&text={formatted_msg}'"
        
        os.system('termux-tts-speak "Opening WhatsApp and preparing the message, Deepak sir."')
        os.system(command)
        
        # थोड़ा इंतज़ार ताकि व्हाट्सएप लोड हो जाए, फिर एंटर (भेजने) का निर्देश (अगर root है तो)
        time.sleep(2)
        print("\033[1;36m[SUCCESS]:\033[0m Message interface deployed.")

if __name__ == "__main__":
    wa = WhatsAppCommander()
    
    # उदाहरण के लिए (यहाँ आप अपना नंबर या किसी का भी नंबर डाल सकते हैं)
    number = input("Enter Phone Number (without 91): ")
    msg = input("Enter Message: ")
    
    wa.send_whatsapp(number, msg)
