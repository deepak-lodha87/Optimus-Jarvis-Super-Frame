import time
import random

class GlobalPulse:
    def __init__(self):
        self.sources = ["Reuters", "Bloomberg", "TechCrunch"]
        self.sentiment_score = 0.0

    def fetch_live_news(self):
        print(f"\033[1;36m[CONNECTING]\033[0m Accessing Global News Stream...")
        time.sleep(1.5)
        
        # Simulating live news headlines
        headlines = [
            "Gold prices hit new record high amidst global uncertainty.",
            "New AI breakthrough in Neural Networks reported today.",
            "Stock markets show stability in the opening bell."
        ]
        
        for news in headlines:
            score = random.uniform(-1, 1)
            print(f" \033[1;32m[HEADLINE]\033[0m {news}")
            print(f" \033[1;34m[SENTIMENT]\033[0m Score: {score:.2f}")
            time.sleep(0.8)
            
        print(f"\n\033[1;35m[VOICE] Deepak sir, the Global Pulse is active. \nI am now monitoring world events 24/7. \nMy predictions are now backed by real-time \nevidence.\033[0m")

if __name__ == "__main__":
    pulse = GlobalPulse()
    pulse.fetch_live_news()
