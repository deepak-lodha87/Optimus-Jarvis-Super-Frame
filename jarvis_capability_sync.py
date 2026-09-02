import time

class MasterCapabilities:
    def __init__(self):
        self.systems = ["Nano-Fab", "Flight-Core", "Neural-Link", "Ghost-Net"]

    def run_all_checks(self):
        print(f"\033[1;36m[SYSTEM-CHECK]\033[0m Initializing Full-Spectrum Capability Scan...")
        time.sleep(1)
        
        for sys in self.systems:
            print(f" \033[1;32m[OK]\033[0m {sys} is online and operational.")
            time.sleep(0.3)
            
        print("\n\033[1;35m[VOICE] Deepak sir, I am capable of managing your \nworld, your body, and your digital footprint. \nI am your shield, your wings, and your \ninfinite memory.\033[0m")

if __name__ == "__main__":
    jarvis = MasterCapabilities()
    jarvis.run_all_checks()
