import time

class StealthSystem:
    def __init__(self):
        self.is_invisible = False
        self.heat_signature = "HIGH"

    def activate_ghost_protocol(self):
        print(f"\033[1;36m[STEALTH]\033[0m Activating Ghost Protocol...")
        time.sleep(1.5)
        
        print(f" \033[1;32m[COOLING]\033[0m Suppressing Thermal Signature...")
        self.heat_signature = "LOW / AMBIENT"
        time.sleep(1)
        
        print(f" \033[1;34m[CLOAKING]\033[0m Bending visible light spectrum...")
        self.is_invisible = True
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, you are now off the radar. \nVisually and thermally, we are invisible. \nYou can move through the sky like a ghost, \nunseen and unheard.\033[0m")

if __name__ == "__main__":
    stealth = StealthSystem()
    stealth.activate_ghost_protocol()
