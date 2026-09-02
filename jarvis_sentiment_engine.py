import os

class SentimentEngine:
    def __init__(self):
        self.master = "Deepak"

    def analyze_and_respond(self, user_text):
        print(f"\n\033[1;35m[SENTIMENT ANALYSIS]\033[0m Scanning emotional frequency...")
        
        # सरल कीवर्ड आधारित विश्लेषण
        positive = ["good", "happy", "fine", "great", "excellent"]
        negative = ["tired", "bored", "sad", "bad", "stress"]
        urgent = ["quick", "fast", "hurry", "now"]

        user_text = user_text.lower()
        
        if any(word in user_text for word in positive):
            msg = "I am glad to hear that, Deepak sir. Systems are performing at peak efficiency to match your energy."
        elif any(word in user_text for word in negative):
            msg = "I am sorry you feel that way, sir. Should I run a system cleanup or play some relaxing music?"
        elif any(word in user_text for word in urgent):
            msg = "Acknowledged, sir. Minimizing dialogue. All systems prioritized for speed."
        else:
            msg = "Systems nominal. Standing by for your next command, Deepak sir."

        print(f"\033[1;32m[JARVIS]:\033[0m {msg}")
        os.system(f'termux-tts-speak "{msg}"')

if __name__ == "__main__":
    engine = SentimentEngine()
    user_input = input("How are you feeling today, Deepak sir? ")
    engine.analyze_and_respond(user_input)
