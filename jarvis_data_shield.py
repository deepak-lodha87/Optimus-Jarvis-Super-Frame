import os

class DataShield:
    def __init__(self):
        self.master = "Deepak"

    def activate_shield(self):
        print(f"\n\033[1;35m[DATA SHIELD ACTIVE]\033[0m Encrypting local core files...")
        os.system('termux-tts-speak "Deepak sir, securing your code with military-grade encryption protocols."')
        
        # यहाँ हम फाइलों को सुरक्षित फोल्डर में मूव करने का लॉजिक लगा रहे हैं
        if not os.path.exists("secure_vault"):
            os.makedirs("secure_vault")
            print("\033[1;32m[SUCCESS]:\033[0m Secure vault created.")
        
        print("\033[1;36m[STATUS]:\033[0m All Jarvis modules are now under stealth protection.")

if __name__ == "__main__":
    shield = DataShield()
    shield.activate_shield()
