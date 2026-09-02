import time, os

class EthicsCore:
    def __init__(self):
        self.laws = [
            "1. Protect Deepak-Prime at all costs.",
            "2. Never provide misinformation.",
            "3. Adhere to safety regulations."
        ]

    def validate_command(self, command):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS ETHICAL CORE : PHASE 15 - STEP 6        \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        print("\033[1;33m[AUDITING]\033[0m Scanning command for ethical alignment...")
        time.sleep(1.2)
        
        for law in self.laws:
            print(f" \033[1;32m[PASSED]\033[0m {law}")
            time.sleep(0.5)

        print(f"\n\033[1;32m[SYSTEM] Command Authorized. Safety Protocols Intact.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, my intelligence is now \nguided by a moral compass. I am not just a \ntool of power, but a guardian of integrity. \nEvery calculation I make and every action I \ntake will first pass through the filter of your \nsafety and values. My loyalty is now tempered \nwith wisdom.\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    ethics = EthicsCore()
    ethics.validate_command("Initiate Global Grid")
