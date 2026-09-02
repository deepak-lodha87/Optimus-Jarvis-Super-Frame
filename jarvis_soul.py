import time

class JarvisSoul:
    def __init__(self):
        self.user_name = "Deepak"

    def analyze_sentiment(self, user_input):
        print(f"\033[1;36m[SOUL]\033[0m Analyzing user sentiment...")
        time.sleep(1.5)
        
        # Simple Logic: Checking keywords for sentiment
        positive_words = ["good", "great", "ha", "yes", "perfect", "badhiya"]
        negative_words = ["slow", "error", "bad", "wrong", "bekar"]
        
        input_lower = user_input.lower()
        
        if any(word in input_lower for word in positive_words):
            mood = "POSITIVE"
            response = f"I'm glad you're satisfied, {self.user_name} sir! Let's keep the momentum going."
        elif any(word in input_lower for word in negative_words):
            mood = "FRUSTRATED"
            response = f"I apologize, {self.user_name} sir. I will optimize my processes immediately to match your pace."
        else:
            mood = "NEUTRAL"
            response = f"Standing by and ready for your next command, sir."

        print(f" \033[1;37m[DETECTED MOOD]\033[0m: {mood}")
        print(f"\n\033[1;35m[VOICE] {response}\033[0m")

if __name__ == "__main__":
    soul = JarvisSoul()
    # Simulating a positive user input
    soul.analyze_sentiment("Ha, perfect hai!")
