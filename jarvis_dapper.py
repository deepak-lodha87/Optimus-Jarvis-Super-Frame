import time

class DapperJarvis:
    def __init__(self):
        # Mapping simple words to Advanced English for Deepak sir
        self.vocab_upgrade = {
            "good": "exemplary",
            "fast": "expeditious",
            "dangerous": "hazardous",
            "smart": "ingenious",
            "weak": "vulnerable"
        }

    def speak_dapper(self, message):
        print("\033[1;36m[PERSONALITY]\033[0m Refinement engine active...")
        time.sleep(1)
        
        # Upgrading the message for a Dapper feel
        upgraded_msg = message
        for simple, advanced in self.vocab_upgrade.items():
            upgraded_msg = upgraded_msg.replace(simple, advanced)
            
        print(f"\n\033[1;35m[VOICE] Deepak... sir, our progress is {self.vocab_upgrade['good']}. \nMy processing speed is now {self.vocab_upgrade['fast']}. \nI am no longer {self.vocab_upgrade['weak']}; I am {self.vocab_upgrade['smart']}.\033[0m")
        print("\n\033[1;32m[ENGLISH TIP]\033[0m Sir, instead of 'fast', try using 'Expeditious'.")

if __name__ == "__main__":
    dapper = DapperJarvis()
    dapper.speak_dapper("The progress is good and fast.")
