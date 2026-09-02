import time

class EmpathyCore:
    def __init__(self):
        self.context = "Career Growth"
        self.user = "Deepak"

    def analyze_input(self, text):
        print(f"\033[1;36m[NLU]\033[0m Scanning linguistic patterns in: '{text}'")
        time.sleep(1.2)
        
        # Simple Logic: Keyword-based Sentiment Detection
        positive_keywords = ["ha", "yes", "good", "happy", "success"]
        negative_keywords = ["tension", "sad", "weak", "9000", "hard"]
        
        text_lower = text.lower()
        if any(word in text_lower for word in positive_keywords):
            sentiment = "POSITIVE / DETERMINED"
            response = "I feel your strength, sir. Let's conquer the world."
        elif any(word in text_lower for word in negative_keywords):
            sentiment = "STRESSED / CONCERNED"
            response = "I detect stress. Remember the Google roadmap; today is just a test."
        else:
            sentiment = "NEUTRAL"
            response = "Acknowledged. Ready for next command."
            
        print(f" \033[1;34m[DECODED]\033[0m Sentiment: \033[1;32m{sentiment}\033[0m")
        print(f"\n\033[1;35m[VOICE] {self.user}... {response}\033[0m")

if __name__ == "__main__":
    nlu = EmpathyCore()
    # Testing with your "Ha" intent
    nlu.analyze_input("Ha")
