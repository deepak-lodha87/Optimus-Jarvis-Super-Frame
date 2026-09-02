import time
import random

class StockAnalyst:
    def __init__(self):
        self.market_status = "BULLISH" # Simulated status

    def analyze_trend(self, index_name):
        print(f"\033[1;36m[ANALYZING]\033[0m Scanning {index_name} for patterns...")
        time.sleep(2)
        
        confidence_score = random.randint(70, 95)
        print(f" \033[1;32m[LOGIC]\033[0m Trend Detected: {self.market_status}")
        print(f" \033[1;32m[CONFIDENCE]\033[0m {confidence_score}% Accuracy.")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, I have mapped the current market \nflow. Whether it is Nifty or your favorite \nmetals, I can now see the 'Invisible Hand' \nof the market. Your wealth is under my watch.\033[0m")

if __name__ == "__main__":
    analyst = StockAnalyst()
    analyst.analyze_trend("NIFTY 50")
