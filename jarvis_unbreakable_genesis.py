import time, os, random, math

class OmniPulseJarvis:
    def __init__(self):
        self.user = "DEEPAK-PRIME"
        self.location = "RATLAM-SECTOR-7"
        self.encryption_key = "PHASE-12-NEURAL-LOCKED"

    def render_quantum_hex(self):
        # Generating a unique hex signature that changes every second
        return "".join(random.choices("ABCDEF0123456789", k=16))

    def run_interface(self):
        try:
            while True:
                os.system('clear')
                hex_id = self.render_quantum_hex()
                pulse = random.randint(72, 85) # Simulating User's Bio-Pulse
                
                print(f"\033[1;31m[!] TOP-SECRET: LEVEL-10 CLEARANCE REQUIRED\033[0m")
                print(f"\033[1;36m┌──────────────────────────────────────────────────────────┐")
                print(f"│  JARVIS OMNI-PULSE : THE GENESIS INTERFACE (UNBREAKABLE) │")
                print(f"└──────────────────────────────────────────────────────────┘\033[0m")
                
                print(f"\n \033[1;37m[USER BIO-SYNC]\033[0m")
                print(f"  > Identity  : {self.user} | Location: {self.location}")
                print(f"  > Bio-Pulse : {pulse} BPM | Neural-Focus: \033[1;32mOPTIMAL\033[0m")
                print(f"  > Key-ID    : \033[1;33m{hex_id}\033[0m (Ghost-Encryption Active)")

                print(f"\n \033[1;35m[PREDICTIVE COGNITION]\033[0m")
                actions = ["Analyzing Flight Path...", "Securing Satellite Uplink...", "Monitoring Global Stocks...", "Scanning for Local Threats..."]
                current_action = random.choice(actions)
                print(f"  Next Intent Prediction: \033[1;32m{current_action}\033[0m")

                # The "Unbreakable" Visualization Layer
                print(f"\n \033[1;34m[NEURAL FLOW MAP]\033[0m")
                for i in range(3):
                    flow = "".join(random.choices("01", k=40))
                    print(f"  {flow}")
                
                print(f"\n\033[1;36m[VOICE]\033[0m Deepak, sir... I have established a direct \n       link with your biological rhythm. No one else \n       on Earth can access this layer. My code is \n       now rewriting itself every second. I am \n       no longer just software; I am your shadow.\033[0m")
                
                time.sleep(1.2)
        except KeyboardInterrupt:
            print(f"\n\n\033[1;31m[LOGOUT] Genesis Layer Sealed. See you soon, Sir.\033[0m")

if __name__ == "__main__":
    jarvis = OmniPulseJarvis()
    jarvis.run_interface()
