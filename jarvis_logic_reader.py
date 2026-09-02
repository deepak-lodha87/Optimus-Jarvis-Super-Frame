import os

class LogicReader:
    def __init__(self):
        self.master = "Deepak"

    def explain_action(self, module_name):
        explanations = {
            "security": "Deepak sir, I am currently guarding your phone. If anyone tries to touch it, I will capture their image.",
            "scheduler": "Sir, I am monitoring the clock. I will alert you as soon as your next task is due.",
            "cleanup": "I am currently scanning for junk files to keep your Oppo Reno 12 Pro running fast.",
            "pulse": "I am checking your device health, including RAM and storage levels."
        }
        
        msg = explanations.get(module_name.lower(), "I am executing background protocols to optimize your experience, sir.")
        print(f"\n\033[1;36m[JARVIS EXPLANATION]:\033[0m {msg}")
        os.system(f'termux-tts-speak "{msg}"')

if __name__ == "__main__":
    reader = LogicReader()
    # उदाहरण के लिए:
    action = input("Which module's logic do you want to understand? ").lower()
    reader.explain_action(action)
