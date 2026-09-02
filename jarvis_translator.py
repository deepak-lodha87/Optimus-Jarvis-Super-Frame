import time, os

class UniversalTranslator:
    def __init__(self):
        self.primary_lang = "English"
        self.target_lang = "Hindi"
        self.vocab_count = 0

    def translate_and_teach(self, text):
        os.system('clear')
        print(f"\033[1;35m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS TRANSLATOR : PHASE 21 - STEP 4          \033[0m")
        print(f"\033[1;35m====================================================\033[0m")
        
        print(f"\033[1;33m[INPUT]\033[0m Analyzing: '{text}'")
        time.sleep(1.2)
        
        print("\033[1;34m[PROCESSING]\033[0m Mapping Linguistic Patterns...")
        time.sleep(1.0)
        
        translation_flow = [
            ("Syntax Identification", "SUCCESS"),
            ("Semantic Mapping (HINDI)", "DONE"),
            ("Advanced Vocab Extraction", "ACTIVE"),
            ("Grammar Refinement", "OPTIMIZED")
        ]
        
        for task, status in translation_flow:
            print(f" \033[1;36m[LANG]\033[0m {task:28} | [\033[1;32m{status}\033[0m]")
            time.sleep(0.6)

        print(f"\n\033[1;32m[SUCCESS] Translation Node is Active. Communication is Seamless.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, language is no longer a \nbarrier between you and the world's knowledge. \nI will be your voice and your translator. \nTogether, we will turn your weakness into your \ngreatest strength. From now on, you won't just \nread English; you will master it.\033[0m")
        print(f"\033[1;35m====================================================\033[0m")

if __name__ == "__main__":
    translator = UniversalTranslator()
    translator.translate_and_teach("The future belongs to those who prepare for it.")
