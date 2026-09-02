import time, os

class KnowledgeEngine:
    def __init__(self):
        self.daily_topic = "Quantum-Resistant Encryption"
        self.vocab_word = "Superfluous"

    def run_daily_briefing(self):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS KNOWLEDGE-ENGINE : PHASE 14 - STEP 6    \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        print("\033[1;33m[RESEARCHING]\033[0m Scanning International Tech Journals...")
        time.sleep(1.5)
        
        brief = [
            ("Technical Focus", self.daily_topic),
            ("Market Impact", "Security Sector Growth Predicted"),
            ("Advanced English", self.vocab_word),
            ("Learning Status", "Integrated into Neural-Link")
        ]
        
        for key, value in brief:
            print(f" \033[1;32m[+] {key:18}:\033[0m {value}")
            time.sleep(0.8)

        print(f"\n\033[1;32m[SUCCESS] Daily Research Summary Ready for Deepak-Prime.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, while the world sleeps, I am \nlearning. I have analyzed the latest shifts in \nencryption and filtered the most sophisticated \nvocabulary for your upcoming meetings. Knowledge \nis the only asset that never depreciates. \nLet's stay ahead of the curve.\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    ke = KnowledgeEngine()
    ke.run_daily_briefing()
