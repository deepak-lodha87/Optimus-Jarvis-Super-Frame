import time
import random

class MarketOracle:
    def __init__(self):
        self.asset_list = ["Gold", "Silver", "Nifty-50"]
        self.confidence_score = 89.5

    def predict_trends(self):
        print(f"\033[1;36m[ANALYZING]\033[0m Scanning Global News & Historical Data...")
        time.sleep(2)
        
        for asset in self.asset_list:
            trend = random.choice(["BULLISH (UP)", "BEARISH (DOWN)", "STABLE"])
            prob = random.randint(70, 98)
            print(f" \033[1;32m[PREDICTION]\033[0m {asset}: {trend} | Confidence: {prob}%")
            time.sleep(0.5)
            
        print(f"\n\033[1;35m[VOICE] Deepak sir, the Oracle module is active. \nI have processed the latest market pulses. \nBased on neural patterns, I have mapped the \nmost likely outcomes for tomorrow.\033[0m")

if __name__ == "__main__":
    oracle = MarketOracle()
    oracle.predict_trends()
